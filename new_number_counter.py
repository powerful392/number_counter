list_of_number = []
few = int(input('چندتا عدد میخوای وارد کنی، به عدد وارد کن\n'))
for few1 in range(few):
    number = int(input('عدد رو وارد کن\n'))
    list_of_number.append(number)
convert_tuple = tuple(list_of_number)
result = sum(convert_tuple)
print(result)