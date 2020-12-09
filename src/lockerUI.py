#!/usr/bin/python3
# -*- coding: utf-8 -*

#  This module deals with the UI of the locker.
#  @author Brieuc Dubois
#  @date Created on 26/11/2020
#  @date Last modification on 08/12/2020
#  @version 1.1.0

from senseHat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED


def calculate_orientation(angle, precision=45):
    return int(int((angle+(precision/2))/precision) % (360/precision))


def get_direction_id(direction):
    return ['up', 'down', 'left', 'right'].index(direction.lower())


class LockerUI(object):
    """ This class allows to ask things to the user """
    def __init__(self, sense):
        self.sense = sense

    def ask_a_number_list(self, minimum=0, maximum=9, max_len=50):
        """ Ask a list of numbers to user

        :param (int=0) minimum: Minimum value of each number
        :param (int=9) maximum: Maximum value of each number
        :param (int=50) max_len: Maximum length of final message

        :post: Screen is clean at the end of function

        :return: (str) List of numbers
        """

        result = []

        for __ in range(max_len):
            current = minimum

            while True:
                self.sense.show_letter(str(current))

                event = self.sense.stick.wait_for_event()
                if event.direction == 'left' and event.action == ACTION_RELEASED:
                    current = max(minimum, current-1)

                elif event.direction == 'right' and event.action == ACTION_RELEASED:
                    current = min(maximum, current+1)

                elif event.direction == 'middle' and event.action == ACTION_RELEASED:
                    result.append(current)
                    break

                elif event.direction == 'middle' and event.action == ACTION_HELD:
                    self.sense.clear()
                    return ''.join(map(str, result)) + str(current)

    def show_message(self, *args, **kwargs):
        """ Display message on screen """
        self.sense.show_message(*args, **kwargs)

    def ask_gesture_code(self):
        """ Ask a succession of gesture to the user
        :return: (int) the final score
        """
        initial_gyroscope = self.sense.get_gyroscope().values()
        total_score = 1
        while True:
            event = self.sense.stick.wait_for_event()
            if event.action == ACTION_PRESSED or event.action == ACTION_RELEASED:
                if event.direction == 'middle':
                    return total_score
                else:
                    x, y, z = map(calculate_orientation, [x1 - x2 for (x1, x2) in zip(self.sense.get_gyroscope().values(), initial_gyroscope)])
                    score = (x << 6) + (y << 3) + z
                    score = (score << 2) + get_direction_id(event.direction)
                    total_score = (total_score << 11) + score
                    print(score, total_score)

    def ask_binary_question(self, question):
        self.show_message(question)
        self.show_message('Move the stick upwards for yes and downwards for no')
        while True:
            event = self.sense.stick.wait_for_event()
            if event.action == ACTION_HELD:
                if event.direction == 'up':
                    return True
                elif event.direction == 'down':
                    return False

    def screen_saver(self):
        self.sense.stick.wait_for_event()



""" Example of usage """
if __name__ == '__main__':
    s = SenseHat()
    s.low_light = True
    lockUI = LockerUI(s)
    code = lockUI.ask_gesture_code()
    lockUI.show_message(str(code))
