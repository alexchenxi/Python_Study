# 6.4
coding_terms = {"range": "序列", "list": "列表", "print": "打印"}

coding_terms['dictionary'] = '字典'
coding_terms['set'] = '集合'

for term, expression in coding_terms.items():
    print(f"{term}: {expression}")

print("##################################")

# 6.5
rivers = {'nile': 'egypt', 'Yangtze': "china", 'amazon': 'Brazil'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

inited_persons=['jen', 'sarah', 'alex','kevin']
for person in sorted(inited_persons):
    if person in favorite_languages:
        print(f"Thank you for your work {person.title()}!")
    else:
        print(f"Please take our survey {person.title()}.")
