print("Welcome to the Quiz Game!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    print("Maybe next time. Goodbye!")
    quit()
else:
    print("Great! Let's get started.")
score = 0
answer = input("What does GPU stand for?")
if answer.lower() == "graphic processing unit":
    score += 1
    print("Correct! - Your Score:" ,score)
else:
    print("Wrong answer")
    quit()
answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    score += 1
    print("Correct! - Your Score:" ,score)
else:
    print("Wrong answer")
    quit()
answer = input("What does RAM stand for?")
if answer.lower() == "random acess memory":
    score += 1
    print("Correct! - Your Score:" ,score)
else:
    print("Wrong answer")
    quit()
answer = input("what does ALU stand for?")
if answer.lower() == "aritmetic logic unit":
    score += 1
    print("Correct! - Your Score:" ,score)
else:
    print("Wrong answer")
    quit()
    

print("You score: "+ str(score/4)*100 +"%")