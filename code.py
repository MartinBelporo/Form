# This program FOR TAXES CALCULATION!

print("Welcome to the tax form")
name = input("Enter your name: ")
position = input("Enter your position: HR OR ENG. ")
salary = int(input("Enter your annual salary: "))
country = input("Enter your country (CAN, US): ")
if position == "HR":
    if country == "CAN":
        taxes=(salary+8000)*0.2
        print("The amount of taxes you pay is " + str(taxes)+ ' $') 
    elif country == "US":
        taxes=(salary+8000)*0.15
        print("The amount of taxes you pay is " + str(taxes)+' $') 
if position == "ENG":
    if country =="US":
      Tax =(salary+20000)*0.15
      print("The amount of taxes you pay is " + str(Tax)+ ' $')
      print("Thank you for choosing us")
    elif country == "CAN":
       Tax =(salary+8000)*0.15
       print("The amount of taxes you pay is " + str(Tax)+ ' $')
       print("Thank you for choosing us")


