class ValidParentheses(object):
    def __init__(self):
        self.parentheses_match = {'(': ')', '[': ']', '{': '}'}

    def valid_parentheses(self, string):
        if string is None or len(string) == 0:
            return True
        stack = []
        for i in range(len(string)):
            if string[i] == '(' or string[i] == '[' or string[i] == '{':
                stack.append(string[i])
            else:
                top_parentheses = stack.pop()
                top_parentheses_match = self.parentheses_match[top_parentheses]
                if top_parentheses_match != string[i]:
                    return False
        return len(stack) == 0


def evaluate_reverse_polish_notation(tokens):
    if tokens is None or len(tokens) == 0:
        return 0
    stack = []
    for i in range(len(tokens)):
        if tokens[i].isdigit():
            stack.append(tokens[i])
        else:
            num_1 = stack.pop()
            num_2 = stack.pop()
            if tokens[i] == "+":
                stack.append(num_1 + num_2)
            elif tokens[i] == "-":
                stack.append(num_1 - num_2)
            elif tokens[i] == '*':
                stack.append(num_1 * num_2)
            else:
                stack.append(num_1 // num_2)
    return stack.pop()


