month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
         8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
season = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer',
          8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

while True:
    num = input("Enter number from 1 to 12 or 'stop' to stop:")
    if num == 'stop':
        break
    elif num.isdigit():
        if 1 <= int(num) <= 12:
            print(f"{int(num):02} is {month[int(num)]} month, {season[int(num)]}")
        elif int(num) > 12:
            print("Enter number from 1 to 12 or 'stop' to stop!!!")
    elif type(num) == str:
        print("Enter number from 1 to 12 or 'stop' to stop!!!")
