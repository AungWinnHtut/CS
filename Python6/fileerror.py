from icecream import ic
marks = 0

with open('Q.txt','r') as file:
    for one_q in file:
        #ic(one_q)
        question, correct_answer = one_q .split('#')
        ans = input(question)
        #ic(question)
        #ic(ans)
        if ans == correct_answer.strip():
            marks += 10
            print(f'Your answer is correct! Now your marks are {marks}\n')
        else:
            print(f'Your answer is wrong! So your marks are {marks}\n')
print(f'Finally, your total marks are {marks}')