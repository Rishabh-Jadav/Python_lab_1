print("Enter Marks Obtained in 5 Subjects: ")
sub1 = int(input("Python: "))
sub2 = int(input("J2EE : "))
sub3 = int(input("Cyber Security : "))
sub4 = int(input("C#: " ))
sub5 = int(input("HTML:"))

if sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100:
    print("Invalid marks")
    exit()
    
total = "Total marks : 500"
print(total)
tot= sub1+sub2+sub3+sub4+sub5
avg = tot/5

print("Obtained marks: ",int(tot))

print("Percentage : ",avg,"%")

if sub1<33 or sub2<33 or sub3<33 or sub4<33 or sub5<33:
    print("You're FAIL!")
else:
    print("You're PASS")

if avg >= 90 and avg <= 100:
    print("Your Grade is A")
elif avg >= 70 and avg < 90:
    print("Your Grade is B")
elif avg >= 50 and avg < 70:
    print("Your Grade is C")
elif avg >= 33 and avg < 50:
    print("Your Grade is D")

    
    
    
    
    
    
    
    
    