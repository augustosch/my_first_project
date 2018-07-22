
number_to_guess = 8

user_number = int(input("adivina el numero:"))

if number_to_guess == user_number:
    print("has ganado")
else:
    user_number = int(input("fallaste, te quedan 4 vidas, dime otro numero:"))

    if number_to_guess == user_number:
        print("has ganado")
    else:
        user_number = int(input("fallaste, te quedan 3 vidas, dime otro numero:"))

        if number_to_guess == user_number:
            print("has ganado")
        else:
            user_number = int(input("fallaste, te quedan 2 vidas, dime otro numero:"))

            if number_to_guess == user_number:
                print("has ganado")
            else:
                user_number = int(input("fallaste, te queda 1 vida, dime otro numero:"))
                if number_to_guess == user_number:
                    print("has ganado")
                else:
                    print("perdiste, te quedaste sin vidas")