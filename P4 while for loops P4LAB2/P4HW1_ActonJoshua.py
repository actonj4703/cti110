# Joshua Acton
# 04/03/2025
# P4HW1
# Calculates letter grades and lists the lowest score




num_scores = int(input("How many scores do you want to enter? "))

scores = []  


for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i} again:", end=' ')


lowest_score = min(scores)
scores.remove(lowest_score)


average_score = sum(scores) / len(scores)


if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'


print("\n------------Results------------")
print(f"Lowest Score   : {lowest_score:.1f}")
print(f"Modified List  : {scores}")
print(f"Scores Average : {average_score:.2f}")
print(f"Grade          : {grade}")
print("--------------------------------")
