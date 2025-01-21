s = .5
m  = 1
l = 1.25
xl = 2.25

s1 = int(input("Enter the number of small sandwiches: "))
m1 = int(input("Enter the number of medium sandwiches: "))
l1 = int(input("Enter the number of large sandwiches: "))
xl1 = int(input("Enter the number of extra-large sandwiches: "))

summ = s1*s+m1*m+l1*l+xl1*xl
seconds = int((summ % 1)*60)
minutes = int(summ)

print(f"\nYou've entered {s1} small sandwiches.")
print(f"You've entered {m1} medium sandwiches.")
print(f"You've entered {l1} large sandwiches.")
print(f"You've entered {xl1} extra-large sandwiches.\n")

print(f"Total cooking time is {minutes} minutes and {seconds} seconds.")
