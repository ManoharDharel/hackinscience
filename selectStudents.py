my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]


def select_student(students, threshold):
    accepted = []
    refused = []
    for item in students:
        if item[1] >= threshold:
            accepted.append(item)
        else:
            refused.append(item)

    value_item = {"Accepted": sorted(accepted, key=lambda x: x[1], reverse=True),
                  "Refused": sorted(refused, key=lambda x: x[1])}
    return value_item


print(select_student(my_class, 20))
