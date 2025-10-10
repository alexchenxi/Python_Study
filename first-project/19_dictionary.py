slang_dict = {"Alex": "18514003311", "Bob": "13966552212"}
slang_dict['Chris'] = "14855221122"


query: str = input('Please input the name of the person you wish to search: ')
if query in slang_dict:
    print(query + "\'s number is " + slang_dict[query])
else:
    print("Sorry, I didn't find that.")
    print("Current count of dict is " + str(len(slang_dict)))
