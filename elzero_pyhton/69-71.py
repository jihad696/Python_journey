values = (0, 1, 2)

if any(values): # true cuz at least one var is true

    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] #the condition is true so my_var = 0 


if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]): #True or True or True all are true 

    print("Good")

else:

    print("Bad")

#==============================================
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820
#==============================================
n = 21

l = list(range(n)) #[1,2,3,..,20]

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9): #sum(1..20)/21

  print("Good")

