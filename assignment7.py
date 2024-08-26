#first step
name=input("Enter your name :")
print(name)
#second step
number= []
number.append(int(input("Enter your first favourite number :")))
number.append(int(input("Enter your Second favourite number :")))
number.append(int(input("Enter your Third favourite number :")))
#third step        
even_odd = []
for num in number:
    if num % 2 == 0:
        even_odd.append((num,"even"))
    else:
        even_odd.append((num,"odd"))
for evenodd in even_odd:
 print(f"\nthe number is {evenodd}")        
     
#fourth step
print(f"\nHere are your number than square ")
for num in number:
    square = num * num
    print(f"the square of {num} is :{square}")
#fifth step
sum = number[0] + number[1] + number[2]
print(f"\nthe sum of three favourite numbers is :{sum}")
print(f"great job , {name}! number are fascinating aren't they?")
#sixth step
print(f"\nWow, {sum} is a prime number")
