import school_scores
list_of_record = school_scores.get_all()

for g in list_of_record:
    print(g['GPA'])
