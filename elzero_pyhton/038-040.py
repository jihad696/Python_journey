




name = input("enter your name").strip().capitalize()
print("Hello {}, Happy To See You Here.".format(name))

print ("=" * 30)

age = int(input())

if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
elif age >= 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


print ("=" * 30)


first_name = input().strip().capitalize()
second_name = input().strip().capitalize()

print(f"Hello {first_name} {second_name[0]}.")


print ("=" * 30)

email = input().strip().lower()
print("Your Name Is", email[:email.index("@")])
print("Email Service Provider Is",email[email.index("@")+1:email.index(".")])
print("Top Level Domain Is", email[email.index(".") + 1:])

