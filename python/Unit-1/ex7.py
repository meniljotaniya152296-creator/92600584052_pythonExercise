# write a python program to demonstrate and demonstrate dictionary methods and iteration.

a_dict = {'namne':'menil' , 'age' : 7, 'class' : 'first'}

print(a_dict)

print("length" , len(a_dict))

a_dict.update({'city':"Rajkot"})
print("UpDated Dict ", a_dict)

del a_dict['city']
print("delete city", a_dict)

b_dict = a_dict.copy()
print("new Disc : ", b_dict)
