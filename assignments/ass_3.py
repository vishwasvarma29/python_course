def run_quiz(questions):
    score = 0
    print("🧠 Welcome to the Python Quiz Game!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'\n")

    print(f"🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You got all correct!")
    elif score > len(questions) * 0.7:
        print("👍 Great job! Keep practicing!")
    else:
        print("💡 Keep learning! You can do it!")

# List of 20  Python quiz questions
quiz_questions = [
    {
        "question": "What is the result of len('Hello World')?",
        "options": ["a) 10", "b) 11", "c) 12", "d) 5"],
        "answer": "b"
    },
    {
        "question": "What does range(5) return?",
        "options": ["a) [0, 1, 2, 3, 4]", "b) [1, 2, 3, 4, 5]", "c) (0, 1, 2, 3, 4)", "d) {0, 1, 2, 3, 4}"],
        "answer": "a"
    },
    {
        "question": "Which is a valid variable name?",
        "options": ["a) 2var", "b) var_2", "c) var-2", "d) var 2"],
        "answer": "b"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["a) 6", "b) 8", "c) 9", "d) 5"],
        "answer": "b"
    },
    {
        "question": "Which keyword handles exceptions?",
        "options": ["a) handle", "b) exception", "c) catch", "d) try"],
        "answer": "d"
    },
    {
        "question": "Which data type stores true/false?",
        "options": ["a) int", "b) bool", "c) str", "d) float"],
        "answer": "b"
    },
    {
        "question": "What does append() do?",
        "options": ["a) Adds to list end", "b) Adds to set", "c) Adds to dict", "d) Deletes last item"],
        "answer": "a"
    },
    {
        "question": "Which operator checks equality?",
        "options": ["a) =", "b) ==", "c) :", "d) !="],
        "answer": "b"
    },
    {
        "question": "Which loop is for sequences?",
        "options": ["a) for", "b) do-while", "c) repeat", "d) until"],
        "answer": "a"
    },
    {
        "question": "What is int('10') + float('5.5')?",
        "options": ["a) '105.5'", "b) 105.5", "c) 15.5", "d) Error"],
        "answer": "c"
    },
    {
        "question": "What is bool('')?",
        "options": ["a) True", "b) False", "c) Error", "d) None"],
        "answer": "b"
    },
    {
        "question": "Which method removes item by value from list?",
        "options": ["a) pop()", "b) del", "c) remove()", "d) discard()"],
        "answer": "c"
    },
    {
        "question": "Which is mutable?",
        "options": ["a) tuple", "b) int", "c) str", "d) list"],
        "answer": "d"
    },
    {
        "question": "What does 'is' check in Python?",
        "options": ["a) Value equality", "b) Type check", "c) Identity", "d) Assignment"],
        "answer": "c"
    },
    {
        "question": "What is '7' + '3'?",
        "options": ["a) 10", "b) 73", "c) Error", "d) 21"],
        "answer": "b"
    },
    {
        "question": "What does float('5.0') return?",
        "options": ["a) 5", "b) '5.0'", "c) 5.0", "d) Error"],
        "answer": "c"
    },
    {
        "question": "Which symbol is used for exponentiation?",
        "options": ["a) ^", "b) *", "c) **", "d) //"],
        "answer": "c"
    },
    {
        "question": "What is the result of 9 // 2?",
        "options": ["a) 4.5", "b) 4", "c) 5", "d) 5.0"],
        "answer": "c"
    },
    {
        "question": "Which function converts string to integer?",
        "options": ["a) str()", "b) float()", "c) int()", "d) chr()"],
        "answer": "c"
    },
    {
        "question": "What does 'in' keyword do?",
        "options": ["a) Assign", "b) Loop", "c) Membershib test", "d) comment"],
        "answer":"c"
    }
]
run_quiz(quiz_questions)