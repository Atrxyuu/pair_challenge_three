from datetime import datetime 

def age_verification(dob):
    d_o_b = dob
    date_of_birth = datetime.strptime(d_o_b, "%Y-%m-%d").date()
    
