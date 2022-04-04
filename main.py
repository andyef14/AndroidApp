from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class AndroidApp(MDApp):
    def build(self):
        return MDLabel(text = "Hello, Android App!", halign = "center")

AndroidApp().run()
