arithmetic = ["+", "-", "*",  "/", "%", "**", "//"]
assignment = ['=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<=']
coomparision = ['==', '!=', '>', '<', '>=', '>=']
bitwise = ['&', '|', '^', '~', '<<', '>>']
all = ['+', '-', '*',  '/', '%', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<=', '==', '!=', '>', '<', '>=', '>=', '&', '|', '^', '~', '<<', '>>' ]
# all.append(arithmetic)
# all.append(assignment)
# all.append(coomparision)
# all.append(bitwise)

user = input("Enter a operator: ")
for i in all: 
    if i == user: 
        print(f"{user} is a valid operator.")
    else: 
        pass
for j in arithmetic:
    if j == user:
        print("Type: Arithmetic Opeteator")
    else: 
        pass
for k in assignment: 
    if k == user:
         print("Type: Assignment Operator")
    else: pass

for l in coomparision: 
    if l == user:
        print("Type: Coomparision Operator")
    else: pass

for m in bitwise: 
    if m == user: 
        print("Type: Bitwise Operator")
    else: pass
