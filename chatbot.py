import time
import random
name = input("Hello, what is your name? ")
time.sleep(2)
print("Hello " + name)
feeling = input("How are you today? ")
time.sleep(1)
if "good" in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")
time.sleep(1)
favcolour = input("What is your favourite colour? ")
colours = ["Red","Green","Blue"]
time.sleep(1)
print("My favourite colour is " + random.choice(colours))
mood = input("What are you doing today? ")
mood = ["dancing", "reading", "playing", "watching TV", "hiking"]
time.sleep(1)
print("I feel like " + random.choice(mood) + " today")
love=input("Do you have a girlfriend? ")
love = ["Yes", "No"]
time.sleep(1)
input("cool")
