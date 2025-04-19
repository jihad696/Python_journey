print(bool(5))
print(bool([1, 2, 3]))
print(bool("Hello"))
print(bool({1, 2, 3}))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))

print("=" * 20)



html = 80
css = 60
javascript = 70
print(html >= 50 and css >= 50 and javascript >= 50)




print("=" * 20)

num_one = 10
num_two = 20
num = 20 

print(num > num_one or num > num_two)
# you can use bool 
# print(bool(num > num_one or num > num_two))


print(num > num_one and num > num_two)

print("=" * 20)

result = num_one + num_two
print(result)
print((result ** 3))
print((result ** 3) % 26000)  
print(((result ** 3) % 26000) / 5)
print(type(str(((result ** 3) % 26000) / 5)))


  