while True:
    age = input("How old are you? We have different prices for different age ranges: ")
    
    if age == "quit":
        break

    int_age = int(age)

    if int_age < 12:
        print("Your ticket price is $8!")
    elif int_age >= 65:
        print("Your ticket price is $10!")
    else:
        print("Your ticket price is $15!")

    