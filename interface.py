import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
import pyautogui
import time
import win32api
import win32con
from kivy.core.window import Window


Account = {'I GOT CANDIES': ['qVRfO3191','ZZrot34**'], 'ELON MUSK BANGER': ['uplivingterror','RCjBVii2I2'],'SNOWBALL THE MID': ['d3We3','core9@maildrop.cc']}

class Melo(App):
    def build(self):
        Window.size = (400, 200)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        
        #image widget
        self.window.add_widget(Image(source='yuumi.gif'))
        
        #label widget
        self.grettings = Label(text='What do you want Bro?', font_size = 18, color='#00FFCE')
        self.window.add_widget(self.grettings)
        
        #scrollable text input widget
        
        Account = {'I GOT CANDIES': ['qVRfO3191','ZZrot34**'], 'ELON MUSK BANGER': ['uplivingterror','RCjBVii2I2'],'SNOWBALL THE MID': ['d3We3','pasword']}
        self.switcher = Spinner(text='Compte',values=Account)
        self.window.add_widget(self.switcher)
        
        #button widget
        self.button = Button(text='Lets goooooo!', size_hint=(0.5,0.5), bold=True, background_color= '#00FFCE', on_press=self.callback)
        self.window.add_widget(self.button)
        
        return self.window
    
    def callback(self, instance):
        Textlist = (" That's a fucking good choice Broo!!!","Ohhhh, Nice Onee!!","Damien Nique tes morts","Ohhhh Fuckkk Yeahhhh")
        self.grettings.text = "Salut" + Account[self.switcher.text][1]
        self.Connexion()
        

    def MouseClick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    
    
    def Connexion(self): 
        Connexion = pyautogui.locateOnScreen("images/Connexion.png", grayscale=False,confidence=0.90)
        try:
            if Connexion!=None:
                account = Account[self.switcher.text][0]
                password = Account[self.switcher.text][1]
                print(account,password)
                
                #LogDesired
                pyautogui.moveTo(Connexion[0],Connexion[1]+80)
                time.sleep(0.1)
                self.MouseClick()
                pyautogui.typewrite(account, interval=0.10)
                time.sleep(0.1)
                print('Log Write')
                    
                #PwdDesired
                pyautogui.moveTo(Connexion[0],Connexion[1]+140)
                time.sleep(0.1)
                self.MouseClick()
                pyautogui.typewrite(password, interval=0.10)
                time.sleep(0.1)
                print('Pwd Write')
                    
                #Press connexion button
                pyautogui.moveTo(Connexion[0]+60,Connexion[1]+520)
                time.sleep(0.1)
                self.MouseClick()
                time.sleep(6)
                
                #Press Play button
                pyautogui.moveTo(Connexion[0],Connexion[1]+650)
                time.sleep(0.1)
                self.MouseClick()
                time.sleep(20)   
            else:
                print('No connexion detected')       
        except:
            print('No more accounts')
     

if __name__ == "__main__":
    Melo().run()