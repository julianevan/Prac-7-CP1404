from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
class ConvertMToKMApp(App):
    def build(self):
        """Build the kivy app"""
        Window.size = (500,250)
        self.title = "Convert Miles to Kilometers App"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root
    def raise_number(self,value):
        """To raise the number"""
        if value != "":
            value = int(value) + 1
        else:
            value = 1
        self.root.ids.input_miles.text = str(value)
    def lower_number(self,value):
        """To lower the number"""
        if value != "":
            value = int(value) - 1
        else:
            value = -1
        self.root.ids.input_miles.text = str(value)
    def convert(self,value):
        """To execute conversion"""
        try:
            kilometer = float(value) * 1.60934
            self.root.ids.result.text = str(kilometer)
        except ValueError:
            self.root.ids.result.text = "0.0"
ConvertMToKMApp().run()