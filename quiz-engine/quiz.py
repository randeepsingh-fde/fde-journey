import random
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "quiz_history.json"

question_list = [
    {
        "question": "1. Which gas makes up the largest percentage of Earth's atmosphere?",
        "correct_answer": "Nitrogen",
        "options": ("Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"),
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "question": "2. Which country is known as the Land of the Rising Sun?",
        "correct_answer": "Japan",
        "options": ("China", "Japan", "Thailand", "South Korea"),
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "question": "3. How many players are there in a standard football team on the field?",
        "correct_answer": "11",
        "options": ("9", "10", "11", "12"),
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "question": "4. Who was the first woman to win a Nobel Prize?",
        "correct_answer": "Marie Curie",
        "options": ("Mother Teresa", "Marie Curie", "Rosalind Franklin", "Jane Addams"),
        "category": "General Knowledge",
        "difficulty": "Medium"
    },
    {
        "question": "5. Who wrote Romeo and Juliet?",
        "correct_answer": "William Shakespeare",
        "options": ("Charles Dickens", "William Shakespeare", "George Orwell", "Oscar Wilde"),
        "category": "General Knowledge",
        "difficulty": "Medium"
    },
    {
        "question": "6. How many colours are traditionally identified in a rainbow?",
        "correct_answer": "7",
        "options": ("5", "6", "7", "8"),
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "question": "7. Which ancient civilization developed cuneiform writing?",
        "correct_answer": "Sumerians",
        "options": ("Egyptians", "Romans", "Sumerians", "Greeks"),
        "category": "General Knowledge",
        "difficulty": "Hard"
    },
    {
        "question": "8. Who is popularly known as the Missile Man of India?",
        "correct_answer": "A. P. J. Abdul Kalam",
        "options": ("C. V. Raman", "Homi J. Bhabha", "A. P. J. Abdul Kalam", "Vikram Sarabhai"),
        "category": "General Knowledge",
        "difficulty": "Medium"
    },
    {
        "question": "9. Which treaty formally ended World War I between Germany and the Allied Powers?",
        "correct_answer": "Treaty of Versailles",
        "options": ("Treaty of Paris", "Treaty of Versailles", "Treaty of Vienna", "Treaty of Tordesillas"),
        "category": "General Knowledge",
        "difficulty": "Hard"
    },
    {
        "question": "10. Which organization publishes the annual Human Development Report?",
        "correct_answer": "UNDP",
        "options": ("World Bank", "UNESCO", "UNDP", "World Economic Forum"),
        "category": "General Knowledge",
        "difficulty": "Medium"
    },
    {
        "question": "11. What is the chemical formula of water?",
        "correct_answer": "H2O",
        "options": ("CO2", "H2O", "O2", "NaCl"),
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "12. Which planet is known as the Red Planet?",
        "correct_answer": "Mars",
        "options": ("Venus", "Mars", "Jupiter", "Mercury"),
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "13. What is the main ingredient used to make traditional glass?",
        "correct_answer": "Sand",
        "options": ("Sand", "Limestone", "Clay", "Salt"),
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "14. Which part of a human cell contains most of its genetic material?",
        "correct_answer": "Nucleus",
        "options": ("Cytoplasm", "Ribosome", "Nucleus", "Cell membrane"),
        "category": "Science",
        "difficulty": "Medium"
    },
    {
        "question": "15. Which vitamin is primarily produced by the human body when skin is exposed to sunlight?",
        "correct_answer": "Vitamin D",
        "options": ("Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"),
        "category": "Science",
        "difficulty": "Medium"
    },
    {
        "question": "16. Which organ in the human body is primarily responsible for filtering blood and producing urine?",
        "correct_answer": "Kidneys",
        "options": ("Liver", "Heart", "Kidneys", "Lungs"),
        "category": "Science",
        "difficulty": "Easy"
    },
    {
        "question": "17. What is the SI unit of electric resistance?",
        "correct_answer": "Ohm",
        "options": ("Volt", "Ampere", "Ohm", "Watt"),
        "category": "Science",
        "difficulty": "Medium"
    },
    {
        "question": "18. What is the approximate escape velocity from Earth's surface?",
        "correct_answer": "11.2 km/s",
        "options": ("5.2 km/s", "7.9 km/s", "11.2 km/s", "15.6 km/s"),
        "category": "Science",
        "difficulty": "Hard"
    },
    {
        "question": "19. Which subatomic particle has no electric charge?",
        "correct_answer": "Neutron",
        "options": ("Proton", "Electron", "Neutron", "Positron"),
        "category": "Science",
        "difficulty": "Hard"
    },
    {
        "question": "20. What is the approximate speed of light in a vacuum?",
        "correct_answer": "300,000 km/s",
        "options": ("150,000 km/s", "200,000 km/s", "300,000 km/s", "450,000 km/s"),
        "category": "Science",
        "difficulty": "Medium"
    },
    {
        "question": "21. What does USB stand for?",
        "correct_answer": "Universal Serial Bus",
        "options": ("Universal System Board", "United Serial Bus", "Universal Serial Bus", "Unified Storage Base"),
        "category": "Technology",
        "difficulty": "Easy"
    },
    {
        "question": "22. What does CPU stand for?",
        "correct_answer": "Central Processing Unit",
        "options": ("Central Processing Unit", "Computer Power Unit", "Central Program Utility", "Core Processing Utility"),
        "category": "Technology",
        "difficulty": "Easy"
    },
    {
        "question": "23. Which programming language is primarily used to structure the content of web pages?",
        "correct_answer": "HTML",
        "options": ("Python", "HTML", "C++", "SQL"),
        "category": "Technology",
        "difficulty": "Medium"
    },
    {
        "question": "24. What does URL stand for?",
        "correct_answer": "Uniform Resource Locator",
        "options": ("Universal Reference Link", "Uniform Resource Locator", "Unified Retrieval Language", "User Resource Location"),
        "category": "Technology",
        "difficulty": "Medium"
    },
    {
        "question": "25. Which company developed the Android operating system?",
        "correct_answer": "Google",
        "options": ("Apple", "Microsoft", "Google", "IBM"),
        "category": "Technology",
        "difficulty": "Easy"
    },
    {
        "question": "26. What does SQL primarily stand for?",
        "correct_answer": "Structured Query Language",
        "options": ("Structured Query Language", "Sequential Question Logic", "Standard Quality Language", "System Query Link"),
        "category": "Technology",
        "difficulty": "Hard"
    },
    {
        "question": "27. What is the primary purpose of a firewall in computer networks?",
        "correct_answer": "Monitor and control network traffic",
        "options": ("Increase internet speed", "Store passwords", "Monitor and control network traffic", "Compress files"),
        "category": "Technology",
        "difficulty": "Medium"
    },
    {
        "question": "28. Which data structure follows the LIFO principle?",
        "correct_answer": "Stack",
        "options": ("Queue", "Stack", "Linked List", "Tree"),
        "category": "Technology",
        "difficulty": "Hard"
    },
    {
        "question": "29. What does RAM stand for?",
        "correct_answer": "Random Access Memory",
        "options": ("Read Access Memory", "Random Access Memory", "Rapid Application Module", "Remote Allocation Memory"),
        "category": "Technology",
        "difficulty": "Medium"
    },
    {
        "question": "30. Which cryptographic algorithm is commonly used for key exchange and digital signatures?",
        "correct_answer": "RSA",
        "options": ("RSA", "JPEG", "FTP", "HTML"),
        "category": "Technology",
        "difficulty": "Hard"
    },
    {
        "question": "31. Which is the largest continent by land area?",
        "correct_answer": "Asia",
        "options": ("Africa", "Europe", "Asia", "North America"),
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "question": "32. What is the capital of Australia?",
        "correct_answer": "Canberra",
        "options": ("Sydney", "Melbourne", "Canberra", "Perth"),
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "question": "33. Which is the longest river in India?",
        "correct_answer": "Ganga",
        "options": ("Yamuna", "Ganga", "Godavari", "Brahmaputra"),
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "question": "34. Which desert is the largest hot desert in the world?",
        "correct_answer": "Sahara",
        "options": ("Gobi", "Arabian", "Sahara", "Kalahari"),
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "question": "35. Which ocean is the largest in the world?",
        "correct_answer": "Pacific Ocean",
        "options": ("Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"),
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "question": "36. Which country has the most natural lakes in the world?",
        "correct_answer": "Canada",
        "options": ("Russia", "Canada", "Finland", "United States"),
        "category": "Geography",
        "difficulty": "Hard"
    },
    {
        "question": "37. Mount Kilimanjaro is located in which country?",
        "correct_answer": "Tanzania",
        "options": ("Kenya", "Tanzania", "Ethiopia", "Uganda"),
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "question": "38. Which strait separates Asia from North America?",
        "correct_answer": "Bering Strait",
        "options": ("Strait of Malacca", "Bering Strait", "Strait of Gibraltar", "Bosporus Strait"),
        "category": "Geography",
        "difficulty": "Hard"
    },
    {
        "question": "39. Which Indian state has the longest coastline?",
        "correct_answer": "Gujarat",
        "options": ("Maharashtra", "Tamil Nadu", "Gujarat", "Andhra Pradesh"),
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "question": "40. Which is the world's highest uninterrupted waterfall?",
        "correct_answer": "Angel Falls",
        "options": ("Niagara Falls", "Victoria Falls", "Angel Falls", "Iguazu Falls"),
        "category": "Geography",
        "difficulty": "Hard"
    }
]

