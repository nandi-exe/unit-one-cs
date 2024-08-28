# Quiz 004

## Paper Solution

<img width="888" alt="image" src="https://github.com/user-attachments/assets/b6639226-9b65-4c40-8123-0fff68547e15">

## Code

```.py
perfectcheck = False
sum = 0
num= int(input("Please enter a number: "))
for x in range(1,num-1):
    if num % x == 0:
        print(x)
        sum = sum + x
if sum == num:
    prefectcheck = True
if perfectcheck:
    print("Your number ", num, "is perfect")
else:
    print("Your number ", num, "is not perfect")
```
## Proof of Work
![image](https://github.com/user-attachments/assets/39f8308f-405d-4055-9369-21ee716e9c52)
