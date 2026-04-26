src = open("input.txt").read().splitlines()
# mnt: macro name -> start index in MDT
# mdt: macro body lines (stored one after another, each ending at MEND)
# ala: macro name -> list of formal parameters
mnt, mdt, ala = {}, [], {}

# Pass 1: build MNT, MDT, and ALA.
i = 0
while i < len(src):
    # Ignore non-macro lines in pass 1.
    if src[i] != "MACRO":
        i += 1
        continue

    # Header format: MACRONAME arg1 arg2 ...
    head = src[i + 1].split()
    name, formals = head[0], head[1:]
    # Save formal args and where this macro body starts inside MDT.
    ala[name], mnt[name] = formals, len(mdt)

    # Move to first body line and copy lines until MEND.
    i += 2
    while src[i] != "MEND":
        mdt.append(src[i]); i += 1
    # Keep MEND as a sentinel to know where expansion stops.
    mdt.append("MEND"); i += 1

print("MNT:", mnt)
print("MDT:", *mdt, sep="\n")

# Pass 2: expand macro calls.
print("\nPASS 2 OUTPUT")
for line in src:
    tok = line.split()
    # If first token is a macro name, expand it.
    if tok and tok[0] in mnt:
        k, actuals = mnt[tok[0]], tok[1:]
        while mdt[k] != "MEND":
            out = mdt[k]
            # Replace formal args with actual args one by one.
            for f, a in zip(ala[tok[0]], actuals):
                out = out.replace(f, a)
            print(out); k += 1
    # Print normal source lines (skip macro definition internals).
    elif line not in ("MACRO", "MEND") and not line.startswith(("ADD", "SUB")):
        print(line)
