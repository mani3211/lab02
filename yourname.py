#I want this program to ask the user
#for their name. "What's your name?" and then,
#I want the program to say "Hi, NAME"
#Back where NAME is the users actual name

#step 1, ask the user what their name is
print("What is your name?")
#step 2, input the name from the keyboard
#and then save it into a variable so we can use it later
user_name = input()
#step 3, say hi back using the user's name
print("Hi, " +user_name + ".")
#step 4, great introduction. Now asking for the user's age
print("How old are you?")
#step 5, input the age from the keyboard, then save it to a variable so we can use it later
user_age = input()
#step 6, after getting a light introduction to the user,
# ask them about their favorite food and add a response
print("Well it's nice to finally meet you, " +user_name + "!")
print("You like food right? What is your favorite food?")
favorite_food = input()
print("That's awesome! I like " +favorite_food + " aswell!")