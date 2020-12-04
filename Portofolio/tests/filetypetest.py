import os
from django.test import TestCase

class FileTypeTestCase(TestCase):   


	def test_file(self):
        	for filename in os.listdir("./media/gallery"):
            		self.assertEqual(filename.endswith(".jpg"), True)