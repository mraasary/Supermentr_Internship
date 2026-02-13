name=input("Enter your name: ")
age=int(input("Enter your age: "))
hobby=input("Enter your hobby: ")

if age<13:
    category="Child"
elif age<20:
    category="Teenager"
elif age<60:
    category="Adult"
else:
    category="Senior"
    
print(f"Hello {name}! You are categorized as a {category} and your hobby is {hobby}.")