print("Menu:")
print("1. BRUSCHETTA = $360.82")
print("2. CAPRESA = $300.58")
print("3. BURRATA = $391.54")
print("4. MARGARITA = $572.25")
print("5. PIZZAS = $572.25")
print("6. LASAGNA = $632.49")
print("7. RAVIOLI = $662.61")
print("8. CARBONARA = $541.53")
print("9. PESTO = $481.29")
 
reservation = input("Do you have a reservation: ")
if reservation.lower() == "no":
    print("Sorry, you need a reservation.")
else:
    name = input("Enter your name: ")
    print(f"Welcome, {name}")
 
    BRUSCHETTA = int(input("How many BRUSCHETTAS would you like?: "))
    CAPRESA = int(input("How many CAPRESA would you like?: "))
    BURRATA = int(input("How many BURRATA would you like?: "))
    MARGARITA = int(input("How many MARGARITA would you like?: "))
    PIZZAS = int(input("How many PIZZAS would you like?: "))
    LASAGNA = int(input("How many LASAGNA would you like?: "))
    RAVIOLI = int(input("How many RAVIOLI would you like?: "))
    CARBONARA = int(input("How many CARBONARA would you like?: "))
    PESTO = int(input("How many PESTO's would you like?: "))
 
    total = (BRUSCHETTA * 360.82 + 64.9476) + (CAPRESA * 300.58 + 54.1044) + (BURRATA * 391.54 + 70.4772) + (MARGARITA * 572.25 + 103.005) + (PIZZAS * 572.25 + 103.005) + (LASAGNA * 632.49 + 113.8482) + (RAVIOLI * 662.61 + 119.2698) + (CARBONARA * 541.53 + 97.4754) + (PESTO * 481.29 + 86.6322)
 
    # Order Summary
    print("Your order summary:")
    print(f"{BRUSCHETTA}x BRUSCHETTA(s) - ${BRUSCHETTA * 360.82 + 64.9476:.2f}")
    print(f"{CAPRESA}x CAPRESA(s) - ${CAPRESA * 300.58 + 54.1044:.2f}")
    print(f"{BURRATA}x BURRATA(s) - ${BURRATA * 391.54 + 70.4772:.2f}")
    print(f"{MARGARITA}x MARGARITA(s) - ${MARGARITA * 572.25 + 103.005:.2f}")
    print(f"{PIZZAS}x PIZZAS(s) - ${PIZZAS * 572.25 + 103.005:.2f}")
    print(f"{LASAGNA}x LASAGNA(s) - ${LASAGNA * 632.49 + 113.8482:.2f}")
    print(f"{RAVIOLI}x RAVIOLI(s) - ${RAVIOLI * 662.61 + 119.2698:.2f}")
    print(f"{CARBONARA}x CARBONARA(s) - ${CARBONARA * 541.53 + 97.4754:.2f}")
    print(f"{PESTO}x PESTO(s) - ${PESTO * 481.29 + 86.6322:.2f}")
 
    desert = input("Would you like to have desert? ")
    if desert.lower() == "no":
        print(f"\nTotal amount: ${total:.2f}")
        print(f"Thank you, {name}. Goodbye!")
    else:
        print("HERE IS THE DESERT MENU.")
        print("1. TIRAMISU = $451.78")
        print("2. ICECREAM = $180.71")
        print("3. CREPE = $421.06")
 
        TIRAMISU = int(input("How many TIRAMISU would you like?: "))
        ICECREAM = int(input("How many ICECREAM would you like?: "))
        CREPE = int(input("How many CREPE would you like?: "))
 
        totalS = total + (TIRAMISU * 451.78 + 81.3204) + (ICECREAM * 180.71 + 32.5278) + (CREPE * 421.06 + 75.7908)
        print(f"Your total with dessert is: ${totalS:.2f}")
 
        cardorcash = input("Would you like to pay with card or cash? ")
 
        if cardorcash.lower() == "cash":
            amount_paid = int(input("How much are you paying with? "))
            change = amount_paid - totalS
 
            if change > 0:
                print(f"Change: ${change:.2f}")
                bills = [2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
                change_breakdown = {}
                for bill in bills:
                    bill_count = change // bill
                    if bill_count > 0:
                        change_breakdown[bill] = int(bill_count)
                        change -= bill_count * bill
 
                print("Change breakdown:")
                for bill, count in change_breakdown.items():
                    print(f"{count}x {bill} DOP")
 
        if cardorcash.lower() == "card":
            tip = input("Would you like to tip? (yes/no) ")
            if tip.lower() == "yes":
                tip_amount = int(input("How much would you like to tip? 10, 25, 50, 75, 100: "))
                totalS += tip_amount
                print(f"Thank you for the tip! Your total amount is now: ${totalS:.2f}")
            else:
                print(f"Your total amount is: ${totalS:.2f}")
        print(f"Thank you, {name}. Goodbye!")