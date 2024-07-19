answers = []
inputs = []
score = 0

with open('answers.txt', 'r') as file:
    for line in file:
        answers.append(line.strip()[-1])

with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip()[-1])

for i in range(len(answers)):
    if inputs[i] == answers[i]:
        score += 1

percentage = (score/len(answers)*100).__round__(1)
print(f"Score was: {score}/{len(answers)}")
print(f"Percentage: {percentage}")