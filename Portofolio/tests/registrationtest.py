from django.test import TestCase    


class RegistrationTestCase(TestCase):

     def test_registration(self):
        files= os.listdir("./registration")
        self.assertEqual("apps.py" in files, True)