import kivy
kivy.require('2.1.0')           #To know version "print(kivy.__version__)"

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image (To get img from .py file)

Builder.load_file('design.kv')
#Builder.load_string('''  {We can directly write our kv things here}   ''')

class MyLayouts(Widget):

    def submit_btn(self):
        #name = self.ids.name.text

        self.ids.lbl_name.text = f'Hi {self.ids.name.text}, Good Greetings!'
        self.name.text = ''

class DemoApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayouts()


if __name__ == '__main__':
    DemoApp().run()

