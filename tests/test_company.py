from model import Company
import unittest

class TestCompany(unittest.TestCase):
	def setUp(self):
		self.valid_link = "http://somelink.com" #used for ease of writing tests
		self.valid_category = "Software"
		self.company1 = Company(
			name="Microsoft",
			category=self.valid_category,
			logo_img="https://bit.ly/3uWfYzK",
			banner_img="https://bit.ly/3xfolJs"
			)

		self.company2 = Company(
			name="Google",
			category=self.valid_category,
			logo_img="http://somelink.com",
			banner_img="http://somelink.com"
			)

	def test_types(self):
		self.assertRaises(TypeError, Company, None, self.valid_category, self.valid_link,self.valid_link)
		self.assertRaises(TypeError, Company, "Netflix", 2, self.valid_link, self.valid_link)
		self.assertRaises(TypeError, Company, "Home Depot", self.valid_category, [], self.valid_link)
		self.assertRaises(TypeError, Company, "Netflix", self.valid_category, self.valid_link, None)
		self.assertRaises(TypeError, Company, "Netflix", self.valid_category, self.valid_link, self.valid_link,
						 description=333)

	def test_values(self):
		#name test
		#it's kind of hard to determine what's a valid company name
		self.assertRaises(ValueError, Company, "", self.valid_category, self.valid_link, self.valid_link)
		#category test
		self.assertRaises(ValueError, Company, "Netfix", "", self.valid_link, self.valid_link)
		self.assertRaises(ValueError, Company, "Netfix", "invalid", self.valid_link, self.valid_link)
		self.assertRaises(ValueError, Company, "Netfix", "softwre", self.valid_link, self.valid_link)
		self.assertRaises(ValueError, Company, "Netfix", "111", self.valid_link, self.valid_link)
		#logo_img test
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, "htp/broken_link", self.valid_link)
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, "http://", self.valid_link)
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, "htp/www.broken.com", self.valid_link)
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, "broken.com", self.valid_link)
		#banner_img test
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link, banner_img="brkn")
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link, banner_img="http://www.")
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link, banner_img="http://")
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link, banner_img="broken.com")
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link, banner_img="http://invalid")

	def test_attributes(self):
		self.assertIsNone(self.company1.culture_rat)
		self.assertIsNone(self.company1.work_rat)
		self.assertIsNone(self.company1.company_rat)
		self.assertEqual(self.company1.num_company_reviews,0)
		self.assertEqual(self.company1.num_work_reviews,0)
		self.assertEqual(self.company1.num_culture_reviews ,0)

if __name__ == "__main__":
	unittest.main(failFast=True)