print("Enter your first number")
num1 = int(input())

print("Enter your second number")
num2 = int(input())

print("choose any operator +, ×, ÷,  %, - ")
operator = input()

if operator=="+" :
	ans = num1 + num2
	print(ans)
	

elif operator=="×" :
	ans1 = num1 * num2
	print(ans1)
	
	
elif operator=="÷" :
	ans2 = num1 / num2
	print(ans2)
	
	
elif operator=="%" :
	ans3 = num1 % num2
	print(ans3)
	
	
elif operator=="-" :
	ans4 = num2 - num1
	print(ans4)
