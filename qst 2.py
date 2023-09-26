def ticket_cost(age, show_time):
    matinee_13 = 7.50
    evening_13 = 10.00
    matinee_13_and_64 = 12.50
    evening_13_and_64 = 15.00
    matinee_65_and_older = 10.00
    evening_65_and_older = 12.50
    
    if age < 13:
        if show_time == "matinee":
            return matinee_13
        else:
            return evening_13
    elif age >= 13 and age <= 64:
        if show_time == "matinee":
            return matinee_13_and_64
        else:
            return evening_13_and_64
    else:
        if show_time == "matinee":
            return matinee_65_and_older
        else:
            return evening_65_and_older

age = int(input("Enter your age: "))
show_time = input("Enter show time (matinee/evening): ").lower()
ticket_cost = ticket_cost(age, show_time)
print(f"Ticket cost: ${ticket_cost:.2f}")
