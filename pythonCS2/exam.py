
from qlist import *

marks = 0

for q in qlist:
    question = q['question']
    option1 = q['option1']
    option2 = q['option2']
    option3 = q['option3']
    correct_ans = q['correct_ans']

    print(question)
    print(option1)
    print(option2)
    print(option3)
    ans = input('Choose correct ans: (1,2,3): ')

    if ans == correct_ans:
        print('Congratulations, correct ans')
        marks += 1
    else:
        print('Wrong Answer')
    print(f'your marks is now {marks}')
    print()