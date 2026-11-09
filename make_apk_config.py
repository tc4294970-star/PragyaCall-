import os
print("Configuring Android APK build rules for PragyaCalls...")
with open("buildozer.spec", "w") as f:
    f.write('''[app]\ntitle = PragyaCalls\npackage.name = pragyacalls\npackage.domain = org.pragya.calls\nsource.include_exts = py,png,jpg,kv,atlas\nversion = 1.0\nrequirements = python3,kivy\nandroid.permissions = READ_PHONE_STATE,READ_CALL_LOG,READ_CONTACTS,INTERNET,ACCESS_FINE_LOCATION\nandroid.api = 34\nandroid.minapi = 21\n''')
print("Buildozer spec generated successfully!")
