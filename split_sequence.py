from numpy import asarray


def split_sequence(data):
    train = []
    output = []

    for i in range(len(data)):
        for _ in range(3):
            data[i][_] = (data[i][_] - 0) / (384 - 0)

        if i < len(data) - 1:
            train.append(data[i])

        if i != 0:
            output.append(data[i])

    return asarray(train), asarray([output])
