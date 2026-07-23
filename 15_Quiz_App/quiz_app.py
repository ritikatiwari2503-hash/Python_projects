questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Pune", "Jaipur"],
        "answer": "Delhi"
    },
    {
        "question": "What is 5 x 5?",
        "options": ["20", "25", "30", "35"],
        "answer": "25"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Earth", "Venus", "Mercury", "Mars"],
        "answer": "Mercury"
    }
] # questions and their corresponding options with answers 


score = 0
for q in questions:(q["question"]) # for loop for returning the score gathered from all correct app

   
    # options print karo (enumerate use karo numbering ke liye)
for i, option in enumerate(q["options"], 1):
    print(f"{i}. {option}")
    
# user se answer lo
user_answer = input("Your answer: ")
    
# check karo sahi hai ya nahi
if user_answer == q["answer"]:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! Correct answer: {q['answer']}")

# loop ke baad score print karo
print(f"\nYour score: {score}/{len(questions)}")


# for q in questions:        ← question 1 lo
#     print(question)        ← "What is capital of India?"
#     for option in options: ← options print karo (1,2,3,4)
#     user_answer = input()  ← answer lo
#     check karo             ← sahi/galat?

# for q in questions:        ← question 2 lo
#     ... same repeat
    
# for q in questions:        ← question 3 lo
#     ... same repeat

# score print karo           ← loop khatam hone ke baad
