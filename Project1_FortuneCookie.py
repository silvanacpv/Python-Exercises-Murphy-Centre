#Question One – Option B
#Fortune Cookie
#By:   Silvana Paredes
#Date: 22/02/2025

import random

# Possible fortunes
responses = [
   "Great opportunities are coming your way.",
   "A pleasant surprise is waiting for you.",
   "Your kindness will lead you to success.",
   "Adventure and excitement are in your future.",
   "A wise decision will bring you happiness.",
   "Trust yourself, and good things will happen.",
]

#First part
print("Fortune:")

#Get the response
answer = random.choice(responses)
    
#Print the Answer    
print(answer, "\n")

#Second part
print("Random numbers:")
for numb in range(0,4):
    rand = random.randint(0, 99)
    print(rand)


    
  










