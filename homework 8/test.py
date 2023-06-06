# class Trigon:
#
#     @classmethod
#     def valid_triangle(cls, args):
#         if not (
#                 args[0] < args[1] + args[2] and
#                 args[1] < args[0] + args[2] and
#                 args[2] < args[0] + args[1]
#         ):
#             raise Exception("Не треугольник")
#
#     @classmethod
#     def date_validation(cls, args):
#         if len(args) != 3:
#             print(len(args))
#             raise IndexError(f"Передано {len(args)} аргументов, а ожидается 3")
#         elif not all([isinstance(x, int) for x in args]):
#             raise TypeError('Стороны должны быть числами')
#         elif not all([x > 0 for x in args]):
#             raise ValueError('Стороны должны быть положительными')
#
#     def __init__(self, args):
#         try:
#             Trigon.date_validation(args)
#         except (IndexError, TypeError, ValueError) as e:
#             raise e
#         else:
#             Trigon.valid_triangle(args)
#
#
#
# pt = Trigon((3, 4, 5))
#
def f(*args):
    l = [x for x in args]
    print(len(l))

f(3, '7',)
