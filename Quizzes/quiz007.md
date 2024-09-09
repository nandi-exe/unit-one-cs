# Quiz 007

## Code 
```
from my_lib import validate_int

def binary_converter() ->str:
    n = validate_int("Please enter a number")
    remainder = ""
    while n!= 0:
        remainder =remainder + str(n%2)
        n = n//2

    for count in remainder:
        binary_int = remainder[::-1]

    return binary_int

number = binary_converter()
print(number)
```

## Proof Of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/15a7928a-e5f5-4ce1-b5e1-98c90af379b1">


