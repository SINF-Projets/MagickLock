# Projet 3 - Test-locker-back
#
# Name : Dewilde   Alexandre            Noma :  24572000
#        Dubois    Arnaud                       82622000
#        Dubois    Brieuc                       23752000
#        Duquesne  Vincent                      08032000
#
#
# Date : November - December 2020

import unittest
import LocklearBack as lb


class TestLockerBack (unittest.TestCase):

"""
    Test class LockerBack and its methods.

    @autor : Duquesne Vincent
    @date : 26 November 2020

"""

    def setUp(self):
        
        """  """
        
        self.l = lb.LockerBack("LockTest")


    def test_init(self):
        
        """ Test of the initialization method """

        self.assertEqual(self.l.sense_hat(), 0,     "Your LockerBack don't ")          # Test à prévoir pour vérifier si nous sommes bien lier avec la classe LockerBack
                                                                                       # Test pour vérifier si nos attributs sont tous bien valide.


    def test_run_decrypt_password(self):

        """ Test of the run_decrypt_password method """
                                                                                        # Test à prévoir pour vérifié si il y à bien un fichier mot de passe
                                                                                        # Test à prévoir pour vérifier que le fichier contient un mot de passe
                                                                                        # Test à prévoir si le mot de passe est bien conforme aux exigence demander
        password = file ????                                                            # Test à prévoir pour vérifié si le mot de passe est correctement décripter
        self.assertEqual(self.l.sense_hat(), 0,     "Your LockerBack don't ")           # Test à prévoir pour vérifier que le fichier contient un mot de passe
                                                                                        # Test à prévoir si le mot de passe est bien conforme aux exigence demander



    def test_create_cipher_text(self):

        """ Test of the create_cipher_text method """

        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)   