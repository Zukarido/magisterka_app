from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
import time
import tensorflow as tf
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
import numpy as np
import os
from kivy.logger import Logger




class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=3


        self.predict_btn = Button(text="predict", background_color=(1,0,0,1))
        self.predict_btn.bind(on_press=self.predict_lesion)
        self.add_widget(self.predict_btn)


        # self.file = FileChooserListView(path = cur_dir)
        # self.add_widget(self.file)

        #self.model = tf.keras.models.load_model('mobilenet.hdf5')

        # self.choose_photo_btn = Button(text="pre")
        # self.choose_photo_btn.bind(on_press=self.choose_photo)
        # self.add_widget(self.choose_photo_btn)

        # # self.camera = Camera(play=True)
        # # self.add_widget(self.camera)

        # self.make_photo = Button(text="make photo")
        # self.make_photo.bind(on_press=self.make_photo_func)
        # self.add_widget(self.make_photo)


        # self.model = tf.keras.models.load_model('S:\Magisterka_app/mobilenet.hdf5')
        # self.last_image_name = ""

        # self.image = None
        # self.file = FileChooserListView(path = "S:\Magisterka_app/")
        # self.add_widget(self.file)

    def predict_lesion(self, instance):
        return 0
    # def choose_photo(self, instance):

    #     self.preprocess("S:\Magisterka_app/ISIC_0024319.jpg")

    # def make_photo_func(self, instance):
    #     timestr = time.strftime("%Y%m%d_%H%M%S")
    #     self.last_image_name = "IMG_{}.png".format(timestr)
    #     self.camera.export_to_png(self.last_image_name)
    #     self.preprocess(self.last_image_name)



    # def preprocess(self, path):
    #     img  = tf.keras.utils.load_img(path = path, grayscale=False, color_mode="rgb",target_size=(224,224), interpolation="nearest",keep_aspect_ratio=False)
    #     print(type(img))
    #     img  = np.array(img)
    #     y = self.model((img[np.newaxis,:,:,:]), training=False)
    #     print(y.numpy()[0][0])
    #     self.cur_dir = str(y.numpy()[0][0])
        


class MyApp(App):
    def build(self):
        return MyGrid()




if __name__ == "__main__":
    MyApp().run()