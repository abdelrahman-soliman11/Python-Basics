file = open("Students.txt", "a")


def storeInputs(firstName, lastName, gender, ID):
    Text = str(firstName + " " + lastName + " " + gender + " " + ID)
    file.write(Text)


firstName = input("Enter your FirstName: ")
lastName = input("Enter your LastName: ")
gender = input("Enter your Gender: ")
ID = input("Enter your ID 3 Digits only: ")

storeInputs(firstName, lastName, gender, ID)
