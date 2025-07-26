import random

print("Welcome our snack/water game!")

com = random.randint(1, 3)
user = int(input("Enter \n1.Snack\n2.Water\n3.Gun: "))

def print_choice():
  if com == user:
    print("It's a tie!")

  elif (com == 1 and user == 2) or (com == 2 and user == 3) or (com == 3 and user == 1):
    print("Computer wins!")

  else:
    print("You win!")

print_choice()
