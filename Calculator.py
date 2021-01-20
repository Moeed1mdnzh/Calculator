import kivy
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (500,600)

Builder.load_file("Design.kv")

class bootUp(Widget):
	pass

class Calculator(App):
	def build(self):
		return bootUp()



if __name__ == "__main__":
		Calculator().run()