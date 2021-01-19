import kivy
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file("Design.kv")

class application(Widget):
	pass

class Calculator(App):
	def build(self):
		return application()



if __name__ == "__main__":
		Calculator().run()