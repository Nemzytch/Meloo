from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


comptes = {'I Got Candies': ['qVRfO3191','ZZrot34**'], 'Riot Squad': ['uplivingterror','RCjBVii2I2'],'SnowballtheMid': ['d3We3','core9@maildrop.cc'],'Big Male Fight Top': ['nk047772911','R8w688JKlr']}

# print le nom d'utilisateur et le mode de passe du premier compte
utilisateur1 = comptes['I Got Candies'][0]
print(utilisateur1)
class SayHello(App):
    def aloha(self):
        print('aloha')
    def build(self):
        dropdown = DropDown()
        self.window = GridLayout(cols=2)
        self.window.add_widget(Image(source='yuumi.gif', anim_delay=0.05))
        self.window.add_widget(DropDown())
        for _ in comptes:
            
            btn = Button(text= _ , size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
            mainbutton = Button(text='Hello', size_hint=(None, None))
            mainbutton.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            
            
            
        runTouchApp(mainbutton)
        return self.window
        

if __name__ == "__main__":
    SayHello().run()