from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy import platform
import plyer

PATH = '.'
TIME_VIBRATION = 0.5

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

    PATH = "/storage/emulated/0"  # app_folder

import os
import convertisseur

class SaveDialog(BoxLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(BoxLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)

    _popup = None

    def dismiss_popup(self):
        try:
            plyer.vibrator.vibrate(TIME_VIBRATION)
        except:
            print("exception vibreur")
        self._popup.dismiss()

    def show_jpg_to_png(self):
        try:
            plyer.vibrator.vibrate(TIME_VIBRATION)
        except:
            print("exception vibreur")
        content = SaveDialog(save=self.jpg_to_png, cancel=self.dismiss_popup)
        content.ids.filechooser.path = PATH
        self._popup = Popup(title="jpg to png", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_pdf_to_png(self):
        try:
            plyer.vibrator.vibrate(TIME_VIBRATION)
        except:
            print("exception vibreur")
        content = SaveDialog(save=self.pdf_to_png, cancel=self.dismiss_popup)

        content.ids.filechooser.path = PATH
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def jpg_to_png(self, path, filename):
        convertisseur.jpg_to_png(str(os.path.join(path, filename)))
        self.dismiss_popup()

    def pdf_to_png(self, path, filename):
        convertisseur.pdf_to_png(str(os.path.join(path, filename)))
        self.dismiss_popup()

    def show_png_to_jpg(self):
        try:
            plyer.vibrator.vibrate(TIME_VIBRATION)
        except:
            print("exception vibreur")
        content = SaveDialog(save=self.png_to_jpg, cancel=self.dismiss_popup)
        content.ids.filechooser.path = PATH
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
    
    def png_to_jpg(self, path, filename):
        convertisseur.png_to_jpg(str(os.path.join(path, filename)))
        self.dismiss_popup()
        # vibrator.vibrate(10)


class ConvertisseurIhmApp(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    ConvertisseurIhmApp().run()