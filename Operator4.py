arithmetic = ["+", "-", "**",  "//", "%", "*", "/"]
assignment = ['=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<=']
coomparision = ['==', '!=', '>', '<', '>=', '>=']
bitwise = ['&', '|', '^', '~', '<<', '>>']
all = ['+', '-', '*',  '/', '%', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<=', '==', '!=', '>', '<', '>=', '>=', '&', '|', '^', '~', '<<', '>>' ]
keyword = ["range", "False", "for", "while", "in", "None", "True", ]
token = ["sum", "div" ]

user = input("Input:  ")

for i in all:
    if i == user: 
        print(f"{user} is a valid operator.")
    else: 
        pass


print("--------------------------------------------------------------------------------------")
print("|          Operator          |         Type          |         Valid/Invalid         |")
print("--------------------------------------------------------------------------------------")

for users in user: 
    if users in keyword: 
        print(f"|             {users}             |         Keyword         |             Valid             |" + "\n--------------------------------------------------------------------------------------")
    elif users in arithmetic: 
        print(f"|              {users}             |         arithmetic    |            Valid              |" + "\n--------------------------------------------------------------------------------------")
    elif users in assignment: 
        print(f"|              {users}             |         assignment    |             Valid             |" + "\n--------------------------------------------------------------------------------------")
    elif users in coomparision: 
        print(f"|             {users}             |      Coomparision     |             Valid             |" + "\n--------------------------------------------------------------------------------------")
    elif users in bitwise: 
        print(f"|             {users}             |         Bitwise         |            Valid              |" + "\n--------------------------------------------------------------------------------------")
    elif users in token: 
        print(f"|             {users}             |          Token          |             Valid             |" + "\n--------------------------------------------------------------------------------------")
    