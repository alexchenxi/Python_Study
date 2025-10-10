def calculate_BMI(height, weight):
    user_BMI = weight / (height * height)
    return user_BMI


result1 = calculate_BMI(1.8, 65)
print(result1)
result2 = calculate_BMI(1.67, 65)
print(result2)
