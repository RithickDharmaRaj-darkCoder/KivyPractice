import kivy
kivy.require('2.1.0')           #To know version "print(kivy.__version__)"

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('design.kv')
#Builder.load_string('''  {We can directly write our kv things here}   ''')

class MyLayouts(Widget):
   pass

class DemoApp(App):
    def build(self):
        return MyLayouts()



if __name__ == '__main__':
    DemoApp().run()

