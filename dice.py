import random
import time

print("\nRolling the dice...")
time.sleep(5)

face = random.randint(1,6)
   
if face == 1:
        print("""
            -----
            |   |
            | o |
            |   |
            -----""")
elif face == 2:
        print("""
            -----
            |o  |
            |   |
            |  o|
            -----""")  
elif face == 3:
        print("""
            -----
            |o  |
            | o |
            |  o|
            -----""") 
elif face == 4:
        print("""
            -----
            |o o|
            |   |
            |o o|
            -----""") 
elif face == 5:
        print("""
            -----
            |o o|
            | o |
            |o o|
            -----""") 
elif face == 6:
        print("""
            -----
            |o o|
            |o o|
            |o o|
            -----""")  
