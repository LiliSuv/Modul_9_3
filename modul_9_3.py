first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs (len (y[1]) - len (y[0])) for y in zip (first, second) if len (y[0]) != len (y[1]))
x = first + second
second_result = ( len (x[i]) == len (x[len (first) + i])  for i in range (len (first)))

print (list (first_result))
print (list (second_result))
