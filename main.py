from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class VpnPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=30, **kwargs)
        self.status = Label(text="VPN: desconectada", font_size=24)
        self.add_widget(self.status)
        self.add_widget(Button(text="Conectar", font_size=20, on_press=self.connect_vpn))

    def connect_vpn(self):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            Toast = autoclass('android.widget.Toast')
            Toast.makeText(activity, "Pyjnius funciona", Toast.LENGTH_SHORT).show()
            self.status.text = "VPN: solicitud enviada"
        except Exception as e:
            self.status.text = f"Error: {e}"

class PyVpnApp(App):
    def build(self):
        return VpnPanel()

if __name__ == '__main__':
    PyVpnApp().run()
