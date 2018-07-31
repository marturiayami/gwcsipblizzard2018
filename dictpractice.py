peoples_ages = {
    'Sam':16,
    'Adrea':17,
    'Alejandro':17,
    'Evelyn':16,
    'Sidney':17,
    'Gabbody':17,
    'Lauren':17,
    'Makaria':19,
    'Aletheia':20
}

age_list = list(peoples_ages.values())


for keys,values in peoples_ages.items():
    print(keys)
    print(values)


final_average = sum(age_list)/float(len(age_list)-1)
print(final_average)
