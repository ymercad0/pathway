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
		self.assertRaises(TypeError, self.company1.category_badge, "None")
		self.assertRaises(TypeError, self.company1.category_badge, 3+4j)


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
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link,
		 				  banner_img="http://www.")

		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link, banner_img="http://")
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link,
		                  banner_img="broken.com")
		self.assertRaises(ValueError, Company, "Netflix", self.valid_category, self.valid_link,
		                  banner_img="http://invalid")

		self.assertRaises(ValueError, self.company1.category_badge, -5)
		self.assertRaises(ValueError, self.company1.category_badge, 5.1)


	def test_equality(self):
		# default status color
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "secondary")
		# perfect score
		self.company1.company_rat = 5
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "success")
		# should be green
		self.company1.company_rat = 4.99
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "success")
		# just at the edge of 4
		self.company1.company_rat = 3.9
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "warning text-dark")
		# at the edge of 3
		self.company1.company_rat = 2.99
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "danger")
		# exact value
		self.company1.company_rat = 2
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "danger")
		# any score less than 2
		self.company1.company_rat = 1.99
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "dark")
		# score of 0
		self.company1.company_rat = 0
		self.assertEqual(self.company1.category_badge(self.company1.company_rat), "dark")

if __name__ == "__main__":
	unittest.main(failFast=True)