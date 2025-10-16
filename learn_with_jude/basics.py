# name = 'Ayomide'
# location = 'Here'

person = {
    'name': 'Ayomide',
    'age': '26',
    'color': 'chocalate',
    'attributes': ['mean', 'wicked']
}

# print(f"my name is {name}, i live {location} ")
print(f"my name is {person['name']}, i'm {person["age"]} years old, i am very {person["attributes"][0]} ")
print(type(person['attributes']))
