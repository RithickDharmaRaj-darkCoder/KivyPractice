import kivy
kivy.require('2.1.0')           #To know version "print(kivy.__version__)"

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('practice1.kv')
#Builder.load_string('''  {We can directly write our kv things here}   ''')

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    roll = ObjectProperty(None)
    reign = ObjectProperty(None)
    output = ObjectProperty(None)

    def press(self):
        name = self.name.text
        rollno = self.roll.text
        regno = self.reign.text
#        result = self.output.text

        print(f"Hi {name}, your roll number is {rollno} and ur register number is {regno}")
        self.output.text = f"Hi {name}, your roll number is {rollno} and ur register number is {regno}"
        self.name.text = ''
        self.roll.text = ''
        self.reign.text = ''

class Practice1App(App):
    def build(self):
        return MyGridLayout()



if __name__ == '__main__':
    Practice1App().run()

