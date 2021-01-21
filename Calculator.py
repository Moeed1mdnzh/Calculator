import kivy
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from math import *

Window.size = (500,600)

Builder.load_file("Design.kv")

class bootUp(Widget):
	def add_sign(self,sign):
		self.ids.phrase.text += sign

	def add_number(self,num):
		self.ids.phrase.text += num

	def clear_all(self):
		self.ids.phrase.text = ''

	def rmv_element(self):
		self.ids.phrase.text = self.ids.phrase.text[:len(self.ids.phrase.text)-1]

	def calculate(self):
		phrase = self.ids.phrase.text
		filters = {
					"^":"**",
					"π":"pi",
					"÷":"/",
					"x":"*"
				}
		for k,v in filters.items():
			phrase = phrase.replace(k,v)
		try:
			self.ids.phrase.text = str(round(eval(phrase),2))
		except Exception:
			self.ids.phrase.text = "[ERROR]"

	def change_color(self,instance,value):
		instance.foreground_color = (60/255,60/255,60/255,1)

class Calculator(App):
	def build(self):
		return bootUp()



if __name__ == "__main__":
		Calculator().run()