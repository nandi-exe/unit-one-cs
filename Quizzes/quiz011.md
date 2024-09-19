# Quiz 011

## Paper Solution

<img width="837" alt="Screenshot 2024-09-19 at 9 10 00" src="https://github.com/user-attachments/assets/f5145d16-70c7-44a1-9bdb-6a29fd239a1f">

## Code 

```
def best_month(month:str):
    months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    start_days= [1,4,5,1,3,1,1,4,0,2,5,0]
    week = ["Sun","Mon","Tues","Wed","Thurs","Fri","Sat"]
    last_day = [30,28,31,20,31,30, 31,31,30,31,30,31]
    x = month.lower()
    month_found = False
    weekday_count = 0
    count = 0
    start_day = ""
    while not month_found:
        if x in months[count]:
            month_found = True
            weekday_count = start_days[count]
            start_day = week[weekday_count]
            quit = last_day[count]
        elif count < 11:
            count = count + 1
        else:
            print("Input not found")
            break
    if month_found:
        for day in range(0,quit):
            weekday = weekday_count%7
            date = week[weekday], day +1
            weekday_count = weekday_count +1
            print(date)

```

## Proof of Work

<img width="1470" alt="image" src="https://github.com/user-attachments/assets/23fea92f-540e-4a17-9c0b-c736dea10897">

## Flowchart
