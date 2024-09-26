# Imported Functions & Procedures
import os.path
from function_library import encrypt_password
from function_library import student_generate_email
from function_library import staff_generate_email
end_code = "\033[00m"
cyan = "\33[0;36m"
yellow = "\33[0;33m"

secret_password = "happyplaces2024"
terminator = False
while not terminator :
    menu_select = input(f'{cyan}Welcome to your address book! Would you like to:\n{end_code}a. Add new email(s), \nb. Delete email(s), \nc. View a contact list\nType in A, B, or C.{cyan}\nIf none of these apply, press x to terminate the program: \n{end_code}')
    if menu_select in "Aa":
        #Opens the create email sector
        choice = input(f'{cyan}Would you like to:{end_code}\na. Generate new year group emails\nb. Create new staff emails\nc.Add individual student emails to pre-existing files\n')
        if choice in "Aa":
            #Create new student email file
            year_group = int(input(f"{cyan}Enter the incoming students' year group: {end_code}"))
            join_year = int(input(f"{cyan}Enter the year of joining: {end_code}"))

            with open(f'{year_group}_{join_year}.csv', 'w') as f:
                f.writelines([])
            limit = int(input(f"{cyan}How many new students are joining?: {end_code}"))
            for x in range(0, limit):
                fname = input(f"{cyan}First Name: ")
                lname = input(f"{cyan}Last Name: ")
                email = student_generate_email(fname, lname, join_year)
                print(fname, lname, email)
                with open(f'{year_group}_{join_year}.csv', 'a') as f:
                    f.writelines(f'\n{fname}, {lname}, {email}')
        elif choice in "Bb":
            #Create new teacher emails
            new_staff = int(input(f"{cyan}Enter the total members of staff joining: {end_code}"))
            for count in range(0, new_staff):
                fname = input(f"{cyan}First Name: {end_code}")
                lname = input(f"{cyan}Last Name: {end_code}")
                email = staff_generate_email(fname, lname)
                dept = input(f"{cyan}Enter the letter corresponding to the department the staff is joining {end_code}\na. Teaching \nb. Pastoral \nc.Administration\n")
                if dept in "Aa":
                    #Teaching Department
                    with open(f'teaching.csv', 'a') as f:
                        f.writelines(f'\n{fname}, {lname}, {email}')
                elif dept in "Bb":
                    #Pastoral Department
                    with open(f'pastoral.csv', 'a') as f:
                        f.writelines(f'\n{fname}, {lname}, {email}')
                elif dept in "Cc":
                    #Administration
                    with open(f'admin.csv', 'a') as f:
                        f.writelines(f'\n{fname}, {lname}, {email}')
                else:
                    #Invalid Input
                    print("Invalid input")
                    break
        elif choice in "Cc":
            # Append existing student file
            year_group = int(input(f"{cyan}Enter the incoming students' year group: {end_code}"))
            join_year = int(input(f"{cyan}Enter the year of joining: {end_code}"))
            if os.path.exists(f'{year_group}_{join_year}.csv'):
                limit = int(input(f"{cyan}How many new students are joining?: {end_code}"))
                for x in range(0, limit):
                    fname = input(f"{cyan}First Name: ")
                    lname = input(f"{cyan}Last Name: ")
                    email = student_generate_email(fname, lname, join_year)
                    with open(f'{year_group}_{join_year}.csv', 'a') as f:
                        f.writelines(f'\n{fname}, {lname}, {email}')
            else:
                print(f"{cyan}File does not exist{end_code}")

    elif menu_select in "Bb":
        #Deleting Emails
        type = input(f'{cyan}Is the contact list for: \na. Students \nb. Staff\n{end_code}')
        if type in "Aa":
            #Delete Student Emails
            year_group = int(input(f'{cyan}Enter the year group:{end_code}'))
            join_year = int(input(f'{cyan}Enter the year of joining: {end_code}'))
            if os.path.exists(f'{year_group}_{join_year}.csv'):
                with open(f'{year_group}_{join_year}.csv','r') as f:
                    data = f.readlines()
                    for i, item in enumerate(data):
                        clean_item = item.strip()
                        fname, lname, email = clean_item.split(',')
                        print(f"{i + 1}:{fname} {lname}: {email}")
                    delete = int(input(f'{cyan}Enter the contact you would like to delete: {end_code}'))
                    new_data = []
                    if delete <= len(data):
                        for i, item in enumerate(data):
                            if i + 1 != delete:
                                new_data.append(item)
                        print(data, new_data)
                    else:
                        exit('Number is incorrect')
        elif type in "Bb":
            #Deleting Staff Emails
            correct_input = False
            dept = input(f"{cyan}Enter the department name in full: \na. Teaching \nb. Pastoral \nc.Admin{end_code}\n")
            dept = dept.lower()
            if os.path.exists(f'{dept}.csv'):
                correct_input = True
                with open(f'{dept}.csv', 'r') as f:
                    data = f.readlines()
                    for i, item in enumerate(data):
                        clean_item = item.strip()
                        fname, lname, email = clean_item.split(',')
                        print(f"{i + 1}:{fname} {lname}: {email}")
                    delete = int(input(f'{cyan}Enter the contact you would like to delete: {end_code}'))
                    new_data = []
                    if delete <= len(data):
                        for i, item in enumerate(data):
                            if i + 1 != delete:
                                new_data.append(item)
                        print(data, new_data)
                    else:
                        exit('Number is incorrect')
            else:
                print(f'{cyan} This file does not exist{end_code}')

    elif menu_select in "Cc":
        #View Contact Lists
        type = input(f'{cyan}Is the contact list for: \na. Students \nb. Staff\n{end_code}')
        if type in "Aa":
            #View Student Contacts
            year_group = int(input(f'{cyan}Enter the year group: {end_code}'))
            join_year = int(input(f'{cyan}Enter the year of joining: {end_code}'))
            if os.path.exists(f'{year_group}_{join_year}.csv'):
                with open(f'{year_group}_{join_year}.csv', 'r') as f:
                    data = f.readlines()
                    for i, item in enumerate(data):
                        clean_item = item.strip()
                        fname, lname, email = clean_item.split(',')
                        print(f'{i + 1}:{fname} {lname}: {email}')

            else:
                print(f'{cyan}File Unavailable{end_code}')
        elif type in "Bb":
            #View Staff Contacts
            dept = input(f'{cyan}Enter the department: {end_code}')
            if os.path.exists(f'{dept}.csv'):
                with open(f'{dept}.csv', 'r') as f:
                    data = f.readlines()
                    print(f'{dept.title()} Department')
                    for i, item in enumerate(data):
                        clean_item = item.strip()
                        fname, lname, email = clean_item.split(',')
                        print(f'{i + 1}:{fname} {lname}: {email}')
            else:
                #Unavailable
                print(f'{cyan}File Unavailable{end_code}')
    elif menu_select == secret_password:
        #Opens Password Function
        close = False
        while not close:
            #Keeps the Password Manager Looping
            choice = input(f'{yellow}Password Manager: \n Would you like to:\n a. Add a password \nb. Delete an existing password\nc. View a password\nd. Exit Password Manager\n{end_code}')
            if choice in "Aa":
                #Password Addition
                domain = input(f'{yellow}Enter the site domain: {end_code}')
                password = input(f'{yellow}Enter the password to be added: {end_code}')
                with open(f'password_bank.csv', 'a') as f:
                    f.writelines(f'{domain}, {encrypt_password(password)}')
            elif choice in "Bb":
                #Password Deletion
                with open(f'password_bank.csv', 'r') as f:
                    data = f.readlines()
                for i, item in enumerate(data):
                    clean_item = item.strip()
                    domain, password = clean_item.split(',')
                    print(f"{i + 1}:{domain}")
                delete = int(input(f'{yellow}Enter the index password you would like to delete: {end_code}'))
                new_data = []
                pass_check = input(f'{yellow}Enter the master password to delete this passsword: \n{end_code}')
                if pass_check == secret_password:
                    if delete <= len(data):
                        for i, item in enumerate(data):
                            if i + 1 != delete:
                                new_data.append(item)
                        print(data, new_data)
                        with open(f'password_bank.csv', 'w') as f:
                            f.writelines(new_data)
                        print(f'{cyan} Procedure Complete! {end_code}')
                    else:
                        print('Number is incorrect')
                else:
                    print("Incorrect password")
            elif choice in "Cc":
             #View All Passwords
             with open(f'password_bank.csv', 'r') as f:
                 data = f.readlines()
             for i, item in enumerate(data):
                 clean_item = item.strip()
                 domain, password = clean_item.split(',')
                 print(f"{i + 1}:{domain}")
             view_passcode = int(input(f'{yellow}Enter the index of the password you would like to view: {end_code}'))
             new_data = []
             pass_check = input(f'{yellow}Enter the master password to delete this password: \n{end_code}')
             if pass_check == secret_password:
                 for i, item in enumerate(data):
                     if i+1 == view_passcode:
                         clean_item = item.strip()
                         domain, password = clean_item.split(',')
                         print(f"{i + 1}:{domain}: {encrypt_password(password)}")
                     else:
                        print(f'{yellow}Index entered is incorrect{end_code}')
             else:
                 print("Incorrect password")
            elif choice in "Dd":
                #Exit Password Manager
                close = True
            else:
                #Invalid Input
                print("Invalid input")
    elif menu_select == "X" or menu_select == "x":
        terminator = True
        print(f'{cyan}Thank you for using our application!{end_code}')
    else:
        #Overall Invalid Input
        print(f'{cyan}Please enter a valid option. In this case, A, B, or C{end_code}')


#The print blahs are temporary fillers. I'll work on building functions for them in a bit