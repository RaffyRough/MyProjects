# Program to solve factorisation and expansion
# 2 helper functions will need to be created: HCF and LCM
# 3x
cache = {}
def LCM(x, y):
    lcm = None
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


# HCF function created to be a helper function of my algebraic factorisation function
def HCF(x, y):
    hcf = None
    # 1st find out which number is less
    if x < y:
        lower = x
    else:
        lower = y
    # loop thru all nums from 1 to lower and modulus x and y by them
    # if a number satisfies both then return that num
    for i in range(1, lower +1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    if hcf == 1:
        return 'There are no common factors'
    return hcf



# Expansion function. Assumptions currently are: there are only single digits and oper will be a "+" sign
# Solutions to edge cases and correct use of operator sign if it is a "-" to be done
def expandEquation(expr_1, oper, expr_2):
    ''':arg expr_1: str
       :arg expr_2: str
        expr_1 and expr_2 will be an equation -> 3(3x + 2y)
       :arg oper : str that will decide how
       :return: an expanded version of the two expressions in a str format'''

    # Create the left and right side of the equation to be returned and initialise as None
    left_side = None
    right_side = None
    mult_1, mult_2 = expr_1[0], expr_2[0]
    expr_1_1st_digit, expr_1_2nd_digit = expr_1[2], expr_1[5]
    expr_2_1st_digit, expr_2_2nd_digit = expr_2[2], expr_2[5]
    oper_1, oper_2 = expr_1[4], expr_2[4]
    expr_1_1stLetter, expr_1_2ndLetter = expr_1[3], expr_1[6]
    expr_2_1stLetter, expr_2_2ndLetter = expr_2[3], expr_2[6]

    # do 1st expansion by multiplying digits by multipliers
    expr_1_1st_digit, expr_1_2nd_digit = int(expr_1_1st_digit) * int(mult_1), int(expr_1_2nd_digit) * int(mult_1)
    expr_2_1st_digit, expr_2_2nd_digit = int(expr_2_1st_digit) * int(mult_2), int(expr_2_2nd_digit) * int(mult_2)

    # conciliate similar elements to one side each
    # 1st the left side
    if expr_1_1stLetter == expr_2_1stLetter and oper == '+':
        left_side = expr_1_1st_digit + expr_2_1st_digit
    elif expr_1_1stLetter == expr_2_1stLetter and oper == '-':
        left_side = expr_1_1st_digit - expr_2_1st_digit

    # then the right
    if expr_1_2ndLetter == expr_2_2ndLetter and oper == '+':
        right_side = expr_2_2nd_digit + expr_1_2nd_digit
    elif expr_1_2ndLetter == expr_2_2ndLetter and oper == '-':
        right_side = expr_1_2nd_digit - expr_2_2nd_digit

    # now combine the two sides and return
    return ('The answer is '+ str(left_side)+ expr_1_1stLetter + ' ' + oper +' '+ str(right_side) + expr_2_2ndLetter)

def factoriseEquation(equation):
    # sample equation: '6x + 24'
    oper = equation[3]
    letter = equation[1]
    factor = 0
    result_int = 0
    first_int, second_int = 0, 0
    first_flag = False
    try:
        first_int = int(equation[0] + equation[1])
        first_flag = True
    except ValueError:
        first_int = int(equation[0])
        first_flag = False

    if first_flag == False:
        try:
            second_int = int(equation[5] + equation[6])
        except ValueError:
            second_int = int(equation[5])

    elif first_flag == True:
        oper = equation[4]
        letter = equation[2]
        try:
            second_int = int(equation[6] + equation[7])
        except ValueError:
            second_int = int(equation[6])

    factor = HCF(second_int, first_int)
    result_int = int(second_int / factor)

    result = ('The answer is: ' + str(factor) + '(' + letter + ' ' + oper + ' ' + str(result_int) + ')')
    return result




e1 = '3(6x+2y)'
e2 = '2(4x+2y)'
e_oper = '+'
#print(expandEquation(e1,e_oper,e2))
e_3 = '16x + 24y'
print(factoriseEquation(e_3))


