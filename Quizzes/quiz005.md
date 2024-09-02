# Quiz 005

## Code

```.py
import random
password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for x in range(0,9):
    for y in range(0,20):
        number = random.randint(0,61)
        password = password + characters[number]
    print(password)
    password = ""
```
## Proof of Work

![image](https://github.com/user-attachments/assets/16a951aa-3dbd-4a94-b820-4e9f50180951)
