#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Root(FloatLayout):
    def show_stuff(self, item):
        print(item.str_Label, item.str_TextInput)

    def show_ids(self, ids):
        for id in ids:
            print(id)


class LayoutPlayApp(App):
    pass


if __name__ == '__main__':
    LayoutPlayApp().run()
