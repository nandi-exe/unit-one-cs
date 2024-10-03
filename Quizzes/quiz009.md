# Quiz 009

## Paper Solution

<img width="497" alt="image" src="https://github.com/user-attachments/assets/86f8bce4-75da-4c61-b50e-f5e9266d1458">

## Flowchart

## Code

```
def shift13(statement:str,shift:int):
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_string = " "
    up_or_down = True
    limit = len(statement)
    for a in range(0,limit):
        letter_found = False
        passed = False
        char = statement[a:a + 1:1]
        for b in range(0,25):
            if char == upper_letters[b]:
                index = b
                up_or_down = True
                letter_found = True
                break
            elif char == lower_letters[b]:
                index = b
                up_or_down = False
                letter_found = True
                break
            elif char == " ":
                passed = True
                break
        if letter_found or passed:
            if passed:
                new_string += " "
            elif letter_found:
                shift_index = index + shift
                if shift_index > 26:
                    shift_index = shift_index % 26
                if up_or_down:
                    new_string += upper_letters[shift_index]
                elif not up_or_down:
                    new_string += lower_letters[shift_index]
        else:
            print("Task Unsuccessful")
    return new_string
```

## Proof of Work

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/97697b96-793f-46b8-b116-47d88cc1625e">

