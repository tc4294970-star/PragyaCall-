import os
print("Generating PragyaCalls UI layout...")
with open("main.py", "w") as f:
    f.write('''from kivy.app import App\nfrom kivy.uix.boxlayout import BoxLayout\nfrom kivy.uix.label import Label\n\nclass PragyaCallsApp(App):\n    def build(self):\n        return BoxLayout(orientation='vertical')\n\nif __name__ == '__main__':\n    PragyaCallsApp().run()\n''')
print("UI layout template generated!")
