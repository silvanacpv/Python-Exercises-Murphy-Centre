#Question One – Random Number Generator
#Magic 8 Ball
#By:   Silvana Paredes
#Date: 19/02/2025

import random

#Responses
categories = {
    "affirmative": [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes, definitely!", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs points to yes."
    ],
    "non_committal": [
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again"
    ],
    "negative": [
        "Don't count on it.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful."
    ]
}

#Creating dictionary for responses with its categories
#responses = {answer: category for category, answers in categories.items() for answer in answers}
responses = {}
for category, answers in categories.items():
    for answer in answers:
       responses[answer] = category  #Assign response as key, and category (Affirmative, Non-Committal, Negative) as value
    
#Counting responses by category
category_count = {key: 0 for key in categories}


next_question = 'Y'

while next_question == 'Y':  
    input("Please, enter your question:\n")  

    #Get the answer
    answer = random.choice(list(responses.keys()))
    
    #Determine the type of answer   
    category = responses[answer]
    category_count[category] += 1

    #print(f"\nAffirmative: {category_count['affirmative']}, Non-committal: {category_count['non_committal']}, Negative: {category_count['negative']}")
    
    #Build the list by selecting possible answers
    for cat, count in category_count.items():
        if count >= 3:
            for response in categories[cat]:
                responses.pop(response, None)  #Delete responses if total per category >= 3
    
    #If there are no more responses, reset the counters
    if not responses:
        responses = {answer: category for category, answers in categories.items() for answer in answers}
        category_count = {key: 0 for key in categories}  # Reset counters

    #Print the Answer
    print("\nMagic 8 Ball says:", answer)

    #Ask for the next question
    next_question = input("Do you want to continue (Y/N):\n").strip().upper()

    while next_question not in ['Y', 'N']:  
        next_question = input("Please enter a valid response (Y/N):\n").strip().upper()

    if next_question == 'N':
        print("Goodbye!")
        break
