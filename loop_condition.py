bus = []

while len(bus) < 5:
    print("Letting a person on the bus...")
    bus.append('person')
    print("There are", len(bus), "people on the bus right now")

print(bus)

flag = True

while flag:
    user = input("If you would like to quit then just type quit.")
    if user == 'quit':
        break