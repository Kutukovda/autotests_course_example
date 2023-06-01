department = 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование'
text = "".join(department)
# count = sorted([text.count(letter) for letter in text], reverse=True)
# print([6, 6, 6, 6, 5, 5, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# print(count)
# # print(set(text))

for i in sorted(set(text), reverse=True):
    print(i, end=" ")
