print ("WELCOME TO THE QUIZZZ!")

questions = ("1. Which of these is not a core data type?",
            "2. Which module in Python supports regular expressions?",
            "3. To start Python from the command prompt, use the command ___",
            "4. What is the output of the expression : 3*1**3",
            "5. Which of the following is correct about Python?",)


options= (("A. Lists", "B. Dictionary", "C. Tuples", "D. Class"),
         ("A. re","B. regex","C. pyregex","D. None"),
         ("A. execute python","B. go python","C. python","D. run python"),
         ("A. 9","B. 3 ","C. 27 ","D. 1"),
         ("A. It supports automatic garbage collection.","B. It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java","C. Both of the above","D. None of the above"))

answers= ("D ","A","C","B","C")

guesses= [] 

score= 0

question_num = 0

for question in questions:
    print("---------------------------------------------------")
    print(question)
    for option in options[question_num]:
     print(option)
    
    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)    
    if guess == answers[question_num]:
      score += 1
      print("CORRECT HORRAYYY!")
    else:
      print("INCORRECT")
      print(f"{answers[question_num]} is the correct answer")

    question_num += 1
 
print("------------------------------") 
print("------------------------------")
print("            RESULTS           ")
print("------------------------------") 
print("------------------------------")


score= int(score/ len(questions) * 100)
print(f"Your score is: {score}%")
