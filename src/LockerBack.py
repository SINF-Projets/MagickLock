#!/usr/bin/python3
# -*- coding: utf-8 -*

#  This module deals with the Back-end of the locker.
#  @author Vincent Duquesne
#  @date Created on 26/11/2020
#  @date Last modification on 01/12/2020
#  @version 1.0.4

import RPi.GPIO as GPIO
import subprocess
import os
from snake import Snake
from locker_ui import LockerUI
from lib.crypto import encode, decode, hashing
from lib.file import delete, exists

class LockerBack:

    def __init__(self, sense_hat):
        """ Initialization method """

        self.sense_hat = sense_hat
        self.wrong_counter = 0
        self.snake = Snake(sense_hat)
        self.locker_ui = LockerUI(sense_hat)


    def run_decrypt_password_and_cipher(self):
        """ Method for decrypting the password """

        password = self.locker_ui.ask_gesture_code()

        with open ("Password_secret") as file:                      
            hashed_password = file.read()                           
        
        if hashed_password == hashing(password):                    
            with open ("cipher") as file:                               
                cipher_text = file.read()                                 
            
            if self.wrong_counter < 3:                                  
                text = file.decode(password, cipher_text)
                self.locker_ui.show_message(text)
                                               
            else:
                self.delete_password_cipher()                                           
                self.locker_ui.show_message("Wrong password, Information Delete!")
        else:
            self.wrong_counter += 1                                
            self.locker_ui.show_message("Wrong password, try again...")


    def create_cipher_text (self):
        """ Method for create a cipher text """

        message = self.locker_ui.ask_gesture_code()
        text = self.locker_ui.ask_a_number_list()

        while file.read("password_secret") != self.message() :
            
            self.text()

                with open ("Password_secret", "w") as file:
                    file.write(hashing(self.message()))
                
                with open ("cipher", "w") as file:
                    file.write(encode(self.message(), self.text()))


    def delete_password_cipher (self, None):
        """ Method for Deletes the message and code """
        self.delete_password_cipher == True

        file.delete("Password_secret")
        file.delete("cipher")


    def shutdown (self):
        
    def run (self):
        """
        faire tourner le snake.
        verifier si y a un mot de passe deja enregistrer
        si y a un mot de passe, demander qu'il le rentre
            si il y à un message, montrer le message
            sinon, crée un message
        si pas de mot de passe, demander qu'il en creer un puis de creer un message
        """
        snake = Snake(self.sense_hat)                                       
        snake.run()                                                         

        while True:
            if os.path.isfile("cipher"):                                          
                self.run_decrypt_password()                                                      
                if os.path.isfile("Password_secret"):       
                    self.run_decrypt_password_and_cipher()                                               
                else:
                    if self.delete_password_cipher() is True:


                    pass
            else:
                self.create_cipher_text()

    

if __name__ == '__main__':
    run()


        
    