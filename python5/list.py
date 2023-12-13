marks = [56,77,68,79,80,81,82,83] #0 - 7
status = 1 # 1 - pass the exam 0 - fail the exam

for m in marks:
    if m >= 50:
        print("Pass")
    else:
        print("Fail")
        status = 0

print()

if status == 0:
    print("Fail the Exam")
else:
    print("Pass the Exam")