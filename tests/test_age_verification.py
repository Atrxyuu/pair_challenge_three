from datetime import date 
from lib.age_verification import *

def test_date_of_birth_is_date_type():
	date_of_birth = age_verification("2010-05-15")
	assert isinstance(date_of_birth, date)
# This test will no longer work