# Quiz 015

## Paper Solution

![image](https://github.com/user-attachments/assets/a36a91bd-f1e9-4e86-86db-20db47639754)

## Flowchart

## Code

```
def averageLength(words: list) -> float:
    total_length = 0
    total_words = len(words)

    for word in words:
        total_length += len(word.replace(" ", ""))

    if total_words == 0:
        return 0.0  # Handle case of empty list
    return total_length / total_words
```

## Proof of Work

![image](https://github.com/user-attachments/assets/734dfc4d-4ed0-4e91-85ca-b59b0b5de162)
