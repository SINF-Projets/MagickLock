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
import lib

class TestLockerBack (unittest.TestCase):

    def setUp(self):        
        self.l = LockerBack()

    

    def run_decrypt_password_and_cipher(self):
        x = self.l.decrypt_password_and_cipher(password="Salut ça va")
        with open(self.l.password_secret, 'r') as file:
            hashed_password = file.read()
            self.assertNotEqual(hashed_password, "")
            if hashed_password == hashing(password):
                self.assertTrue(x)
            else:
                self.assertEqual(self.l.wrong_counter, self.l.wrong_counter + 1)
                if self.l.wrong_counter > 3:
                    self.assertIsNone(self.l.password_secret)
                self.assertFalse(x)



    def test_create_cipher_text(self):
        self.l.create_cipher_text(text="regarde à droite", code="Salut ça va")
        with open(self.l.password_secret, "r") as file:
            c = file.read()
            self.assertEqual(c, hashing(code))
        with open(self.l.cipher_file, "r") as file:
            t = file.read()
            self.assertEqual(t, encode(code, text))



    def test_delete_password_cipher(self):
        self.l.delete_password_cipher()
        self.assertIsNone(self.l.password_secret)
        self.assertIsNone(self.l.cipher_file)


    









if __name__ == '__main__':
    unittest.main(verbosity=2)  