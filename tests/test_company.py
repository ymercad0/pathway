import unittest 
from model import Company

class TestCompany(unittest.TestCase):
	def setUp(self):
		self.company1 = Company(
			name="Microsoft",
			category="software",
			logo_img="https://bit.ly/3uWfYzK",
			banner_img="https://bit.ly/3xfolJs"
			)
		self.company2 = Company(
			name="Google",
			category="Software",
			logo_img="link_to_somewhere",
			banner_img="other_link"
			)
	def test_types(self):
		self.assertRaises(TypeError, Company, None, "software", "link","link")	
		self.assertRaises(TypeError, Company, "Netflix", 2, "link", "link")
		self.assertRaises(TypeError, Company, "Home Depot", "software", [], "link")
		self.assertRaises(TypeError, Company, "Netflix", "software", "link", None)
		self.assertRaises(TypeError, Company, "Netflix", "software", "link", "link", description=333)

	def test_values(self):
		pass


	if __name__ == "__main__":
		#failFast set to false in order to see all failing tests in one run
		unittest.main(failFast=False)