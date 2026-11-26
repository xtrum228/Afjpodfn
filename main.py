import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock

import cv2
import numpy as np

class ChessCamera(Image):
    def __init__(self, **kwargs):
        super(ChessCamera, self).__init__(**kwargs)
        self.capture = None
        # Инициализация камеры (0 — по умолчанию для мобильных/ПК)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0) # 30 FPS

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Препроцессинг кадра (здесь будет поиск доски OpenCV)
            # Для примера: добавляем тестовый оверлей / текст
            h, w, _ = frame.shape
            cv2.putText(frame, "Chess Vision Active", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Подсветка центральной зоны (прототип сетки доски)
            cv2.rectangle(frame, (int(w*0.2), int(h*0.2)), (int(w*0.8), int(h*0.8)), (255, 0, 0), 2)

            # Конвертируем OpenCV BGR в Kivy Texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = texture1

    def on_stop(self):
        if self.capture:
            self.capture.release()

class ChessApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Виджет камеры с оверлеем
        self.camera_view = ChessCamera()
        layout.add_widget(self.camera_view)
        
        # Панель статуса / подсказок
        self.status_label = Label(
            text="Сканирование доски... Жду первый ход", 
            size_hint_y=0.15,
            font_size='18sp'
        )
        layout.add_widget(self.status_label)
        
        return layout

if __name__ == '__main__':
    ChessApp().run()
