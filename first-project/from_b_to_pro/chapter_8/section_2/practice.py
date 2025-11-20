# 8.3
def make_shirt(size, text_content):
    print(
        f'We will make a shirt which size is {size}, and it has a logo with "{text_content}".'
    )


make_shirt("M", "Impossible is Nothing!")
make_shirt(text_content="To be NO.1", size="XL")

print("###########################################")


# 8.4
def make_shirt_modified(size="L", text_content="I love Python"):
    print(
        f'We will make a shirt which size is {size}, and it has a logo with "{text_content}".'
    )


make_shirt_modified()
make_shirt_modified("M")
make_shirt_modified(text_content="I can play")

print("###########################################")


# 8.5 非默认形参在前，默认形参在后
def describe_city(city, country="China"):
    print(f"{city} is in {country}")


describe_city("Suzhou")
describe_city("Bejing")
describe_city("Chicago", "United States")
