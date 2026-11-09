import os
os.environ["CFLAGS"] = "-I$PREFIX/include"
os.environ["LDFLAGS"] = "-L$PREFIX/lib"
print("Zlib environment paths set successfully!")
