def data_parse(raw_midi):
    temp = []
    to_remove = []

    for i in range(len(raw_midi)):
        temp.append(raw_midi[i].split(', '))

    for i in range(len(temp)):
        if temp[i][2] != 'Note_on_c':
            to_remove.append(temp[i])
    
    for i in to_remove:
        temp.remove(i)

    to_remove.clear()
    
    for i in temp:
        i.remove(i[0])
        i.remove(i[1])
        i.remove(i[1])

    for i in range(len(temp)):    # Splits time
        if i == len(temp) - 1:
            temp[i][0] = temp[i - 1][0]
        else:
            if (str(int(temp[i + 1][0]) - int(temp[i][0])))[0] == '-':
                to_remove.append(temp[i])
            temp[i][0] = str(int(temp[i + 1][0]) - int(temp[i][0]))

    for i in range(len(temp)):  # adds chords
        if i == len(temp) - 1:
            break
        if temp[i + 1][0] == '0':
            temp[i].append(temp[i + 1][1])
            to_remove.append(temp[i + 1])

    for i in to_remove:
        temp.remove(i)

    for i in range(len(temp)):
        if len(temp[i]) == 4:
            temp[i].pop()

    for i in range(len(temp)):
        for _ in range(3):
            temp[i][_] = int(temp[i][_])

    for i in temp:
        print(i)

    return temp
