#!/usr/bin/python3
# -*- coding: utf-8 -*

#  This module deals with the UI of the locker.
#  @author Arnaud Dubois
#  @date Created on 26/11/2020
#  @date Last modification on 29/11/2020
#  @version 1.0.1

from snake import Snake
import os
from lib.crypto import encode, decode, hashing
from lib.file import delete, exists

class LockerBack:

    def __init__(self, sense_hat):
        """ Initialization method """

        self.sense_hat = sense_hat
        self.wrong_counter = 0


    def run_decrypt_password(self):
        """ Method for decrypting the password """
        #demander le mot de passe au front

        password = None                                             # Le mot de passe (série de mouvement) est None
        with open ("Password_secret") as file:                      # On ouvre "Password_secret" dans File
            hashed_password = file.read()                           # On hache le mot de passe qui est écrit dans le File
        
        if hashed_password == hashing(password):                    # Si le mot de passe hachée est égale aux mot de passe (None) hachée
            with open ("cipher") as file:                               # On ouvre "cipher" dans File
                cipher_text = file.read()                               # Le text de cipher est écrit dans File  
            
            if self.wrong_counter > 3:                                  # Si le nombre d'essai pour le code est inférieur à 3
                decode(password, cipher_text)                               # On décode le mot de passe et le text de Cipher
            else:
                delete("Password_secret")                                   # On supprime le mot de passe
                delete("cipher")                                            # On supprime cipher (Text secret)
        else:
            self.wrong_counter += 1                                 # On ajoute 1 au compte des mauvaises erreurs
    
    
    
    def run_decrypt_cipher(self):
        """ Method for decrypting the cipher message """
        #demander le mot de passe au front
        
        with open ("cipher") as file:                               # On ouvre "cipher" dans File
            hashed_cipher = file.read()                           # On hache le message qui est écrit dans le File
        
        if self.run_decrypt_password is True:                    # Si la méthode de achage est Correct
            with open ("cipher") as file:                               # On ouvre "cipher" dans File
                decode("cipher")                                 # On decode le message cipher
                return ()
        else:
            self.wrong_counter += 1

    def create_cipher_text (self):
        """ """
        #TODO demander au front-end un nouveau mot de passe
        #TODO verifier l'user input
        password = None
        text = ""
        with open ("Password_secret", "w") as file:
            file.write(hashing(password))
        with open ("cipher", "w") as file:
            file.write(encode(password, text))

    def delete_password_cipher (self):
        """ Method for Deletes the message and code """
        delete("Password_secret")
        delete("cipher")

    def run (self):
        """
        faire tourner le snake.
        verifier si y a un mot de passe deja enregistrer
        si y a un mot de passe, demander qu'il le rentre
            si il y à un message, montrer le message
            sinon, crée un message
        si pas de mot de passe, demander qu'il en creer un puis de creer un message
        """
        snake = Snake(self.sense_hat)                                       # Défini un snake
        snake.run()                                                         # Lance le snake

        while True:
            if os.path.isfile("Password_secret"):                               # Si il y a un mot de passe dans file
                self.run_decrypt_password()                                     # Lancer la méthode run_decrypt_password       
                if os.path.isfile("cipher") and hashed_password == hashing(password):                                    # Si il y a un message cypher dans file
                    self.run_decrypt_cipher()                                   # Lancer la méthode run_decrypt_cipher
                else:
                    self.creat_cipher_text()                                     # Lancer la méthode creat_cipher_text
                    self.run_decrypt_cipher()                                    # Lancer la méthode run_decrypt_cipher()

        
    