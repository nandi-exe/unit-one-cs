# Quiz 016
## Paper Solution

<img width="496" alt="image" src="https://github.com/user-attachments/assets/218a6c84-431b-41b1-a161-43a059ef0bd4">

## Flowchart

![quiz016 drawio](https://github.com/user-attachments/assets/a25f603d-51a0-46ac-a9bf-fd0f83bce5aa)

## Code

```

def get_letter(msg:str):
    new_string = ""
    switch = ["4","3","1","0","_"]
    string_len = len(msg)
    for i in range (0,string_len):
        if msg[i:i+1:1] in "Aa":
            new_string = new_string + switch[0]
        elif msg[i:i+1:1] in "Ee":
            new_string = new_string + switch[1]
        elif msg[i:i+1:1] in "Ii":
            new_string = new_string + switch[2]
        elif msg[i:i+1:1] in "Oo":
            new_string = new_string + switch[3]
        elif msg[i:i+1:1] in " ":
            new_string = new_string + switch[4]
        else:
            new_string = new_string + msg[i:i+1:1]

    return new_string

```
## Proof of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/7ce6a6b0-46a8-40a9-8cb9-04a9c6b10586">
