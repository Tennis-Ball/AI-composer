import py_midicsv as pm


def data_format():
    # name = 'bwv'
    # number = 772
    # data = []
    # for i in range(30):
    #     name += str(number)
    #     name += '.mid'
    #     for _ in pm.midi_to_csv(name):
    #         data.append(_)
    #
    #     number += 1
    #     name = 'bwv'
    data = pm.midi_to_csv('mozk281a.mid')

    for i in pm.midi_to_csv('mozk281b.mid'):
        data.append(i)

    for i in pm.midi_to_csv('mozk281c.mid'):
        data.append(i)

    return data
