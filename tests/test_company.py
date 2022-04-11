from model import Company
import unittest

class TestCompany(unittest.TestCase):
	def setUp(self):
		self.valid_link = "http://somelink.com" #used for ease of writing tests
		self.company1 = Company(
			name="Microsoft",
			category="software",
			logo_img="https://bit.ly/3uWfYzK",
			banner_img="https://bit.ly/3xfolJs"
			)
		self.company2 = Company(
			name="Google",
			category="Software",
			logo_img="http://somelink.com",
			banner_img="http://somelink.com"
			)

	def test_types(self):
		self.assertRaises(TypeError, Company, None, "software", self.valid_link,self.valid_link)
		self.assertRaises(TypeError, Company, "Netflix", 2, self.valid_link, self.valid_link)
		self.assertRaises(TypeError, Company, "Home Depot", "software", [], self.valid_link)
		self.assertRaises(TypeError, Company, "Netflix", "software", self.valid_link, None)
		self.assertRaises(TypeError, Company, "Netflix", "software", self.valid_link, self.valid_link,
			description=333)

	def test_values(self):
		self.assertRaises(ValueError, Company, "", "software", self.valid_link, self.valid_link)
		self.assertRaises(ValueError, Company, "Netfix", "", self.valid_link, self.valid_link)
		self.assertRaises(ValueError, Company, "Netflix", "software", "htp/broken_link", self.valid_link)
		self.assertRaises(ValueError, Company, "Netflix", "software", self.valid_link, "")

class TestReviews(unittest.TestCase):
	def setUp(self):
		pass

	def test_init_required(self):
		pass

	def test_init_optional(self):
		pass

	def test_score_values(self):
		pass

	if __name__ == "__main__":
		#failFast set to false in order to see all failing tests in one run
		unittest.main(failFast=False)