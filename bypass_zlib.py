with open("buildozer.spec", "r") as f:
    lines = f.readlines()
new_lines = []
for line in lines:
    if "requirements =" in line:
        line = line.strip() + ",zlib\n"
    new_lines.append(line)
with open("buildozer.spec", "w") as f:
    f.writelines(new_lines)
print("Buildozer spec patched!")
