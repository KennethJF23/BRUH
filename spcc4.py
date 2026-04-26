import re

rules = [re.sub(r"\s+", "", r.strip()) for r in open("grammar.txt")]
terminals, firstT, lastT, table = set(), {}, {}, {}

# STEP 1: Extract terminals
for r in rules:
	for c in r.split("->")[1]:
		if not c.isupper() and c != "|":
			terminals.add(c)
terminals.add("$")

# Check Operator Precedence Grammar
if any(
	a.isupper() and b.isupper()
	for r in rules
	for a, b in zip(r.split("->")[1], r.split("->")[1][1:])
):
	print("Not Operator Precedence Grammar")
	exit()

print("Operator Precedence Grammar Confirmed")

# STEP 2: Compute FIRSTVT & LASTVT
for r in rules:
	firstT[r[0]], lastT[r[0]] = set(), set()

changed = True
while changed:
	changed = False
	for r in rules:
		A, rhs = r[0], r.split("->")[1]
		for prod in rhs.split("|"):
			f, l = prod[0], prod[-1]

			if not f.isupper():
				changed |= f not in firstT[A]
				firstT[A].add(f)
			else:
				changed |= not firstT[f] <= firstT[A]
				firstT[A] |= firstT[f]

			if len(prod) > 1 and not prod[1].isupper():
				firstT[A].add(prod[1])

			if not l.isupper():
				changed |= l not in lastT[A]
				lastT[A].add(l)
			else:
				changed |= not lastT[l] <= lastT[A]
				lastT[A] |= lastT[l]

			if len(prod) > 1 and not prod[-2].isupper():
				lastT[A].add(prod[-2])

# Operator Priority
priority = {"+": 1, "-": 1, "*": 2, "/": 3}


def prec(a, b):
	if a == "$" and b == "$":
		return "Accept"
	if a == "$":
		return "<"
	if b == "$":
		return ">"
	if a == "(" and b == ")":
		return "="
	if a == "(":
		return "<"
	if b == ")":
		return ">"
	if a.islower() and b.islower():
		return "-"
	if a.islower():
		return ">"
	if b.islower():
		return "<"
	if a in priority and b in priority:
		return ">" if priority[a] >= priority[b] else "<"
	return "E"


# Build Table
for a in terminals:
	table[a] = {b: prec(a, b) for b in terminals}

print("\nPrecedence Table:")
print("   ", " ".join(terminals))
for a in terminals:
	print(a, " ", " ".join(table[a][b] for b in terminals))

# STEP 3 & 4: Parsing
inp = input("\nEnter Input String: ") + "$"
stack = "$"
print("\nStack\tSign\tInput\tAction")


def match(stack, prod):
	if len(stack) < len(prod):
		return False
	s = stack[-len(prod) :]
	return all(
		(p.isupper() and c.isupper()) or (p == "i" and c.islower()) or (p == c)
		for p, c in zip(prod, s)
	)


while True:
	i = len(stack) - 1
	while stack[i].isupper():
		i -= 1

	top, nxt = stack[i], inp[0]
	if top == "$" and nxt == "$":
		print(stack, "\t ", "\t", inp, "\tAccept")
		break

	rel = table[top][nxt]
	action = "Shift" if rel in "<=" else "Reduce" if rel == ">" else "Error"
	print(stack, "\t", rel, "\t", inp, "\t", action)

	if action == "Error":
		break

	if action == "Shift":
		stack += nxt
		inp = inp[1:]
	else:
		reduced = False
		for r in rules:
			A, rhs = r.split("->")
			for prod in rhs.split("|"):
				if match(stack, prod):
					stack = stack[: -len(prod)] + A
					reduced = True
					break
			if reduced:
				break

		if not reduced:
			print("Reduction Error")
			break