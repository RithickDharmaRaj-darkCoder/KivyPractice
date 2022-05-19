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

    selected_lang = []
    def checkbox_click(self, instance, click_status, lang):
        if click_status == True:
            MyLayouts.selected_lang.append(lang)
            self.ids.output_label.text = f'{MyLayouts.selected_lang}'
        else:
            MyLayouts.selected_lang.remove(lang)
            self.ids.output_label.text = f'{MyLayouts.selected_lang}'


class DemoApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayouts()


if __name__ == '__main__':
    DemoApp().run()

