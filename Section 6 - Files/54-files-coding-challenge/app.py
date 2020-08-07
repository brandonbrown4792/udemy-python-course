file = open("questions.txt", "r")

questions = [line.strip() for line in file]
file.close()

score = 0

for question in questions:
    question_arr = question.split("=")

    user_input = input(f'{question_arr[0]}=')

    if user_input == question_arr[1]:
        score += 1

result_file = open("result.txt", "w")

result_file.write(f'Your final score is {score}/{len(questions)}.')
result_file.close()
