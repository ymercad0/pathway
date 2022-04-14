from model import Company, Review, User
import unittest

class TestReviews(unittest.TestCase):
	def setUp(self):
		self.comp1 = Company("Amazon", "Software", "http://somelink.com")
		self.comp2 = Company("McDonald's", "Restaurant", "http://somelink.com")
		self.user = User("Test", "somemail@gmail.com", "123323456")

		self.review1 = Review('User', self.comp1, "Title", 'Software Engineering',
		                 "Position", company_rating=4, education="M.S.", interview_desc="Interview",
						 interview_rat=4, offer=True, accepted=True, start_date="05-23-2022",
						 intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")


	def test_init_required(self):
		'Type Errors'
		#invalid user
		self.assertRaises(TypeError, Review, self.user, self.comp1, "Title", 'Software Engineering',
		                 "Position",  4, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, ["User"], self.comp1, "Title", 'Software Engineering',
		                 "Position",  4, "M.S.", "Interview", 4)

		# not a company object
		self.assertRaises(TypeError, Review, 'User', 'Boeing', "Title", 'Software Engineering',
		                 "Position",  4, "M.S.", "Interview", 4)

		# title is of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp1, {"Title"}, 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4)

		# Position is None
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title",
						'Software Engineering', None, 4, "M.S.", "Interview", 4)

		# job is of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", ['Software Engineering'],
						"Position", 4, "M.S.", "Interview", 4)

		# position is of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
						["Position"], 4, "M.S.", "Interview", 4)

		# score is of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
						"Position", hex(4), "M.S.", "Interview", 4)

		# score cant be a float
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
						"Position", 3.90, "M.S.", "Interview", 4)

		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
						"Position", 0.30, "M.S.", "Interview", 4)

		# education is of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
						"Position", 4, ord("M"), "Interview", 4)

		# description is of the wrong time
		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
						"Position", 4, "M.S.", ["Review"], 4)

		# score is of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
						"Position", 4, "M.S.", "Review", hex(4))

		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
						 "Position", 4, "M.S.", "Review", 4.90)

		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
						 "Position", 4, "M.S.", "Review", 3.50)

		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
					    "Position", 4, "M.S.", "Review", float(2))
		'Value Errors'
		# user is empty or not the right length
		self.assertRaises(ValueError, Review, "", self.comp1, "Title", 'Software Engineering',
		                 "Position",  4, "M.S.", "Interview", 4)

		self.assertRaises(ValueError, Review, "chr", self.comp1, "Title", 'Software Engineering',
		                 "Position",  4, "M.S.", "Interview", 4)

		# title is empty
		self.assertRaises(ValueError, Review, 'User', self.comp1, "", 'Software Engineering',
		                 "Position", 4, "M.S.", "Review", 4)

		# position is empty
		self.assertRaises(ValueError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                  "", 4, "M.S.", "Review", 4)
		# SWE is not a job category
		self.assertRaises(ValueError, Review, 'User', self.comp1, "Title", 'SWE', "Position", 4, "M.S.", "Review", 4)

		# category is empty
		self.assertRaises(ValueError, Review, 'User', self.comp1, "Title", '', "Position", 4, "M.S.", "Review", 4)

		# rating more or less than the max or min allowed
		self.assertRaises(ValueError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                  "Position", 10, "M.S.", "Review", 4)

		self.assertRaises(ValueError, Review, 'User', self.comp1, "Title", 'Software Engineering',
						  "Position", -1, "M.S.", "Review", 4)

		# invalid education
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "", "Review", 4)

		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title",  'Software Engineering',
		                "Position",  4, "A degree", "Review", 4)

		# invalid description
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
						"Position", 4, "M.S.", "", 4)

		# rating is invalid
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                  "Position", 4, "M.S.", "Review", -3)

		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                  "Position", 4, "M.S.", "Review", 6)

	def test_init_optional(self):
		'Type Errors'
		# offer not a bool
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=0, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# accepted not a bool
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=None,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# start date of the wrong type
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date=["05", "23", "2022"], intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# intern desc is None
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc=None, work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# work rating of invalid type
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat="10",
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# culture rating of invalid type
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=hex(20), location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# location not a tuple
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=["San Francisco", "California"],
						 pay=35.25, bonuses="Bonus")

		# pay is a string
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay="23.64", bonuses="Bonus")

		# bonuses is an int
		self.assertRaises(TypeError, Review, 'User', self.comp1, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses=32.40)


		# state or city are of invalid types
		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", 333),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=(33, "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(TypeError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=(33, True),
						 pay=35.25, bonuses="Bonus")

		'Value Errors'
		# invalid date format
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="23-05-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="2022-05-23", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# accepted an offer that wasn't given (offer = False)
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=False, accepted=True,
						 start_date="05-22-2023", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# invalid artings
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=-4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=10,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=-4, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")

		# invalid state
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "Some State"),
						 pay=35.25, bonuses="Bonus")

		# invalid pay
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("San Francisco", "California"),
						 pay=-35.25, bonuses="Bonus")

		# invalid city (not alphabetical)
		self.assertRaises(ValueError, Review, 'User', self.comp2, "Title", 'Software Engineering',
		                 "Position", 4, "M.S.", "Interview", 4, offer=True, accepted=True,
						 start_date="05-23-2022", intern_desc="desc", work_rat=4,
						 culture_rat=4, location=("Some c1t5", "California"),
						 pay=35.25, bonuses="Bonus")

	def test_score_equality(self):
		#the first time a score is entered
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 4, places=1)
		self.assertEqual(self.comp1.total_reviews, 1)
		#work is now being rated
		self.review1.company_rating = 4
		self.review1.work_rating = 2
		self.review1.culture_rating = None
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 4, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2, places=1)
		self.assertEqual(self.comp1.total_reviews, 2)
		# drop down the scores
		self.review1.company_rating = 3
		self.review1.work_rating = 4
		self.review1.culture_rating = None
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 3.7, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 3, places=1)
		self.assertEqual(self.comp1.total_reviews, 3)
		# introduce the final score category
		self.review1.company_rating = 1
		self.review1.work_rating = 1
		self.review1.culture_rating = 5
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 3, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2.3, places=1)
		self.assertAlmostEqual(self.comp1.culture_rat, 5, places=1)
		self.assertEqual(self.comp1.total_reviews, 4)
		# updating all categories once more to make sure
		# the previous averages round up as they should
		self.review1.company_rating = 5
		self.review1.work_rating = 3
		self.review1.culture_rating = 3
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 3.4, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2.5, places=1)
		self.assertAlmostEqual(self.comp1.culture_rat, 4, places=1)
		self.assertEqual(self.comp1.total_reviews, 5)
		# updating culture with only one of two values
		self.review1.company_rating = 3
		self.review1.work_rating = None
		self.review1.culture_rating = None
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 3.3, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2.5, places=1)
		self.assertAlmostEqual(self.comp1.culture_rat, 4, places=1)
		self.assertEqual(self.comp1.total_reviews, 6)
		# one None
		self.review1.company_rating = 4
		self.review1.work_rating = None
		self.review1.culture_rating = 3
		self.review1.update_scores()
		self.assertAlmostEqual(self.comp1.company_rat, 3.4, places=1)
		self.assertAlmostEqual(self.comp1.work_rat, 2.5, places=1)
		self.assertAlmostEqual(self.comp1.culture_rat, 3.7, places=1)
		self.assertEqual(self.comp1.total_reviews, 7)

if __name__ == "__main__":
	unittest.main(failFast=True)