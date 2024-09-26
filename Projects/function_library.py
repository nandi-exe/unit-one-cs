
#Email Generation (student and staff)
def student_generate_email(fname:str,lname:str,gradyear:int):
    new_email = fname + lname + str(gradyear) + "@happyschool.org"
    return new_email
def staff_generate_email(fname:str, lname:str):
    new_email = fname +lname + "@happyschool.org"
    return new_email

#Encrypting the Passwords
def encrypt_password(password:str):
    new_code = password[::-1]
    return new_code

