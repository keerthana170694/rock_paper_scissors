print("Welcome to PIZZA world!")
print("Amount details: \n small pizza:100 \n Medium pizza:200 \n Large pizz:300")
small_pizza=100
medium_pizza=200
large_pizza=300
pep_small=30
pepper=50
extra_cheese=20
user_choice=input("Enter size of pizza as above mentioned (s/m/l):")
user_choice=user_choice.lower()
if user_choice == "s":
    pep=input("If you want to add pepperoni for your small pizza(yes/no):")
    pep=pep.lower()
    if pep == "yes":
        print(f"pepperoni for small pizza= {pep_small}.")
        amt=small_pizza+pep_small
        print(f"Your pizza amount with added pepperoni is: {amt}")
    else:
        amt=small_pizza
        print(f"Your pizza amount is: {amt}")
elif user_choice == "m":
    pep=input("If you want to add pepperoni for your medium pizza(yes/no):")
    pep=pep.lower()
    if pep == "yes":
        print(f"pepperoni for medium pizza= {pep}")
        amt=medium_pizza+pepper
        print(f"Your pizza amount with added pepperoni is: {amt}")
    else:
        amt=medium_pizza
        print(f"Your pizza amount is: {amt}")
elif user_choice == "l":
    pep=input("If you want to add pepperoni for your large pizza(yes/no):")
    pep=pep.lower()
    if pep == "yes":
        print(f"pepperoni for large pizza= {pep}.")
        amt=large_pizza+pepper
        print(f"Your pizza amount with added pepperoni is: {amt}")
    else:
        amt=large_pizza
        print(f"Your pizza amount is: {amt}")
else:
    print("Invalid choice")
    
print("extra cheese for your pizza is rupee 20.")
cheese=input("Do you want to add extra cheese(yes/no):")
if cheese =="yes":
    print(f"your pizza amount is: {amt+extra_cheese}")
else:
    print("ok,Thank you!.please pay the above amount")

print("Thank you! visit again")