my_nums = [15, 81, 5, 17, 20, 21, 13]
i = 0 
count = 0
my_nums.sort(reverse=True)
for my_nums[i] in my_nums:

    if my_nums[i] % 5 == 0:
       count +=1
       print(f"{count} => {my_nums[i]}")
    i +=1
else:
    print("All Numbers Printed")





print("=" * 15)

#2

i = 1
for i in range(1, 21):
    if i in (6, 8, 12):
        continue
    print(str(i).zfill(2))

else:
    print("All Numbers Printed")





print("=" * 15)

#3
my_ranks = {
  'Math': 'A',  #100
  "Science": 'B', #80
  'Drawing': 'A',
  'Sports': 'C'  #40
}

print
for rank in my_ranks:
    if my_ranks[rank] == 'A':
        print(f"My Rank in {rank} is {my_ranks[rank]} And This Equal 100 Points")
    elif my_ranks[rank] == 'B':
        print(f"My Rank in {rank} is {my_ranks[rank]} And This Equal 80 Points")
    elif my_ranks[rank] == 'C':
        print(f"My Rank in {rank} is {my_ranks[rank]} And This Equal 40 Points")
else:
    print(f"the total is {100+80+40+100}")


print("=" * 15)

#4

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}



for key in students:      
    print("-" * 30)
    print(f"-- Student Name => {key}")
    print("-" * 30)

    total = 0

    for child_key in students[key]:
        grade = students[key][child_key]

        if grade == 'A':
            points = 100
        elif grade == 'B':
            points = 80
        elif grade == 'C':
            points = 40
        elif grade == 'D':
            points = 20
        else:
            points = 0

        total += points
        print(f"- {child_key} => {points} Points")

    print(f"Total Points For {key} Is {total}")





#using items() 

for student_name, subjects in students.items():
    print("-" * 30)
    print(f"-- Student Name => {student_name}")
    print("-" * 30)
    total = 0
    for subject, grade in subjects.items():
        if grade == "A":
            points = 100
        elif grade == "B":
            points = 80
        elif grade == "C":
            points = 40
        elif grade == "D":
            points = 20
        total += points
        print(f"- {subject} => {points} Points")
    print(f"Total Points For {student_name} Is {total}")
