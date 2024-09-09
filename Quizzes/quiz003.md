# Quiz 003

## Code

```
dna_chain = input("Please enter the DNA string :")
new_string = ""
if len(dna_chain) == 0:
    print("Please enter your DNA string")
elif len(dna_chain) == 1:
    if dna_chain == "A" or "a":
        print("T")
    elif dna_chain == "G" or "g":
        print("C")
    elif dna_chain == "T" or "t":
        print("A")
    elif dna_chain == "C" or "c":
        print ("G")
    else:
        print("Please enter a valid input")
else:
    for x in dna_chain:
        if x == "A" or x == "a":
            new_string = new_string + "T"
        elif x == "G" or x == "g":
            new_string = new_string + "C"
        elif x == "T" or x == "t":
            new_string = new_string + "A"
        elif x == "C" or x == "c":
            new_string = new_string + "G"
        else:
            print("String contains an invalid input")
            break
    print(new_string)

```
## Proof of Work

![image](https://github.com/user-attachments/assets/03d74e31-ec76-4374-a2dd-b559912e7f67)

## Paper Solution
