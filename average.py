num = int(input("How many numbers "))
sum = 0
for i in range(num):
    number =float(input("Enter any number ").strip())
    sum +=number
average = sum/num
print(f"average is {average} ")
