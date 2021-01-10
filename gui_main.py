import queue
import win32gui
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageGrab
import cv2
from module.predict import test,test_gui
def PerformNumber(img, mode = 0):
    digit = test_gui(img)
    if (mode == 0):
        print(digit)
    else:
        cur = 0
        for i in range(len(digit)):
            if (0 <= digit[i] <= 9):
                cur = cur * 10 + digit[i]
            else:
                print(cur, end = ' ')
                cur = 0
        print(cur)
# GUI
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.title("Nhận dạng chữ số viết tay")
        # drawing
        self.canvas = tk.Canvas(self, width = 304, height = 304, bg = "white", cursor = "cross")
        self.label = tk.Label(self, text = "Đang vẽ", font = ("Helvetica", 40))
        self.classify_btn = tk.Button(self,  text = "Nhận dạng", font = ("Helvetica 15 bold"), command = self.classify_handwritting)
        self.button_clear = tk.Button(self, text = "Xóa", font = ("Helvetica 15 bold"), command = self.clear_all)
        # label predict aree

        # button area
        self.canvas.grid(row = 0, column = 0, pady = 2, sticky = W, )
        self.label.grid(row = 0, column = 1, pady = 2, padx = 2)
        self.classify_btn.grid(row = 1, column = 1, pady = 2, padx = 2)
        self.button_clear.grid(row = 1, column = 0, pady = 2)

        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwritting(self):
        self.label.configure(text = 'Đang nhận dạng')
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        img = ImageGrab.grab(rect)
        img = img.convert('L')
        # img.show() # this image take border
        img = 255 - np.array(img)
        # img = img[2 : , 2 : 302]
        # img=np.array(img)
        # digit, accuracy = prediction(img)
        res = test_gui(img)
        # result = "There are " + str(len(digit_list)) + " digits:\n";
        # for x in digit_list: result += str(x) + ' '
        self.label.configure(text = res)

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill = "black")

# print(prediction(img))
# digit_detected(img)
# print(digit_recognition(img))
# PerformNumber(img, 1)

app = Application()
mainloop()