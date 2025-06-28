subject1 = int(input("Enter 5 grades you got: "))
subject2 = int(input())
subject3 = int(input())
subject4 = int(input())
subject5 = int(input())
total = subject1 + subject2 + subject3 + subject4 + subject5
average = total/5

print(average)

if average>=97 and average <=100:
    print("A+")
elif average >=93 and average < 97:
    print("A")
elif average >=90 and average < 93:
    print("A-")
elif average >=87 and average < 90:
    print("B+")
elif average >= 83 and average < 87:
    print("B")
elif average >= 80 and average < 83:
    print("B-")
else:
    print("C or below")