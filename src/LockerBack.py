#!/usr/bin/python3
# -*- coding: utf-8 -*
#  This module deals with the Back-end of the locker.
#  @author Vincent Duquesne
#  @date Created on 26/11/2020
#  @date Last modification on 03/12/2020
#  @version 1.0.5
import os
import time
from snake import Snake
from lockerUI import LockerUI
from lib.crypto import encode, decode, hashing
from lib.file import delete, exists, read
from sense_emu import SenseHat


class LockerBack:
    def __init__(self, sense_hat=SenseHat(), password_secret='secret.txt', cipher_file='cipher.txt'):
        """ Initialization method """
        self.sense_hat = sense_hat
        self.wrong_counter = 0
        self.snake = Snake(sense_hat)
        self.locker_ui = LockerUI(sense_hat)
        self.password_secret = password_secret
        self.cipher_file = cipher_file

    def run_decrypt_password_and_cipher(self, password=None):
        """
        Method for decrypting the password
        :pre:
        :post:
        """
        if password is None:
            password = self.locker_ui.ask_gesture_code()

        with open(self.password_secret, 'r') as file:
            hashed_password = file.read()

        if hashed_password == hashing(password):
            with open(self.cipher_file, 'r') as file:
                cipher_text = file.read()
            
            self.locker_ui.show_message(decode(password, cipher_text))

            return True
        else:
            self.wrong_counter += 1
            
            if self.wrong_counter <= 3:
                self.locker_ui.show_message("Wrong password, try again...")
            else:
                self.delete_password_cipher()
                self.locker_ui.show_message("Wrong password, Information Delete!")
            
            return False

    def create_cipher_text(self, text=None, code=None):
        """
        Method for create a cipher text
        :pre:
        :post:
        """
        if text is None:
            text: str = self.locker_ui.ask_a_number_list()
        if code is None:
            code: str = self.locker_ui.ask_gesture_code()

        with open(self.password_secret, "w") as file:
            file.write(hashing(code))
        
        with open(self.cipher_file, "w") as file:
            file.write(encode(code, text))

    def delete_password_cipher (self):
        """
        Method for Deletes the message and the password
        :pre:
        :post:
        """
        os.remove(self.password_secret)
        os.remove(self.cipher_file)

    def run(self):
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
            if os.path.isfile(self.password_secret) and os.path.isfile(self.cipher_file):
                if self.run_decrypt_password_and_cipher():
                    if self.locker_ui.ask_binary_question('Would you remove the message ?'):
                        self.delete_password_cipher()
                    self.locker_ui.screen_saver()
            else:
                self.create_cipher_text()


if __name__ == '__main__':
    lockerBack = LockerBack()
    lockerBack.run()