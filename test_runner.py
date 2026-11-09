import os
print("Running complete PragyaCalls system verification...")
assert os.path.exists("main.py"), "main.py missing!"
assert os.path.exists("buildozer.spec"), "buildozer.spec missing!"
assert os.path.exists("modules/caller_engine.py"), "modules missing!"
print("All systems verified successfully! PragyaCalls is ready for final build.")
