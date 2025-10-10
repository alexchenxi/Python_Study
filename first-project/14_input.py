# BMI = 体重/(身高**2)
import math

user_weight = float(input('Please input your weight(unit:kg): '))
user_height = float(input('Please input your height(unit:m): '))
user_BMI: float = user_weight / math.pow(user_height, 2)
print('Your BMI value is: ' + str(user_BMI))
if user_BMI < 18.5:
    print('You are thin')
elif 18.5 <= user_BMI < 24:
    print('You are normal')
elif 25 <= user_BMI < 28:
    print('You need more practise')
else:
    print('You are fat')
