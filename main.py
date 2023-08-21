from tkinter import *
import camera

if __name__ == "__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (500, 500, 80, 80))
    screen.title("")
    screen.resizable(False, False)
    pageMe= camera.OcrApplication(screen)
    screen.mainloop()