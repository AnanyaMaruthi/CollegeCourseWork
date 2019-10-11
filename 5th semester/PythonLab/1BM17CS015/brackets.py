# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '' and '. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid 
# but "[)", "({)" and "{{{" are invalid.

def checkBrackets(expression):
    stack = []
    for bracket in expression:
        if bracket == "(" or bracket == "[" or bracket == "{":
            stack.append(bracket)
        elif bracket == ")" or bracket == "]" or bracket == "}":
            try:
                opening = stack.pop()
            except:
                print("Invalid")
                return
            if bracket == ")":
                if opening == "(":
                    continue
                else:
                    print("Invalid")
                    return
            elif bracket == "}":
                if opening == "{":
                    continue
                else:
                    print("Invalid")
                    return
            elif bracket == "]":
                if opening == "[":
                    continue
                else:
                    print("Invalid")
                    return
            else:
                print("Invalid")
                return
        else:
            print("Invalid")
            return
    if stack != []:
        print("Invalid")
        return
    print ("Valid")
    return

expression = input("Enter bracket expression")
checkBrackets(expression)
