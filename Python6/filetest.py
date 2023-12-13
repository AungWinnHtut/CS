from icecream import ic
in_file = open ('questions.txt','r')
q = in_file.readlines()
in_file.close()

marks=0
for one_q in q:
    question, correct_answer = one_q.split ("#")
    # correct_answer = correct_answer.strip()
    ic(question)
    ic(correct_answer)
    ans = input(question)
    if ans == correct_answer.strip():
        marks += 10
        print(f'Your answer is correct! Your marks become {marks}\n')
    else:
        print(f'Your answer is wrong! Your marks remain {marks}\n')
print(f'Your total marks is {marks}')

