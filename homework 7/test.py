# department = 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование'
# text = "".join(department)
# # count = sorted([text.count(letter) for letter in text], reverse=True)
# # print([6, 6, 6, 6, 5, 5, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# # print(count)
# # # print(set(text))
#
# for i in sorted(set(text), reverse=True):
#     print(i, end=" ")
# dot1 = (5, 5)
# dot2 = (3, 4)
# print(dot1 + dot2)

def segment(dot1, dot2):
    """Возвращает сумму всех координат"""
    try:
        return dot1[0] + dot1[1] + dot2[0] + dot2[1]
    except TypeError as t:
        return print(str(t), type(str(t)))
segment((2, 3), ('4', 5))