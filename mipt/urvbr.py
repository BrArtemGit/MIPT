import statistics as st
import matplotlib.pyplot as plt
fig, ax = plt.subplots()


with open('input_10.txt', 'r') as file:
    file = ''.join(file.readlines()).split('\n')
    data = []
    for i in range(len(file)):
        data.append(int(file[i][:-2]))

    data.sort()
    data = [[0] * len(data), data]

    for i in range(len(data) - 1):
        plt.stairs(data[i + 1], baseline=data[i], fill=True)

    plt.show()
