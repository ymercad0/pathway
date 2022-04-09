import unittest 
from model import Company

class TestCompany(unittest.TestCase):
	def setUp(self):
		self.company1 = Company(
			name="Microsoft",
			comp_cat="software",
			logo_img="https://bit.ly/3uWfYzK",
			banner_img="https://bit.ly/3xfolJs"
			)
	def test_types(self):
		pass

	def test_values(self):
		pass