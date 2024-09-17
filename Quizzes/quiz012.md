# Quiz 012

## Paper Solution

<img width="854" alt="Screenshot 2024-09-18 at 0 31 52" src="https://github.com/user-attachments/assets/d5a9b2de-895f-4a80-91bd-8077f8194601">

## Code
```
def mystery(num1:int,num2:int):
    answer = 0
    step_1 = num1*num2
    step_2 = num1-num2
    if step_2 > 0:
        answer = step_1+step_2
    else:
        answer = step_1-step_2
    return answer

digit1 = int(input("Please enter the first number"))
digit2 = int(input("Please enter the second number"))

final_response = mystery(digit1,digit2)
print(final_response)
```
## Flowchart

<img width="541" alt="Screenshot 2024-09-18 at 0 53 52" src="https://github.com/user-attachments/assets/0ce18359-cb8e-4a44-9df5-05c09966f129">


## Proof of Work

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/68e9e0a9-7584-4098-b94e-acc6822f936a">


