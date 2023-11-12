print("***Grade Calculator***")
print("This app computes grade based on score!")

user_score_input = input("Enter your score:")

try:
    score = float(user_score_input)
    if 0 <= score <= 100:  # Assuming the score should be between 0 and 100
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f'Your score: {score} Your grade is: {grade}')
    else:
        print("Invalid score. Please enter a number between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

print("End of the program!")
