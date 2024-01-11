import json
from icecream import ic


marks = 0
with open('q.json','r') as qfile:
    qlist = json.load(qfile)
    for q in qlist:
        print(q['question'])
        print(q['option1'])
        print(q['option2'])
        print(q['option3'])
        ans = input('choose 1,2,3: ')
        if ans == q['correct_ans']:
            print('Correct Ans!')
            marks += 1
        else:
            print('Wrong Ans!')
        print(f'Total makrs now {marks}')
        print()


print(f'Final Total makrs {marks}')
