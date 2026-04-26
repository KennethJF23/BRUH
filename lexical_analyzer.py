def read_while(expr, pos, check):
    value = ""
    while pos < len(expr) and check(expr[pos]):
        value += expr[pos]
        pos += 1
    return value, pos


def analyze(expr):
    ids = {}
    tokens, rows, pos = [], [], 0

    while pos < len(expr):
        
        ch = expr[pos]

        if ch == " ":
            pos += 1
            continue

        if ch.isalpha():
            name, pos = read_while(expr, pos, lambda c: c.isalnum())
            if name not in ids:
                ids[name] = len(ids) + 1
            tokens.append(("ID", name))
            rows.append((name, f"<id,{ids[name]}>") )
            continue

        if ch.isdigit():
            num, pos = read_while(expr, pos, lambda c: c.isdigit())
            tokens.append(("NUM", num))
            rows.append((num, f"<{num}>"))
            continue

        tokens.append(("OP", ch))
        rows.append((ch, "<=>" if ch == "=" else f"<{ch}>"))
        pos += 1

    return tokens, rows


if __name__ == "__main__":
    expr = input("Enter an expression: ")
    tokens, rows = analyze(expr)
    print("lexeme   |   token")
    print("-------------------")
    for lexeme, token in rows:
        print(f"{lexeme:<8} | {token}")
