
from settings import *
from tkinter.constants import  N,S,W, E

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
        self.result_label = None

    def main_window(self):
        self.window.title("TimeZone-Converter")
        self.window.geometry(f'{WINDOW_HEIGHT}x{WINDOW_WIDTH}')
        self.window.config(background="#34495e")
        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_columnconfigure(1, weight=3)

    def entry(self):
        row = 2

        self.time_str_entry = tk.Entry(self.window,
                                       width=50,
                                       font=("Arial", 14))

        self.time_str_entry.grid(row=row, column=1, sticky=W, padx=10, pady=10)

        row +=1

        self.from_tz_entry = tk.Entry(self.window,
                                      width=50,
                                      font=("Arial", 14))

        self.from_tz_entry.grid(row=row, column=1, sticky=W, padx=10, pady=10)

        row+=1

        self.to_tz_entry = tk.Entry(self.window,
                                    width=50,
                                    font=("Arial", 14))

        self.to_tz_entry.grid(row=row, column=1, sticky=W, padx=10, pady=10)

        row+=1
        submit_button = tk.Button(self.window,
                                  text = "Convert Time",
                                  command=self.submit,
                                  bg="#1abc9c",
                                  fg="white",
                                  activebackground="#16a085",
                                  font=("Arial", 16, "bold"),
                                  width=20)

        submit_button.grid(row=row, column=0, columnspan=2, pady=30)


    def submit(self):

        self.time_str = self.time_str_entry.get()
        self.from_tz = self.from_tz_entry.get()
        self.to_tz = self.to_tz_entry.get()
        result = self.output()
        self.result_label = tk.Label(self.window,
                                     text=f'{result}',
                                     bg="#2c3e50",
                                     fg="#ecf0f1",
                                     padx=20,
                                     pady=15,
                                     font=("Arial", 16))
        self.result_label.grid(row=23, column=0, columnspan=2, sticky=W + E, padx=50, pady=20)


    def output(self):
        return tzc(self.time_str, self.from_tz, self.to_tz)


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":

    app = App()
    app.main_window()
    app.entry()
    app.run()