def get_categories(question_list):
    category_list = set()
    for i in range(len(question_list)):
        category_list.add(question_list[i].get("category"))
    return sorted(category_list)


def display_categories(category_list):
    print("========== QUIZ CATEGORIES ==========")
    for i, category in enumerate(category_list, start=1):
        print(i, category)


def select_category(category_list, default_category= "General Knowledge"):
    display_categories(category_list)
    while True:
        try:
            category_choice = input("Select a category: ")
            if category_choice == "":
                return default_category
            elif 1 <= int(category_choice) <= len(category_list):
                break
            else:
                print("Category needs to be from the menu options.")
        except ValueError:
            print("Please enter a valid number.")
    return category_list[int(category_choice) - 1]


def get_questions_by_category(question_list, selected_category):
    category_questions = []
    for i in range(len(question_list)):
        if question_list[i].get("category") == selected_category:
            category_questions.append(question_list[i])
    return category_questions


def get_difficulties(category_questions):
    difficulty_list = set()
    for i in range(len(category_questions)):
        difficulty_list.add(category_questions[i].get("difficulty"))
    return sorted(difficulty_list)


def select_difficulty(difficulty_list):
    print("========== SELECT DIFFICULTY ==========")
    for i, difficulty in enumerate(difficulty_list, start=1):
        print(i, difficulty)

    while True:
        try:
            difficulty_choice = int(input("Select the difficulty: "))
            if 1 <= difficulty_choice <= len(difficulty_list):
                break
            else:
                print("Difficulty needs to be from the above list only.")
        except ValueError:
            print("Please enter a valid number.")

    return difficulty_list[difficulty_choice - 1]


