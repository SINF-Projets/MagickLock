#!/usr/bin/python3
# -*- coding: utf-8 -*

#  This module deals with the snake game
#  @author Alexandre Dewilde
#  @date Created on 26/11/2020
#  @date Last modification on 29/11/2020
#  @version 0.1.1

import random
import time
from sense_hat import SenseHat


class Snake:
    def __init__(self, sense):
        """
        Args:
            sense (SenseHat): sensehat object to display the game
        """
        # This list is the coords of the parts of the snake where
        # the last element is the head and the first the taill
        self.snake_parts = [[3, 3]]
        self.sense = sense
        self.length = 1
        self.rewards = []
        self.direction = "up"
        #The special coords to unlock
        self.special_coord = self.generate_special_coords()
        self.special_coord_color = tuple([random.randint(200, 255), random.randint(215, 230), random.randint(0, 10)])
        self.actions = []


    def generate_special_coords(self):
        """Generate random coords for the special coords to unlock the raspberry"""
        special_coord = []
        for _ in range(2):
            coord = random.randint(1, 7)
            while coord == 3:
                coord = random.randint(1, 7)
            special_coord.append(coord)
        return special_coord


    def take_events(self, events):
        """Takes a list of events in input and apply the last to the snake

        Args:
            events (list): list of event
        """
        if len(events) > 0:
            self.actions.extend(events)
            self.direction = events[-1].direction


    def generate_random_colors(self):
        """ Generate a screen with random colors and add the special color for the special coords"""
        colors = [(random.randint(0, 200), random.randint(0, 200), random.randint(0, 255)) for _ in range(32)]
        grid = []
        for color in colors:
            grid.extend([color, color])
        grid[self.special_coord[0] + (self.special_coord[1] * 8)] = self.special_coord_color
        self.sense.set_pixels(grid)


    def generate_rewards(self):
        """Generate a new reward on the grid
        """
        coords = [random.randint(2, 7), random.randint(2, 7)]
        while coords in self.snake_parts:
            coords = [random.randint(2, 7), random.randint(2, 7)]
        self.rewards.append([random.randint(2, 7), random.randint(2, 7)])


    def check_stop_game(self):
        """check if we have to stop the game"""
        if len(self.actions) < 15 and self.snake_parts[-1] == self.special_coord:
            return True
        return False


    def move(self):
        """Move the snake according to the current direction
        """
        new_pos = self.snake_parts[-1][:]
        if self.direction == 'up':
            new_pos[1] -= 1
        elif self.direction == 'down':
            new_pos[1] += 1
        elif self.direction == 'left':
            new_pos[0] -= 1
        else:
            new_pos[0] += 1
        # When the snake is out of the grid
        if new_pos[0] > 7:
            new_pos[0] = 0
        elif new_pos[0] < 0:
            new_pos[0] = 7
        elif new_pos[1] > 7:
            new_pos[1] = 0
        elif new_pos[1] < 0:
            new_pos[1] = 7
        self.snake_parts.append(new_pos)
        self.actions.append(new_pos)


    def check_case_for_reward(self):
        """Check if the head of the snake is eating a reward
        """
        reward = next((reward for reward in self.rewards if self.snake_parts[-1] == reward), None)
        if reward is not None:
            self.rewards.remove(reward)
            self.length += 1
        else:
            # delete the last part of the snake
            del self.snake_parts[0]


    def check_for_collide(self):
        """check if the snake has collide with himself

        Returns:
            bool: if the snake head collide with one pars of it
        """
        return self.snake_parts[-1] in self.snake_parts[:-1]


    def display(self):
        """Display all elements on screen (snake, rewards)
        """
        black = (0, 0, 0)
        grid = [black] * 64
        for part in self.snake_parts:
            pixel = (part[1] *8 ) + part[0]
            grid[pixel] = (0, 255, 0)
        for reward in self.rewards:
            grid[(reward[1] * 8) + reward[0]] = (255, 0, 0)
        self.sense.set_pixels(grid)
    

    def reset(self):
        """Reset the game
        """
        self.__init__(self.sense)


    def run(self):
        """Run the game
        """
        self.sense.show_message('Snake', text_colour=self.special_coord_color)
        self.generate_random_colors()
        time.sleep(4)
        last_time = time.time()
        while True:
            #number of frames per second
            if (time.time() - 1) > last_time:
                last_time = time.time()
                self.take_events(self.sense.stick.get_events())
                self.move()
                self.check_case_for_reward()
                self.display()
                if self.check_for_collide():
                    #Wait a bit to show the colission
                    time.sleep(0.5)
                    self.sense.show_message('GAME OVER', text_colour=[255, 0, 0])
                    self.reset()
                if len(self.rewards) == 0:
                    self.generate_rewards()
                if self.check_stop_game():
                    break


if __name__ == "__main__":
    sense = SenseHat()
    snake = Snake(sense)
    snake.run()