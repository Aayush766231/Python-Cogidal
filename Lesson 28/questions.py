questions = ["What is your name?", "What is your favorite food?", "What is your favorite color? "]
for x, y in enumerate(questions, start=1):
    print(f"{x}: {y}")
    value = input()