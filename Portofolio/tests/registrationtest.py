from django.test import TestCase    
import os

class RegistrationTestCase(TestCase):

     def test_registration(self):
        files= os.listdir("./registration")
        self.assertEqual("apps.py" in files, True)