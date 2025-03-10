#Question One – Random Number Generator
#Magic 8 Ball
#By:   Silvana Paredes
#Date: 19/02/2025

import random

#Affirmative answers
affirmative = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, definitely!",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs points to yes.",
]

#Non-committal
non_committal = [
    "Reply hazy, try again.", 
    "Ask again later.", 
    "Better not tell you now.", 
    "Cannot predict now.",
    "Concentrate and ask again",
]

#Negatives
negative = [
    "Don't count on it.", 
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]


responses = affirmative + non_committal + negative
cont_aff = 0
cont_non = 0
cont_neg = 0

next_question = 'Y'


while next_question == 'Y':  
    question = input("Please, enter your question:\n")

    #Get the answer
    answer = random.choice(responses)
    
    #Determine the type of answer   
    if answer in affirmative:
       cont_aff = cont_aff + 1.
    if answer in non_committal:
       cont_non = cont_non + 1.
    if answer in negative:
       cont_neg = cont_neg + 1.

    #print("\nAffirmative questions: ", cont_aff)
    #print("\nNon-committal questions: ", cont_non)
    #print("\nNegative questions: ", cont_neg)


    #Build the list by selecting possible answers
    if cont_aff >= 3:
        for item in affirmative:
          if item in responses:
            responses.remove(item)
    if cont_non >= 3:
        for item in non_committal:
          if item in responses:
            responses.remove(item)
    if cont_neg >= 3:
        for item in negative:
          if item in responses:
            responses.remove(item)
    if not responses:
        responses = affirmative + non_committal + negative
        
    print(responses)
        
    #Print the Answer
    print("Magic 8 Ball says:\n", answer)

    #Ask for the next question
    next_question = input("Do you want to continue (Y/N):\n")
    
    while next_question not in ['Y', 'N']:  
        next_question = input("Please enter a valid response (Y/N):\n")

    if next_question == 'N':
        print("Good bye!")
        break  










