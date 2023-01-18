# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


data = [1, 2, 3, 5, 1, 5, 3, 10]
new_data = [x for x in data if data.count(x) == 1]
print(new_data)


#my_dict = dict()

# for i in range(len(data)):
#         my_dict[data[i]] = my_dict.get(data[i], 0) + 1
# print(my_dict)

#new_data = [x[0] for x in my_dict.items() if x[1] == 1]

#new_data = list(filter(lambda x: data.count(x) == 1, data))