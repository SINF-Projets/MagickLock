from snake import Snake
import os
from lib.crypto import encode, decode, hashing
from lib.file import delete, exists


class LockerBack:

    def __init__(self, sense_hat):
        self.sense_hat = sense_hat
        self.wrong_counter = 0



    def run_decrypt_password(self):
        #demander le mot de passe au front
        password = None
        with open ("Password_secret") as file:
            hashed_password = file.read()
        if hashed_password == hashing(password):
            with open ("cipher") as file:
                cipher_text = file.read()
            #FIXME passer au front-end   
            decode(password, cipher_text)
            #TODO demander la suppression du truc
        else:
            self.wrong_counter += 1

    def create_cipher_text (self):
        #TODO demander au front-end un nouveau mot de passe
        #TODO verifier l'user input
        password = None
        text = ""
        with open ("Password_secret", "w") as file:
            file.write(hashing(password))
        with open ("cipher", "w") as file:
            file.write(encode(password, text))

    def delete_password_cipher (self):
        delete("Password_secret")
        delete("cipher")



    def run (self):
        """
        faire tourner le snake.
        verifier si y a un mot de passe deja enregistrer
        si y a un mot de passe, demander qu'il le rentre
        si pas de mot de passe, demander qu'il en creer un puis de 
        creer un message
        """
        snake = Snake(self.sense_hat)
        snake.run()
        if os.path.isfile("Password_secret"):
            self.run_decrypt_password()
        else:
            self.create_cipher_text()

        
    