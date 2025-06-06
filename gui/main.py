import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class App:
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.title("POS System")
        self.root.state('zoomed')  # This will maximize the window
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
