def precedence(op):
    return {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}.get(op, 0)


def infix_to_postfix(expr):
    # Step 1: convert infix expression to postfix using operator stack.
    stack, postfix = [], []
    for ch in expr:
        if ch.isalnum():
            postfix.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix.append(stack.pop())
            stack.append(ch)
    while stack:
        postfix.append(stack.pop())
    return postfix


def generate_3ac(postfix, lhs):
    # Step 2: build three-address code from postfix expression.
    stack, code, temp_no = [], [], 1
    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            right, left = stack.pop(), stack.pop()
            temp = f"t{temp_no}"
            code.append((token, left, right, temp))
            stack.append(temp)
            temp_no += 1
    code.append(("=", stack.pop(), "-", lhs))
    return code


stmt = input("Enter expression: ").replace(" ", "")
lhs, rhs = (stmt.split("=") if "=" in stmt else ("result", stmt))
postfix = infix_to_postfix(rhs)
code = generate_3ac(postfix, lhs)

# Step 3: print required practical formats.
print("\nThree Address Code:")
for op, a1, a2, res in code:
    print(f"{res} = {a1}" if op == "=" else f"{res} = {a1} {op} {a2}")

print("\nQuadruples:")
print("{:<8}{:<8}{:<8}{:<8}{:<8}".format("Index", "Op", "Arg1", "Arg2", "Result"))
for i, (op, a1, a2, res) in enumerate(code):
    print("{:<8}{:<8}{:<8}{:<8}{:<8}".format(i, op, a1, a2, res))

print("\nTriples:")
print("{:<8}{:<8}{:<8}{:<8}".format("Index", "Op", "Arg1", "Arg2"))
for i, (op, a1, a2, res) in enumerate(code):
    print("{:<8}{:<8}{:<8}{:<8}".format(i, op, a1, a2))

