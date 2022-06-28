class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        stack
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
    
#   Basic Calc
# Original Problem on Leetcode: Basic Calc


# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .   
#      def calculate(self, s: str) -> int:
#     stack = [] # store sign and operand of previous expressions
#     operand = 0
#     res = 0 # For the on-going result
#     POSITIVE, NEGATIVE = 1, -1
#     sign = POSITIVE # 1 means positive, -1 means negative  

#     for c in s:
#         if c.isdigit():
#             operand = (operand * 10) + int(c)

#         elif c == '+':
#             res += sign * operand # add previous expression
#             sign, operand = POSITIVE, 0

#         elif c == '-':
#             res += sign * operand
#             sign, operand = NEGATIVE, 0

#         elif c == '(':
#             stack.append(res)
#             stack.append(sign)

#             sign = POSITIVE
#             res = 0

#         elif c == ')':
#             res += sign * operand

#             res *= stack.pop() # stack pop 1, sign
#             res += stack.pop() # stack pop 2, operand

#             # Reset the operand
#             operand = 0

#     res += sign * operand
#     return res   

