def info(firstname, surname, birthdate, city, email, phone_number):
    return f"Name:{firstname}\n Surname:{surname}\n Birthdate:{birthdate}\n City:{city}\n e-mail:{email}\n Phone " \
           f"number: {phone_number} "


print(info(firstname=input("Enter your name:"), surname=input("Enter your surname:"), birthdate=input("Enter your birhdate:"),
           city=input("Enter your city:"), email=input("Enter your email:"), phone_number=input("Enter your phone number:")))

