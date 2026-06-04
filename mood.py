from datetime import datetime

# Getting  current date and time
now = datetime.now()

# User inputs
name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/stressed/angry/normal/neutral): ").lower()
energy = int(input("Enter your energy level (1-10): "))

# Display date and time
print("\nCurrent Date and Time:", now.strftime("%d-%m-%Y %H:%M:%S"))

# Personalized advice using conditional statements
print("\nHi there!,", name + "!")

if mood == "happy":
    print("Keep spreading positivity & remeber to stay positive")
elif mood == "sad":
    print("Try talking to a friend or someone you love and also try doing something you enjoy.")
elif mood == "stressed":
    print("Take short breaks, dont overwork yourself & complete one task at a time.")
elif mood == "angry":
    print("Take a deep breath, go for a walk and take in some fresh air it will help improve your mood.")
elif mood == "normal":
    print("Then continue to enjoy your day!!!!!!")
elif mood == "neutral":
    print("Try something new and fun to brighten your day")
else:
    print("Have a great day and take care of yourself!")

# Advice based on energy level
if energy >= 8:
    print("You have lots of energy today! Take on challenging tasks & try something fun & intresting.")
elif energy >= 5:
    print("Your energy level is moderate. Stay productive and take breaks when you feel tired.")
else:
    print("Your energy is low. Make sure to rest and stay hydrated.")