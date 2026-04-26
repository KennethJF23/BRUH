class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 2

    def parse(self):
        return Node("=", Node(self.tokens[0][1]), self.expr())

    def _chain(self, op, next_fn):
        node = next_fn()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] == op:
            self.pos += 1
            
            node = Node(op, node, next_fn())
        return node

    def expr(self):
        return self._chain("+", self.term)

    def term(self):
        return self._chain("*", self.factor)

    def factor(self):
        value = self.tokens[self.pos][1]
        self.pos += 1
        return Node(value)


def print_tree(root):
    print("\nSYNTAX TREE\n")
    print("        ", root.value)
    print("       / \\")
    print("      ", root.left.value, "  ", root.right.value)
    if root.right.left:
        print("           / \\")
        print("          ", root.right.left.value, " ", root.right.right.value)
        if root.right.left.left:
            print("         / \\")
            print("        ", root.right.left.left.value, " ", root.right.left.right.value)


def tokenize(expr):
    tokens, pos = [], 0
    while pos < len(expr):
        ch = expr[pos]
        if ch == " ":
            pos += 1
            continue
        if ch.isalpha():
            value = ""
            while pos < len(expr) and expr[pos].isalnum():
                value += expr[pos]
                pos += 1
            tokens.append(("ID", value))
            continue
        if ch.isdigit():
            value = ""
            while pos < len(expr) and expr[pos].isdigit():
                value += expr[pos]
                pos += 1
            tokens.append(("NUM", value))
            continue
        tokens.append(("OP", ch))
        pos += 1
    return tokens


if __name__ == "__main__":
    expr = input("Enter an expression: ")
    tokens = tokenize(expr)
    tree = SyntaxAnalyzer(tokens).parse()
    print_tree(tree)
