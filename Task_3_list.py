month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
season = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer',
          'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
while True:
    num = input("Enter number from 1 to 12 or 'stop' to stop:")
    if num == 'stop':
        break
    elif num.isdigit():
        if 1 <= int(num) <= 12:
            print(f"{int(num):02} is {month[int(num) -1]} month, {season[int(num) - 1]}")
        elif int(num) > 12 or int(num) <= 0:
            print("Enter number from 1 to 12 or 'stop' to stop!!!")
    elif type(num) == str:
        print("Enter number from 1 to 12 or 'stop' to stop!!!")
