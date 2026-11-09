with open("buildozer.spec", "r") as f:
    content = f.read()
if "source.dir" not in content:
    content = content.replace("[app]\n", "[app]\nsource.dir = .\n")
with open("buildozer.spec", "w") as f:
    f.write(content)
print("buildozer.spec updated successfully!")
