print("=== Personality Profile Generator ===")
print("Please answer the following questions:")

# Get user input
name = input("1. What is your name? ")
age = input("2. How old are you? ")
city = input("3. Which city do you live in? ")
job = input("4. What is your occupation? ")
hobby = input("5. What are your hobbies? ")
favorite_food = input("6. What is your favorite food? ")
favorite_movie = input("7. What is your favorite movie? ")
dream = input("8. What is your biggest dream? ")
personality_trait = input("9. Describe a personality trait of yours: ")
superpower = input("10. If you could have one superpower, what would it be? ")

# Generate the profile
profile = f"""  
===== {name}'s Personality Profile =====  

{name}, {age} years old, lives in {city} and works as a {job}.  
In their free time, they enjoy {hobby} and love eating {favorite_food}.  

Personality trait: {personality_trait}  
Favorite movie: {favorite_movie}  

{name} dreams of one day {dream}.  
If they could have a superpower, it would be {superpower}!  

===== End of Profile =====  
"""

# Display the result
print("\nYour Personality Profile:")
print(profile)  