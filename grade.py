print("***Grade Calculator***")
print("THis app computes grade based on score!")

user_score_input = input("Enter your score:")

if user_score_input.isdigit():
    score = float(user_score_input)
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
    print(f'Your score:{score} Your grade is: {grade}')
else:
    print("Invalid number")
    
print("End of the program!")