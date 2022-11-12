# 1 - Напишите программу вычисления арифметического выражения заданного 
# строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# # Пример:
# # 1+2*3 => 7;
# # (1+2)*3 => 9;

# from decimal import Decimal

# def my_calc(expr):
#     # while '(' in expr:
#     #     pass

#     num = ''
#     oper = ''

#     for ch in expr:
#         if ch.isdigit() or ch == '.':
#             num += ch
#         elif ch == '-':
#             num += ' ' + ch
#         elif ch == ' ':
#             continue
#         else:
#             oper += ch
#             num += ' '
#     num, oper = list(map(Decimal, num.split())), list(oper)


#     def make_oper(sign:str):
#         sign_index = oper.index()
#         first_num = num[sign_index]
#         second_num = num[sign_index + 1]
#         if sign == '/':
#             if second_num == 0:
#                 print('You can not devide by zero')
#                 exit()
#             num[sign_index] = first_num / second_num
#         elif sign == '*':
#             num[sign_index] = first_num * second_num
#         else:
#             num[sign_index] = first_num + second_num
#         del num[sign_index+1]
#         del oper[sign_index]

#     for i in '/*+':
#         make_oper(i)

orig_expr = input('Enter the arithmetic expression without a spaces: ')
final_expr = eval(orig_expr)
print(final_expr)