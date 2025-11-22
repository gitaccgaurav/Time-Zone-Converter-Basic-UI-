
from settings import *
from tkinter.constants import RIGHT

from settings import WINDOW_HEIGHT,WINDOW_WIDTH ,window
from  timezone_converter import time_zone_convertor as tzc

class App:
    def __init__(self):
        self.window = window
        self.time_str = None
        self.from_tz = None
        self.to_tz = None
        self.to_tz_entry = None
        self.from_tz_entry = None
        self.time_str_entry = None
    def main_window(self):
        self.window.title("TimeZone-Converter")
        self.window.geometry(f'{WINDOW_HEIGHT}x{WINDOW_WIDTH}')
        self.window.config(background="#32a8a4")

    def entry(self):
        self.time_str_entry = tk.Entry(self.window)
        self.time_str_entry.pack()
        self.from_tz_entry = tk.Entry(self.window)
        self.from_tz_entry.pack()
        self.to_tz_entry = tk.Entry(self.window)
        self.to_tz_entry.pack()
        submit_button = tk.Button(self.window,text = "Submit",command=self.submit)
        submit_button.pack(side= RIGHT)
    def submit(self):
        self.time_str = self.time_str_entry.get()
        self.from_tz = self.from_tz_entry.get()
        self.to_tz = self.to_tz_entry.get()
    def output(self):
        print(tzc(self.time_str,self.from_tz_entry,self.to_tz_entry))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":

    app = App()
    app.main_window()
    app.entry()
    app.run()
    app.output()

# time_str = input("Enter time")
# from_tz = input("Enter your timezone")
# to_tz = input("Enter target timezone")
# result = time_zone_convertor(time_str,from_tz,to_tz)
# print(result)