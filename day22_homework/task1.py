#Create a function to greet a user with their full name and a custom message.
#Use positional arguments for first name and last name.
#Use a keyword argument for the greeting message with a default value.

def greet_user(first_name, last_name, greeting_message="Hello"):
    full_name = f"{first_name} {last_name}"
    print(f"{greeting_message}, {full_name}!")

greet_user("John", "Smith") 
greet_user("Jane", "Smith", greeting_message="Welcome")
