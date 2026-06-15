from datetime import date 
from lib.age_verification import *

def test_date_of_birth_is_date_type():
	date_of_birth = age_verification("2010-05-15")
	assert isinstance(date_of_birth, date)
# This test will no longer work

def test_underaged_denied_access():
	date_of_birth = age_verification("2010-05-15")
	result = date_of_birth
	assert result == "You are 12, you have to be 16, access denied!"

def test_16_or_over_acess_granted():
	assert result == "Access Granted!"