# Project Unit 1

## Criterion A: Planning
### Problem Definition

My client is a well-known philanthropist. After learning at an international high school, they have been working on opening a similar campus in their home country. They want to be able to standardise communication between students and teachers, and also have a way to have a record of said communication methods that keeps track of when students graduate or teachers leave, so tat they can be made null and void. Due to their old age, they also struggle with recalling all of their passwords, and arent sure of how they can prevent losing them or forgeting them, as their online ccounts are in dire need of the security, and hold lots of sensitive information, and would try to avoid it being leaked at all costs. 

### Solution

I will create an address book, containing an standard email address generator for the school, that follows a specific format. On top of that, the address book will also store all valid and in-use school emails, adding new addresses and deleting redundant ones between school years. As for their password dilemma, I will embed a password manager into the program, to be triggered once a special code is input. This input would allow the password manager to be accessed by the user, allowing for the philanthropist to have a space close-by that they can easily access all their passwords while only neding to remember one.

### Why Python?

I have decided to utilise Python for the development of this project. It's vast libraries and versatility allow for rapid-fire developing. This will ensure I get the pro

### Success Criteria
Main Program

1. Must allow the input and storage of the names of all incoming students and staff, as well as their year of joining(students only).
2. Generate emails for these students, and add them to a file containing all students for that year.
3. Must delete all redundant addresses, or a specific email addresses when prompted by the user.
4. Must allow user's to open and view the contents of all available files, notifying them when an existing file is non-existent.
   
Hidden Functionality:
1. If the user enters the secret code ("happyplaces2024"), the program will change modes and act as a password manager.
2. In password manager mode, the user should be able to:
  * Add a password (for example, for a website).
  * View the stored passwords (only if they re-enter the secret code).
  * Remove any redundant passwords at the user's prompting
3. Basic Security Features - Implementing a basic obfuscation technique or basic encryption (e.g., reversing the password string or shifting characters by a fixed number) 
4. Store the in their encrypted form, using a .csv file.

## Criterion B: Design

### Flow Diagrams for Algorithms

![codetoflow (1)](https://github.com/user-attachments/assets/9b454c0f-8d19-4ca5-97f9-821df48980b3)
![codetoflow (3)](https://github.com/user-attachments/assets/635d68d2-83a9-4bd5-a746-b52b0e46ed15)
![codetoflow (4)](https://github.com/user-attachments/assets/879825e0-6c94-41a8-9ebc-66218f08e0f3)


### Data Storage

All the data in my program with be stored using .csv files, that are generated and appended by user input. These files are meant to be saved in the same folder as the main program in order for it to maintain functionality.

### System Diagram

![image](https://github.com/user-attachments/assets/7d798f9a-f1b9-4272-998e-19eed510bde8)


### Record of Tasks

| Task Number | Planned Action                     | Planned Outcome                                                                                                    |   | Time estimated | Target Completion Date |   |
|-------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------|---|----------------|------------------------|---|
| 1           | First Meeting with the client      | Obtained a problem definition                                                                                      |   | 10 min         | 7 Sept 2024            |   |
| 2           | Working on program plan and design | Have a defined structure                                                                                           |   | 25 min         | 9 Sept 2024            |   |
| 3           | 2nd meeting with client            | Present a potential solution to client; Check to see if they are satifsied with said solution                      |   | 15 min         | 12 Sept 2024           |   |
| 4           | Development Phase 1: Prototyping   | Code a working prototype of of the address book/password manager                                                   |   | 6-12 hours     | 16 Sept 2024           |   |
| 5           | Testing Phase 1: Internal          | Perform alpha testing and black-box testing on the prototype; Not any edits and changes to be made where necessary |   | 4-5 hours      | 18 Sept 2024           |   |
| 6           | Testing Phase 2: Peer Review       | Invite fellow developers to test out the prototype; Make note of all errors and correct accordingly                |   | 4-5 hours      | 20 Sept 2024           |   |
|  7          | Development Phase 2: Final Draft   | Correct any and all errors found during testing; Produce a final version of the program                            |   | 4-10 hours     | 22 Sept 2024           |   |
|  8          |  Client Presentation and Handover  | Final Product is handed over to client for final examination; Client testing                                       |   | 10 min        |                        |   |
|             |                                    |                                                                                                                    |   |                |                        |   |


## Test Data


| Test | Success Criteria                                                                                                                                                           | Result     |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| 1.   | 1. Must allow the input and storage of the names of all incoming students, as well as their year of joining.                                                               | Successful |
| 2.   | 2. Generate emails for these students, and add them to a file containing all students for that year.                                                                       | Successful |
| 3.   | 3. Must delete all redundant addresses, or a specific email addresses when prompted by the user.                                                                           | Successful |
| 4.   | 4. Must allow user's to open and view the contents of all available files, notifying them when an existing file is non-existent.                                           | Successful |
|      | Hidden Functionality:                                                                                                                                                      |            |
| 5.   | 1. If the user enters the secret code ("happyplaces2024"), the program will change modes and act as a password manager.                                                    | Successful |
| 6.   | 2. In password manager mode, the user should be able to:                                                                                                                   | Successful |
| 7.   | * Add a password (for example, for a website).                                                                                                                             | Successful |
| 8.   | * View the stored passwords (only if they re-enter the secret code).                                                                                                       | Successful |
| 9.   | * Remove any redundant passwords at the user's prompting                                                                                                                   | Successful |
| 10.  | 3. Basic Security Features - Implementing a basic obfuscation technique or basic encryption (e.g., reversing the password string or shifting characters by a fixed number) | Successful |
| 11.  | 4. Store the in their encrypted form, using a .csv file.                                                                                                                   | Successful |

### Proof of Funtionality Video

[Video uploaded separately within folder]













