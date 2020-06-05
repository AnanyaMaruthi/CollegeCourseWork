# Implement unification in first order logic
# Use small letters for variables and capital letters for constants in the expression
import re

def getAttributes(expression):
    # expression - Like(g(x), y) ; Attributes - g(x), y
    expression = expression.split("(")[1:]
    expression = "(".join(expression)
    expression = expression[:-1]
    # expression = g(x),y
    # split at commma only when not surrounded by ()
    expression = re.split("(?<!\(.),(?!.\))", expression)
    return expression

def getInitialPredicate(expression):
    # expression - Like(x, y) ; Predicate - Like
    return expression.split("(")[0]

def isConstant(char):
    return char.isupper() and len(char) == 1

def isVariable(char):
    return char.islower() and len(char) == 1

def replaceAttributes(exp, old, new):
    attributes = getAttributes(exp)
    for index, val in enumerate(attributes):
        if val == old:
            attributes[index] = new
    predicate = getInitialPredicate(exp)
    return predicate + "(" + ",".join(attributes) + ")"

def apply(exp, substitutions):
    for substitution in substitutions:
        new, old = substitution  # substitution is a tuple of 2 values (new, old)
        exp = replaceAttributes(exp, old, new)
    return exp

def checkOccurs(var, exp):
    # checks if variable occurs in expression
    if exp.find(var) == -1:
        return False
    return True

def getFirstPart(expression):
    attributes = getAttributes(expression)
    return attributes[0]

def getRemainingPart(expression):
    predicate = getInitialPredicate(expression)
    attributes = getAttributes(expression)
    newExpression = predicate + "(" + ",".join(attributes[1:]) + ")"
    return newExpression

def unify(exp1, exp2):
    if exp1 == exp2:
        return []

    if isConstant(exp1) and isConstant(exp2):
        if exp1 != exp2:
            return False

    if isConstant(exp1):
        return [(exp1, exp2)]

    if isConstant(exp2):
        return [(exp2, exp1)]

    if isVariable(exp1):
        if checkOccurs(exp1, exp2):
            return False
        else:
            return [(exp2, exp1)]

    if isVariable(exp2):
        if checkOccurs(exp2, exp1):
            return False
        else:
            return [(exp1, exp2)]

    # Check if initial predicate matches
    if getInitialPredicate(exp1) != getInitialPredicate(exp2):
        print("Predicates do not match. Cannot be unified")
        return False

    attributeCount1 = len(getAttributes(exp1))
    attributeCount2 = len(getAttributes(exp2))
    if attributeCount1 != attributeCount2:
        return False

    head1 = getFirstPart(exp1)
    head2 = getFirstPart(exp2)
    initialSubstitution = unify(head1, head2)
    if initialSubstitution == False:
        return False
    if attributeCount1 == 1:
        return initialSubstitution

    tail1 = getRemainingPart(exp1)
    tail2 = getRemainingPart(exp2)

    if initialSubstitution != []:
        tail1 = apply(tail1, initialSubstitution)
        tail2 = apply(tail2, initialSubstitution)

    remainingSubstitution = unify(tail1, tail2)
    if remainingSubstitution == False:
        return False

    initialSubstitution.extend(remainingSubstitution)
    return initialSubstitution


exp1 = "hate(f(y),z)"
exp2 = "hate(M,f(y))"
print("Original Expressions: ")
print(exp1)
print(exp2)
substitutions = unify(exp1, exp2)
print("Substitutions:")
print(substitutions)


# initialSubstitution = [(a,b)]
# a is substituted for b. replace b with a

