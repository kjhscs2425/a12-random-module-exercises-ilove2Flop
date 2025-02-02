import random

# Choose:
# Type of animal (at least 3 choices, string)
animals = ["mountain chicken", "elephant shrew", "pika"]
animal = random.choice(animals)

# Age (integer)
age = random.randint(1, 40)  

# Color (at least 3 choices, string)
colors = ["cyan", "green", "rainbow"]
color = random.choice(colors)

# Weight (float)
weight = round(random.uniform(1.0, 20.0), 2) 

# Print a summary of your pet using an f-string
print(f"Your pet is a {color} {animal}, {age} years old, and weighs {weight} kg.")
