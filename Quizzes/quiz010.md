# Quiz 010

## Paper Solution

<img width="584" alt="image" src="https://github.com/user-attachments/assets/ae71e564-6bfb-4740-953e-bb7707b7437a">

## Flowchart

![quiz009 drawio](https://github.com/user-attachments/assets/2b2bb152-616d-411f-93c3-340144b792f8)


## Code

```
def conversions(base:int):
    n_value = [10**12,10**9,10**6,10**3,0,10**-3,10**-6,10**-9,10**-12]
    units = ["Terra", "Giga", "Mega", "Kilo", "Unit", "Milli", "Micro", "Nano", "Pico"]
    product = []
    longest = 0
    gap = "   "
    for i in range (0,8):
        power = n_value[i]
        product.append(float(base*power))
        if len(str(product[i])) > longest:
            longest = len(str(product[i]))
    for a in range(0,8):
        if len(str(product[a])) != longest:
            extra = " "*(longest - len(str(product[a])))
        else:
            extra = ""
        print(f'{product[a]}{gap}{extra}{units[a]}')
```

## Proof of Work

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/e46e0b33-e9a2-40a6-9744-901e35fcf33c">



