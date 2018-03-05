'''
Kivy Catalog

'''

import kivy
kivy.require('1.4.2')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

import backend

Builder.load_string("""
<ScreenUI>:
    
    canvas.before:
        Color:
            rgb: .12, .15, .26
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        Label:
            text: 'UI and Database prototype'
            pos: 230, 400
            size_hint: 3, .5

        Button:
            text: "View"
            pos: 500, 100
            size_hint: 1.6, .5
            on_press: root.view1(self.text)
        Button:
            text: "Add"
            pos: 500, 200
            size_hint: 1.6, .5
            on_press: root.adding(self.text)
        Button:
            text: "Delete"
            pos: 500, 300
            size_hint: 1.6, .5
            on_press: root.remove(self.text)
        
        TextInput:
            id: bottom
            size_hint_y: None
            size_hint: 2, .5
            pos: 290, 100
        TextInput:
            id: addbox
            size_hint_y: None
            size_hint: 2, .5
            pos: 290, 200
        TextInput:
            id: boxtop
            size_hint_y: None
            size_hint: 2, .5
            pos: 290, 300
            
        RstDocument:
            id: boxv
            size_hint: 2.3, 3
            pos: 40, 60
            text: ''
           

        """)

strng = StringProperty()

class ScreenUI(GridLayout):
    
    def view1(self, text):
        self.ids.boxv.text = str(backend.view()).replace('(','').replace(')','\n\n').replace('[','').replace(']','').replace(',','')
        
    def adding(self, text):
        x = self.ids.addbox.text.split(" ")
        
        title= str(x[0])
        strng= str(x[1])
        year = int(x[2])
        integ= int(x[3])
        
        backend.insert(title, strng, year, integ)
        
    def remove(self, text):
        backend.delete(int(self.ids.boxtop.text))
    
    pass

class WidgetApp(App): 



        
    
    def build(self):
        app = ScreenUI()
        return app

if __name__ == '__main__':
    WidgetApp().run()
