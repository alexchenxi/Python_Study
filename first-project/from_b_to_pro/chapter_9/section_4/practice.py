# 9.10

from resteraurant import Restaurant

my_restaurant = Restaurant("KFC", 'Fried Chicken')
my_restaurant.describe_restaurant()

print("########################")

# 9.11

# from user import Admin
#
# my_admin = Admin('Admin', "Howard", 23)
# my_admin.privileges.showPrivileges()

# 9.12
from admin import Admin

my_admin = Admin("Admin", 'KFC', 25)
my_admin.privileges.showPrivileges()
