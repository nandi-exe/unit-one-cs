# Quiz 014

## Paper Solution

![image](https://github.com/user-attachments/assets/0fff008b-b4fa-4ba8-b55c-12d1b8e688aa)

## Code
```
def open_doors(num_students):
    open_doors = 0
    door_status = []
 
    num_doors = num_students
    for count in range(num_doors):
        door_status.append(1)

    jump = 2
    while jump <= num_students:
        for count in range(jump - 1, num_doors, jump):  
            if door_status[count] == 1:  
                door_status[count] = 0
                open_doors += 1
            else:  
                door_status[count] = 1
                open_doors -= 1

        jump += 1

    return open_doors

```
## Proof of Work

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/301a8548-feb6-435f-97b4-30675bdec776">


