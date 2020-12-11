#!/usr/bin/python3
# -*- coding: utf-8 -*

#  This module deals with the UI of the locker.
#  @author Arnaud Dubois
#  @date Created on 26/11/2020
#  @date Last modification on 03/12/2020
#  @version 1.0.2

import unittest
import sys
import os
sys.path.append("../src")
from LockerBack import LockerBack


class TestLockerBack (unittest.TestCase):

    def setUp(self):        
        self.l = LockerBack()

    

    def run_decrypt_password_and_cipher(self):
        

        
       pass 

        




    def test_create_cipher_text(self):
        self.l.create_cipher_text(text="regarde à droite", code="Salut ça va")
        with open(self.password_secret, "r") as file:
            c = file.read()
            self.assertEqual(t, hashing(code))
        with open(self.cipher_file, "r") as file:
            t = file.read()
            self.assertEqual(c, encode(code, text))



    def test_delete_password_cipher(self):
        self.l.delete_password_cipher()
        self.assertIsNone(self.password_secret)
        self.assertIsNone(self.cipher_file)


    def test_run(self):
        
        pass









if __name__ == '__main__':
    unittest.main(verbosity=2)    