import print_function

print_function.print_info("Alex", 37, location="Suzhou", field="It")

# from print_function import print_info

# print_info("Alex", 37)

from print_function import print_info as pi

pi("Bob", 35, gender="male")

import print_function as pf

pf.print_info("Chris", 23, gender="female", hobby="swimming")

from print_function import *

print_info("Alex", 37)
