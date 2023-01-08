import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = str(self.formula)

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if (str(instance.text).lower() == "x"):
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calculate(self, instance):
        self.lbl.text = str(eval(self.formula))
        self.formula = "0"

    def build(self):
        self.formula = "0"
        layout = GridLayout(cols=4, spacing=3, padding=3)
        self.lbl = Label(text="0", font_size=40, halign="right", valign="center", size_hint=(1, .6))
        layout.add_widget(self.lbl)

        layout.add_widget(Button(text="7", on_press=self.add_number))
        layout.add_widget(Button(text="8", on_press=self.add_number))
        layout.add_widget(Button(text="9", on_press=self.add_number))
        layout.add_widget(Button(text="X", on_press=self.add_operation))

        layout.add_widget(Button(text="4", on_press=self.add_number))
        layout.add_widget(Button(text="5", on_press=self.add_number))
        layout.add_widget(Button(text="6", on_press=self.add_number))
        layout.add_widget(Button(text="-", on_press=self.add_operation))

        layout.add_widget(Button(text="1", on_press=self.add_number))
        layout.add_widget(Button(text="2", on_press=self.add_number))
        layout.add_widget(Button(text="3", on_press=self.add_number))
        layout.add_widget(Button(text="+", on_press=self.add_operation))

        layout.add_widget(Button(text="0", on_press=self.add_number))
        layout.add_widget(Button(text="C", on_press=self.calculate))
        layout.add_widget(Button(text="/", on_press=self.add_operation))
        layout.add_widget(Button(text="=", on_press=self.calculate))

        return layout


if __name__ == "__main__":
    CalculatorApp().run()
