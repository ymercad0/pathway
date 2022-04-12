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

		self.review1 = Review(self.comp1, "Title", 'Software Engineering',
		                 "Position", company_rating=4, education="M.S.", interview_desc="Interview",
						 interview_rat=4, offer=True, accepted=True, start_date="05-23-2022",
						 intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")


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

	def test_score_params(self):
		'Type Errors'
		self.assertRaises(TypeError, self.review1.update_scores, {})
		self.assertRaises(TypeError, self.review1.update_scores, None)
		self.assertRaises(TypeError, self.review1.update_scores, [10.32, 15, 20])
		self.assertRaises(TypeError, self.review1.update_scores, [10, "15", 20])
		'Value Errors'
		self.assertRaises(ValueError, self.review1.update_scores, [])
		self.assertRaises(ValueError, self.review1.update_scores, [32, 10])
		self.assertRaises(ValueError, self.review1.update_scores, [10, 15, -20])

	def test_score_equality(self):
		#the first time a score is entered
		self.review1.update_scores([None, None, None])
		self.assertAlmostEqual(self.comp1.company_rat, 4, places=1)
		#work is now being rated
		self.review1.work_rating = 2
		self.review1.update_scores([1, None, None])
		self.assertAlmostEqual(self.comp1.company_rat, 4, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2, places=1)
		# drop down the scores
		self.review1.company_rating = 3
		self.review1.work_rating = 4
		self.review1.update_scores([1, 1, None])
		self.assertAlmostEqual(self.comp1.company_rat, 3.5, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 3, places=1)
		# introduce the final score category
		self.review1.company_rating = 1
		self.review1.work_rating = 1
		self.review1.culture_rating = 5
		self.review1.update_scores([2, 2, None])
		self.assertAlmostEqual(self.comp1.company_rat, 2.7, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2.3, places=1)
		self.assertAlmostEqual(self.comp1.culture_rat, 5, places=1)
		# updating all categories once more to make sure
		# the previous averages round up as they should
		self.review1.company_rating = 5
		self.review1.work_rating = 3
		self.review1.culture_rating = 3
		self.review1.update_scores([3, 3, 1])
		# updating culture with only one of two values
		self.review1.company_rating = 3
		self.review1.work_rating = None
		self.review1.culture_rating = 4
		self.review1.update_scores([4, 4, 2])
		self.assertAlmostEqual(self.comp1.company_rat, 3.2, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2.5, places=1)
		self.assertAlmostEqual(self.comp1.culture_rat, 4, places=1)

if __name__ == "__main__":
	unittest.main(failFast=True)