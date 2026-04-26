import re

expr_map, copy_map, const_map, optimized = {}, {}, {}, []
is_temp = lambda x: re.fullmatch(r"T\d+", x)
is_arith = lambda x: re.fullmatch(r"[0-9+\-*/ ]+", x)

for line in open("input.txt"):
    line = line.strip()  # Remove extra spaces/newline.

    if not line or line.startswith("//"):  # Skip empty/comment lines.
        continue

    left, right = map(str.strip, line.split("="))  # Parse: left = right

    if is_arith(right):  # Constant folding for numeric-only expressions.
        right = str(eval(right))
        const_map[left] = right

    for old, new in copy_map.items():  # Copy propagation.
        right = right.replace(old, new)

    if is_temp(right):  # Save simple temp copy and skip emit.
        copy_map[left] = right; continue
    
    for expr, var in expr_map.items():  # Common subexpression elimination.
        right = right.replace(expr, var)
        
    expr_map[right] = left
    optimized.append([left, right])

final, copies = [], {}
for left, right in optimized:
    if is_temp(right):  # Remove leftover temp assignments.
        copies[left] = right; continue
    for old, new in copies.items():
        right = right.replace(old, new)
    for old, new in const_map.items():  # Constant propagation.
        right = right.replace(old, new)
    final.append([left, right])

print("Optimized Code:")
for left, right in final:
    print(f"{left}={right}")
