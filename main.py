from kivy.app import App
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class PragyaCallsApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15)
        )

        root.add_widget(Label(
            text="[b]PRAGYA CALLS[/b]",
            markup=True,
            font_size=sp(28),
            size_hint_y=None,
            height=dp(65)
        ))

        root.add_widget(Label(
            text="Universal Calling",
            font_size=sp(16),
            size_hint_y=None,
            height=dp(30)
        ))

        self.phone = TextInput(
            hint_text="Enter mobile number",
            multiline=False,
            input_filter="int",
            font_size=sp(18),
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.phone)

        sim = Button(
            text="PHONE CALL  |  SIM NETWORK",
            font_size=sp(17),
            size_hint_y=None,
            height=dp(60)
        )
        sim.bind(on_release=self.sim_call)
        root.add_widget(sim)

        internet = Button(
            text="INTERNET VOICE / VIDEO CALL",
            font_size=sp(17),
            size_hint_y=None,
            height=dp(60)
        )
        internet.bind(on_release=lambda x: self.info(
            "Internet Calling",
            "Internet voice and video calling module is not connected yet."
        ))
        root.add_widget(internet)

        offline = Button(
            text="OFFLINE NEARBY CALLING",
            font_size=sp(17),
            size_hint_y=None,
            height=dp(60)
        )
        offline.bind(on_release=lambda x: self.info(
            "Offline Nearby Calling",
            "Wi-Fi Direct connection and nearby device discovery will be added next."
        ))
        root.add_widget(offline)

        root.add_widget(Label(
            text="Secure Communication • PragyaCalls",
            font_size=sp(12)
        ))

        return root

    def info(self, title, message):
        Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.85, 0.35)
        ).open()

    def sim_call(self, instance):
        number = self.phone.text.strip()

        if not number:
            self.info("Phone Call", "Please enter a phone number.")
            return

        try:
            from jnius import autoclass
            Intent = autoclass("android.content.Intent")
            Uri = autoclass("android.net.Uri")
            PythonActivity = autoclass("org.kivy.android.PythonActivity")

            intent = Intent(
                Intent.ACTION_DIAL,
                Uri.parse("tel:" + number)
            )
            PythonActivity.mActivity.startActivity(intent)

        except Exception as error:
            self.info("SIM Calling", "Android dialer could not be opened.")

if __name__ == "__main__":
    PragyaCallsApp().run()
