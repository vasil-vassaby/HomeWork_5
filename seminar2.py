# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *.приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;

string = '2 + 2 * 5'
string = string.split()
print(string)

my_list = []
for i in range(len(string)):
    if string[i] == '*':
        res = int(string[i - 1]) * int(string[i + 1])

print(string)