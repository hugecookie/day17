def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    return False


def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is EMPTY~")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp

def check_bracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    return is_stack_empty()


SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


if __name__ == "__main__":
    expression_array = ['(2*[A+B)]', '(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expression in expression_array:
        top = -1
        print(expression, ' : ', check_bracket(expression))
