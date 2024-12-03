def print_params(a=1,b='строка',c=True):
    print(f'a:{a},b:{b},c:{c}')

print_params()
print_params(5)
print_params(b=10)
print_params(c=[1,2,3])
print_params(4,7)

values_list=[7.62, 'exersise', False]
values_dict={'a':4,'b':'scringe','c':None}

print_params(*values_list)
print_params(**values_dict)

values_list_2=[None,'anoter']

print_params(*values_list_2,42)