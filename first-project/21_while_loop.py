print("Hello, this is a program to calculate average score.")
total = 0
count = 0
user_input = input("Please enter scores(When finished, press q to quit): ")
array = []
while user_input != "q":
    total += float(user_input)
    array.append(float(user_input))
    count += 1
    print("Current scores are: "+str(array))
    user_input = input("Please enter scores(When finished, press q to quit): ")
average = total / count
print("The average score is: " + str(average))