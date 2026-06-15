## 1 The Problem
```text
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.
```

## 2 Function Signature
```python
import datetime, dateutil
def age_verification(dob):
    # D.O.B => 16, access granted
    # D.O.B < 16, tell them thier age, access denied
	#parameters
	# - D.O.B, string. dashes between date month and year.
	# returns
	# - string, access granted or denied.
	#side effects
	# - none
	Pass

```

## Examples
```python
"""
Given that I have a person with a birthday, person will have their age displayed
"""
def test_date_of_birth_is_date_type():
	assert date_of_birth == 2010-05-15

"""
Given that I have a date of birth that makes me below the age of 16, it will tell me the age and the age requirement, and deny me access
"""
def test_underaged_denied_access():
	assert result == "You are 12, you have to be 16, access denied!"

"""
Given that I have a date of birth that makes me 16 or above, it will grant me access
"""
def test_16_or_over_acess_granted():
	assert result == "Access Granted!"

```