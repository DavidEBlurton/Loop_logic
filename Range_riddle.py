days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Printing even days of the week")
for a in range(len(days_of_week)):
    if a % 2 == 0:
        print(days_of_week[a])