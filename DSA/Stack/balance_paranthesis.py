
def check_match(a, b):
    # checking for the right order of opening and closing paranthesis
    if (a =='(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']'):
        return True
    else:
        return False





def check_balance(exper):
    stack = []
    for x in exper:
        # appending paranthesis in the stack (implementation of list)
        if x in ('(','{','['):
            stack.append(x)
        else:
            # if stack is empty return fasle
            if not stack:
                return False
            # if check_match func. return False then return false
            elif check_match(stack[-1], x) == False:
                return False
            else:
            # otherwise pop the last item
                stack.pop()
            # and continue the process for the rest of expression
            
    if stack:
        return False
    else:
        return True
    # time complexity: bigO(n)

string = ')(())'
print(check_balance(string))