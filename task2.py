#Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.


list_1 = [1, 2, 3, 4, 5,] 
k = 3
index_element = 0
min_element = abs(k - list_1[0])
for i in range(len(list_1)):
    buffer_element = abs(k -list_1[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(list_1[index_element])