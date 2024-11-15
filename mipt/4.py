n = int(input())
data = input().split(' ')
num = []
print(data)

for el in data:
    if el[0] == "N":
        if el[-1] == "E":
            num.append(int(el[1:-1]))
        else:
            num.append(360 - int(el[1:-1]))
    elif el[0] == "E":
        if el[-1] == "S":
            num.append(90 + int(el[1:-1]))
        else:
            if int(el[1:-1]) <= 90:
                num.append(90 - int(el[1:-1]))
            else:
                num.append(450 - int(el[1:-1]))
    elif el[0] == "S":
        if el[-1] == "W":
            num.append(180 + int(el[1:-1]))
        else:
            num.append(180 - int(el[1:-1]))
    else:
        if el[-1] == "N":
            num.append(270 + int(el[1:-1]))
        else:
            num.append(270 - int(el[1:-1]))

print(num)