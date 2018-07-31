#Make and empty dictionary
import json
data = []
#Make a dictionary holding the questions
questions = ['What is your name? ', 'How old are you? ', 'What is your date of birth? ', 'Where do you live? ', 'What is your favorite color? ', 'What is your favorite animal? ', 'What is your favorite book? ']
#Make a loop asking the questions
    #takes inputs and saves to dictionary
cont = True
while cont:
    answers1 = {}
    for q in questions:
        answers1[q] = input(q)
    data.append(answers1)
    next_response = input('''Congratulations you have finished the survey!
    Is there another person that would like to take the survey? Y/N ''')
    if next_response == 'Y':
        cont = True
    else:
        cont = False

if os.path.isfile("data.json"):
    file = open("data.json", "r+")
    old_data = json.load(file)
    old_data.extend(data)
    file.write(json.dumps(old_data))
    file.close()
else:
    f = open("data.json", "w")
    jsons_obj = json.dumps(data)
    f.write(jsons_obj)
    f.close()
