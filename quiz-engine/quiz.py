question_list = [
    {
        "question": "1. Which gas makes up the largest percentage of Earth's atmosphere?",
        "correct_answer": "Nitrogen",
        "options": ("Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"),
    },
    {
        "question": "2. Which country is known as the Land of the Rising Sun?",
        "correct_answer": "Japan",
        "options": ("China", "Japan", "Thailand", "South Korea"),
    },
    {
        "question": "3. What is the main ingredient used to make traditional glass?",
        "correct_answer": "Sand",
        "options": ("Sand", "Limestone", "Clay", "Salt"),
    },
    {
        "question": "4. Which organ in the human body is primarily responsible for filtering blood and producing urine?",
        "correct_answer": "Kidneys",
        "options": ("Liver", "Heart", "Kidneys", "Lungs"),
    },
    {
        "question": "5. What does the abbreviation USB stand for?",
        "correct_answer": "Universal Serial Bus",
        "options": ("Universal System Board", "United Serial Bus", "Universal Serial Bus", "Unified Storage Base"),
    },
]
score = 0
for i in range(len(question_list)):
    print(question_list[i].get("question"))
    for j, option in enumerate(question_list[i].get("options"), start=1):
        print(j,option)
    user_answer = int(input("Your answer: "))
    if question_list[i].get("options")[user_answer-1] == (question_list[i].get("correct_answer")):
        score = score+1
        print("Correct")
        print("Score:",score)
    else:
        print("Incorrect")
        print("Correct Answer:", question_list[i].get("correct_answer"))
        print("Score:", score)

print("Final Score:", score)