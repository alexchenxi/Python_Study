from random import randint, choice


# 9.13
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Die {self.sides} gives you number {randint(1, self.sides)}")


die_six = Die()
times = 10
while times > 0:
    die_six.roll_die()
    times -= 1

die_ten = Die(10)
times = 10
while times > 0:
    die_ten.roll_die()
    times -= 1

die_twenty = Die(20)
times = 10
while times > 0:
    die_twenty.roll_die()
    times -= 1

print("#####################")

# 9.14
lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']

lottery_res = ''
for i in range(4):
    lottery_res += choice(lottery_list)  # i从0开始，+1显示直观的次数

print(f"{lottery_res} is the winner!")

# 9.15
my_ticket = 'abcd'
count = 1
lottery_res = ''
while True:
    for i in range(4):
        lottery_res += choice(lottery_list)
    # print(f"{lottery_res} is the winner!")  # i从0开始，+1显示直观的次数

    if lottery_res == my_ticket:
        print(f"You win this with number \"{my_ticket}\", and you have tried {count} times!")
        break
    else:
        lottery_res = ''
        count += 1
