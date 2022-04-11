from model import Company, Review
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
		self.assertRaises(ValueError, Company, "Netflix", "software", self.valid_link, "desc", "link")

class TestReviews(unittest.TestCase):
	def setUp(self):
		self.comp1 = Company("Amazon", "Software", "http://somelink.com")
		self.comp2 = Company("McDonald's", "Restaurant", "http://somelink.com")

	def test_init_required(self):
		'Type Errors'
		self.assertRaises(TypeError, Review, 'Boeing', "Title", 'Software Engineering',
		                 "Position",  4, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, {"Title"}, 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, "Title",
						'Software Engineering', None, 4, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, "Title", ['Software Engineering'],
						"Position", 4, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
						["Position"], 4, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
						"Position", hex(4), "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
						"Position", 3.90, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
						"Position", 0.30, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp2, "Title", 'Software Engineering',
						"Position", 4, ord("M"), "Interview", 4)

		self.assertRaises(TypeError, Review, self.comp2, "Title", 'Software Engineering',
						"Position", 4, "M.S.", ["Review"], 4)

		self.assertRaises(TypeError, Review, self.comp2, "Title", 'Software Engineering',
						"Position", 4, "M.S.", "Review", hex(4))

		self.assertRaises(TypeError, Review, self.comp2, "Title", 'Software Engineering',
						 "Position", 4, "M.S.", "Review", 4.90)

		self.assertRaises(TypeError, Review, self.comp2, "Title", 'Software Engineering',
						 "Position", 4, "M.S.", "Review", 3.50)

		self.assertRaises(TypeError, Review, self.comp2, "Title", 'Software Engineering',
					    "Position", 4, "M.S.", "Review", float(2))
		'Value Errors'
		self.assertRaises(ValueError, Review, self.comp1, "", 'Software Engineering',
		                 "Position", 4, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp1, "Title", 'Software Engineering',
		                  "", 4, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp1, "Title", 'SWE', "Position", 4, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp1, "Title", '', "Position", 4, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp1, "Title", 'Software Engineering',
		                  "Position", 10, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp1, "Title", 'Software Engineering',
						  "Position", -1, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp2, "Title",  'Software Engineering',
		                "Position",  4, "A degree", "Review", 4)

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
						"Position", 4, "M.S.", "", 4)

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                  "Position", 4, "M.S.", "Review", -3)

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                  "Position", 4, "M.S.", "Review", 6)

	def test_init_optional(self):
		'Type Errors'
		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=0, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=None,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date=["05", "23", "2022"], intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc=None, work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat="10",
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=hex(20), location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=["San Francisco", "California"],
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay="23.64", bonuses="Bonus")

		self.assertRaises(TypeError, Review, self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses=32.40)

		'Value Errors'
		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="23-05-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="2022-05-23", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=-4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=10,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=-4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "Some State"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=-35.25, bonuses="Bonus")

	def test_score_values(self):
		pass

if __name__ == "__main__":
	#failFast set to false in order to see all failing tests in one run
	unittest.main(failFast=False)