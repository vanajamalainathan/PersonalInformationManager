
# welcome to my first Python project! This program collects personal information from the user and displays it in a formatted manner.
# My project

# Welcome message
print("=" * 40)
print("    welcome to my first Python project!")
print("=" * 40)
print()

# Store static information
name = "Ajana"
age = 21
city = "New York"
hobby = "reading"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_movie = input("What's your favorite movie? ")
while favorite_movie == "":
    print("Please enter a valid movie!")
    favorite_movie = input("What's your favorite movie? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

favorite_sport = input("What's your favorite sport? ")
while favorite_sport == "":
    print("Please enter a valid sport!")
    favorite_sport = input("What's your favorite sport? ")


# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Movie: {favorite_movie}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for your time!")
print("=" * 40)