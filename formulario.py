import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class RegistroApp(App):
    def build (self):
        self.title="Formulario de Registro"
        layout=BoxLayout(orientation="vertical", padding=30, spacing=10)

        # Añadiendo labels y entradas
        head_label=Label(text="Formulario de Registro con Python", font_size=26,bold=True,height=40)
        name_label=Label(text="Nombre:", font_size=18)
        self.name_input=TextInput(multiline=False, hint_text="Ingrese su nombre", font_size=18, height=40)

        email_label=Label(text="Correo:", font_size=18)
        self.email_input=TextInput(multiline=False, hint_text="Ingrese su correo", font_size=18, height=40)

        password_label=Label(text="Contraseña:", font_size=18)
        self.password_input=TextInput(multiline=False, hint_text="Ingrese su contraseña", font_size=18, height=40, password=True)

        confirmation_label=Label(text="Confirmar Contraseña:", font_size=18)
        self.confirmation_input=TextInput(multiline=False, hint_text="Confirme su contraseña", font_size=18, height=40,password=True)

        # Añadiendo botones
        submit_button=Button(text="Registrarse", font_size=18, height=40,on_press=self.register)

    
        # Añadiendo widgets al layout
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirmation_label)
        layout.add_widget(self.confirmation_input)
        layout.add_widget(submit_button)

        return layout
    
    def register(self,instance):
        # Recolectar informacion
        name=self.name_input.text
        email=self.email_input.text
        password=self.password_input.text
        confirmation=self.confirmation_input.text

        # Validar informacion
        if name.strip()=="" or email.strip()=="" or password.strip()=="" or confirmation.strip()=="":
            message="Todos los campos son obligatorios"
        elif password!=confirmation:
            message="Las contraseñas no coinciden"
        else:
            filename=name + ".txt"
            with open (filename,"w") as file:
                file.write("Nombre:{}\n".format(name))
                file.write("Correo:{}\n".format(email))
                file.write("Contrasena:{}\n".format(password))
                file.write("Confirmacion:{}\n".format(confirmation))
            message="Formulario enviado\n Nombre: {}\n Correo: {}".format(name,email)
             # Vaciar labels de entrada
            self.name_input.text=""
            self.email_input.text=""
            self.password_input.text=""
            self.confirmation_input.text=""

        

        # Mensage de alerta
        popup=Popup(title="Alerta",content=Label(text=message),size_hint=(None,None),size=(400,200))
        popup.open()
       


if __name__ == "__main__":
    RegistroApp().run()