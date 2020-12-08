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
from locker_ui import LockerUI
from lib.crypto import encode, decode, hashing
from lib.file import delete, exists

class LockerBack:

    def __init__(self, sense_hat, password_secret, cipher_message):
        """ Initialization method """

        self.sense_hat = sense_hat
        self.wrong_counter = 0
        self.snake = Snake(sense_hat)
        self.locker_ui = LockerUI(sense_hat)
        self.password_secret = password_secret
        self.cipher = cipher_message
        self.choice = False
        self.shutdown = False


    def run_decrypt_password_and_cipher(self):
        """ 
        Method for decrypting the password 
        
        :pre: 
        :post: 
        """

        password = self.locker_ui.ask_gesture_code()

        with open (self.password_secret) as file:                      
            hashed_password = file.read()                           
        
        if hashed_password == hashing(password):                    
            with open (self.cipher) as file:                               
                cipher_text = file.read()                                 
            
            if self.wrong_counter < 3:                                  
                text = file.decode(hashed_password, cipher_text)
                self.locker_ui.show_message(self.text)
                                               
            else:
                self.delete_password_cipher()                                           
                self.locker_ui.show_message("Wrong password, Information Delete!")
        else:
            self.wrong_counter += 1                                
            self.locker_ui.show_message("Wrong password, try again...")


    def create_cipher_text (self):
        """ 
        Method for create a cipher text 
        
        :pre: 
        :post:
        """
        code = self.locker_ui.ask_gesture_code()
        text = self.locker_ui.ask_a_number_list()

        while file.read(self.password_secret) != self.code :
            
            self.text()

                with open (self.password_secret, "w") as file:
                    file.write(hashing(self.code)
                    return "Message accepted"
                
                with open (self.cipher, "w") as file:
                    file.write(encode(self.code, self.text)
                    return "Password accepted"


    def delete_password_cipher (self, False):
        """ 
        Method for Deletes the message and the password 
        
        :pre:
        :post:
        """
        
        if self.delete_password_cipher == True:
            file.delete("Password_secret")
            file.delete("cipher")
        else:
            pass


    def shutdown(self, False):
        """
        Method for shutdown the rasberry.

        :pre: 
        :post:
        """
        while self.shutdown() is not True:
            pass
        else:

        
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

        
        while True
            if self.choice == True or self.shutdown == False :
                
                if os.path.isfile(password_secret,cipher_message):                                          
                    self.run_decrypt_password_and_cipher()                                                  
                    if os.path.isfile(password_secret):
                        self.run_decrypt_password_and_cipher                                                   
                    else:
                        if self.delete_password_cipher() is True:
                            self.create_cipher_text()
                        else:
                            pass
                else:
                    self.create_cipher_text()
            else:
                break

    

if __name__ == '__main__':
    run()


        
    