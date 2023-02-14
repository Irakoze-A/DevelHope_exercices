my_list= [*range(5)] 

f = lambda x : x**2 if x%2==0 else x

result = [f(i) for i in my_list]

print(list(result))