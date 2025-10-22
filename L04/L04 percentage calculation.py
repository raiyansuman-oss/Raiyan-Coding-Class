#take marks as input from user 
print("enter marks obtain in 3 subjects: ")

math = int(input("maths ; "))
english = int(input("english :"))
science = int(input("science: "))

#let's calculate the percentage of marks
sum = math + english + science
print("sum of math, english, and science: ",sum)

perc = (sum/300)*100

print(f"percentage Mark ={perc}")