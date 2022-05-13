time = input('Enter the time in HH:MM:SS Format: ')

hour, minute, second = time.split(":")

hour, minute, second = int(hour), int(minute), int(second)

print("Hour: ", hour, "Minute: ", minute, "Second: ", second)