def filter_questions(category_questions, selected_difficulty):
    filtered_questions = []
    for i in range(len(category_questions)):
        if category_questions[i].get("difficulty") == selected_difficulty:
            filtered_questions.append(category_questions[i])
    return filtered_questions


def play_quiz(filtered_questions):
    random.shuffle(filtered_questions)
    score = 0

    for i in range(len(filtered_questions)):
        print(filtered_questions[i].get("question"))
        for j, option in enumerate(filtered_questions[i].get("options"), start=1):
            print(j, option)

        while True:
            try:
                user_answer = int(input("Your answer: "))
                if 1 <= user_answer <= len(filtered_questions[i].get("options")):
                    break
                else:
                    print("Enter a valid option as answer.")
            except ValueError:
                print("Answer has to be a valid option number.")

        if filtered_questions[i].get("options")[user_answer - 1] == filtered_questions[i].get("correct_answer"):
            score = score + 1
            print("Correct")
            print("Score:", score)
        else:
            print("Incorrect")
            print("Correct Answer:", filtered_questions[i].get("correct_answer"))
            print("Score:", score)

    return score


def display_results(filtered_questions, score):
    print("\n")
    print("========== QUIZ RESULTS ==========")
    print("\n")
    total_questions_played = len(filtered_questions)
    print("Total Questions:", total_questions_played)
    print("Correct Answers:", score)
    print("Incorrect Answers:", total_questions_played - score)
    print(f"Accuracy: {(score / total_questions_played) * 100:.2f}%")
    print("\n")


