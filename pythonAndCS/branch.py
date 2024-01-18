# ၁၀ နှစ်အောက်ဆို ၁၀၀ ပေးမယ်
# ၁၀ နှစ်နဲ့ ၂၀ ကြားဆို ၂၀၀ ပေးမယ်
# ၂၀ နဲ့အထက် ၃၀၀

age = input('Enter your age: ')
age = int(age)
pocket_money = 0

#Branching
if age < 10:
   pocket_money = 100
  
if age >= 10 and age<20:
   pocket_money = 200

if age >= 20:
   pocket_money = 300

print(f'your pocket money is {pocket_money} $')