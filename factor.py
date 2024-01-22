# -------------5------------------
# n = int(input())
# i = 1
# sm = i * (i + 1) / 2
# while n >= sm:
#     i += 1
#     sm = i * (i + 1) / 2
# print(i - 1)

line = input()
alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
         'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(33):
    while alpha[i] in line:
        line.replace(alpha[i], "")
    # while alpha[i].upper() in line:
    #     line.replace(alpha[i].upper(), "")
    # while "  " in line:
    #     line.replace("  ", " ")
    print(f"{line} {chr(i)}")