def ask_replay():
    while True:
        replay = input("Would you like to replay? (Y/N): ").strip().upper()
        if replay == "N":
            print("Thanks for Playing.")
            return False
        elif replay == "Y":
            print("Let's start again.")
            return True
        else:
            print("Enter either (Y/N).")


def count_questions_by_category(question_list, selected_category):
    number_of_questions = 0
    for i in range(len(question_list)):
        if question_list[i].get("category") == selected_category:
            number_of_questions = number_of_questions + 1
    return number_of_questions


def calculate_accuracy(total_questions, correct_answers):
    if total_questions == 0:
        return 0
    accuracy = (correct_answers/total_questions)*100
    return accuracy

def save_quiz_attempt(quiz_attempt):
    
    quiz_history = load_quiz_history()
    quiz_history.append(quiz_attempt)

    with open(HISTORY_FILE, "w") as file:
        json.dump(quiz_history, file, indent=4)

def display_quiz_history():
    quiz_history = load_quiz_history()

    if not quiz_history:
        print("No quiz history found.")
    else:
        print("\n========== QUIZ HISTORY ==========")

        for index, attempt in enumerate(quiz_history, start=1):
            print(f"\nAttempt {index}")
            print(f"Category: {attempt['category']}")
            print(f"Difficulty: {attempt['difficulty']}")
            print(f"Total Questions: {attempt['total_questions']}")
            print(f"Correct Answers: {attempt['correct_answers']}")
            print(f"Accuracy: {attempt['accuracy']:.2f}%")

def load_quiz_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            quiz_history = json.load(file)
        return quiz_history

    except FileNotFoundError:
        return []

def display_dashboard():
    quiz_history = load_quiz_history()

    if not quiz_history:
        print("No quiz data available. Complete a quiz first.")
    else:
        total_quizzes = len(quiz_history)
        total_questions = sum(d.get('total_questions', 0) for d in quiz_history)
        total_correct_answers = sum(d.get('correct_answers', 0) for d in quiz_history)
        overall_accuracy = (total_correct_answers / total_questions) * 100

        best_attempt = max(quiz_history, key=lambda x: x["accuracy"])

        print("\n========== PERFORMANCE DASHBOARD ==========")
        print(f"Total quizzes: {total_quizzes}")
        print(f"Total questions: {total_questions}")
        print(f"Total correct answers: {total_correct_answers}")
        print(f"Overall accuracy: {overall_accuracy:.2f}%")

        print("\n========== BEST PERFORMANCE ==========")
        print(f"Category: {best_attempt['category']}")
        print(f"Difficulty: {best_attempt['difficulty']}")
        print(f"Accuracy: {best_attempt['accuracy']:.2f}%")

def run_quiz(question_list):
    while True:
        category_list = get_categories(question_list)
        selected_category = select_category(category_list)
        category_questions = get_questions_by_category(question_list, selected_category)
        difficulty_list = get_difficulties(category_questions)
        selected_difficulty = select_difficulty(difficulty_list)
        filtered_questions = filter_questions(category_questions, selected_difficulty)

        score = play_quiz(filtered_questions)
        display_results(filtered_questions, score)

        accuracy = calculate_accuracy(len(filtered_questions), score)
        quiz_attempt = {
            "category": selected_category,
            "difficulty": selected_difficulty,
            "total_questions": len(filtered_questions),
            "correct_answers": score,
            "accuracy": accuracy,
        }
        save_quiz_attempt(quiz_attempt)
        print("Quiz attempt saved successfully.")

        should_replay = ask_replay()
        if should_replay is False:
            break


def main(question_list):
    while True:
        print("\n========== QUIZ ENGINE ==========")
        print("1. Start a new quiz")
        print("2. View quiz history")
        print("3. View performance dashboard")
        print("4. Exit")

        try:
            menu_choice = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if menu_choice == 1:
            run_quiz(question_list)
        elif menu_choice == 2:
            display_quiz_history()
        elif menu_choice == 3:
            display_dashboard()
        elif menu_choice == 4:
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Please select an option between 1 and 4.")


if __name__ == "__main__":
    main(question_list)