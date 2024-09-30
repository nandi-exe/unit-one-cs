# Quiz 014

## Paper Solution

![image](https://github.com/user-attachments/assets/0fff008b-b4fa-4ba8-b55c-12d1b8e688aa)

## Flowchart

![image](https://github.com/user-attachments/assets/7439cb91-6ce0-4dfd-bdf2-b2dab6a625c3)


## Code
```
def open_doors(num_students):
    open_doors = 0
    door_status = []

    num_doors = num_students
    for count in range(num_doors):
        door_status.append(1)
        open_doors = open_doors + 1

    jump = 2
    while jump <= num_students:
        for count in range(1, num_doors, jump):
            if door_status[count] == 1:
                door_status[count] = 0
                open_doors = open_doors - 1
            else:
                door_status[count] = 1
                open_doors = open_doors + 1

        jump += 1

    return open_doors

```
## Proof of Work

<img width="610" alt="image" src="https://github.com/user-attachments/assets/cf92db8d-81db-4f11-8927-d1a20c49e1a4">




