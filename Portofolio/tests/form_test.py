import os
from django.test import TestCase



class MailTest(TestCase):

    def test_file(self):
        check = False
        for filename in os.listdir("./Portofolio/templates"):
            if filename == "About.html":
                check=True
            self.assertEqual(check, True)
