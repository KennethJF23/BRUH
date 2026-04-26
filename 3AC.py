def precedence(op):
    return {"^":3,"*":2,"/":2,"+":1,"-":1}.get(op,0)

def infix_to_postfix(expr):
    stack,postfix = [],[]
    for ch in expr:
        if ch.isalnum():
            postfix.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1]!='(':
                postfix.append(stack.pop())
                stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix.append(stack.pop())
            stack.append(ch)
    while stack:
        postfix.append(stack.pop())
    return postfix

def generate_3ac(postfix,lhs):
    stack,code,temp_no = [],[],1
    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            right,left = stack.pop(),stack.pop()
            temp = f"t{temp_no}"
            code.append((token,left,right,temp))
            stack.append(temp)
            temp_no +=1
    code.append(("=",stack.pop(),"-",lhs))
    return code


stmnt = input("Enter your expression:").replace(" ","")
lhs,rhs = (stmnt.split("=") if "=" in stmnt else("result",stmnt))
postfix = infix_to_postfix(rhs)
code = generate_3ac(postfix,lhs)

print("\nThree Address Code:")
for op, a1, a2, res in code:
    print(f"{res} = {a1}" if op == "=" else f"{res} = {a1} {op} {a2}")
    
print("\nTriples:")
print("{:<8}{:<8}{:<8}{:<8}".format("Index", "Op", "Arg1", "Arg2"))
for i, (op, a1, a2, res) in enumerate(code):
    print("{:<8}{:<8}{:<8}{:<8}".format(i, op, a1, a2))