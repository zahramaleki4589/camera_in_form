import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class OcrApplication(Frame):
    def __init__(self, screen=None, video_source=0):
        super().__init__(screen)
        self.screen = screen

        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)

        self.canvas = Canvas(self, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH),
                             height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        self.Open_Camera_In()


    def Open_Camera_In(self):

        self.framCamera_In = Frame(self.screen, width=410, bg="red", height=400)
        self.framCamera_In.place(x=10, y=40)

        self.label3 = ttk.Label(self.framCamera_In)
        self.label3.pack()
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)  # تغییر اندازه فریم به عرض و طول نصف شده
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label3.imgtk = imgtk
        self.label3.configure(image=imgtk)
        self.label3.place(x=0, y=0, width=410, height=400)  # تغییر اندازه Label به 320 در 240 پیکسل
        self.framCamera_In.place(x=10, y=10, width=410, height=400)  # تغییر اندازه Frame به 320 در 240 پیکسل
        self.framCamera_In.after(1, self.Open_Camera_In)
