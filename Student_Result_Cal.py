name = input("Student Name:")
sub1 = int(input("Subject 1 Marks: "))
sub2 = int(input("Subject 2 Marks: "))
sub3 = int(input("Subject 3 Marks: "))
total = sub1+sub2+sub3
average = total/3
percentage = (total/300) *100
print("\nStudent:", name)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)

if percentage>=35:
    print("Pass")
else:
    print("Fail")