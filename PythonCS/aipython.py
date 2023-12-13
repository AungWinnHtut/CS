#user input
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

#calculate BMI
bmi = weight/(height*height)

#output
print('Your BMI is ', bmi)