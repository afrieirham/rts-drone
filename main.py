from tkinter import *

from tello import Tello

# Initialize tello
billy = Tello()

# Setup tkinter window
top = Tk()
top.title('Tello Controller')
top.geometry('600x400')


def start_sweep():
    print("Initiate parameter sweep")
    billy.run_sweep()


def override_sweep():
    print("Parameter sweep overridden")
    billy.terminate_sweep()


def quit_dashboard():
    print("Program exited successfully")
    billy.close_socket()
    top.destroy()


# Add dashboard button
sweepButton = Button(top, height=2, width=20, text="Start Parameter Sweep", command=start_sweep)
overrideButton = Button(top, height=2, width=20, text="Override", command=override_sweep)
quitButton = Button(top, height=2, width=20, text="Quit", command=quit_dashboard)

sweepButton.pack(padx=10, pady=5)
overrideButton.pack(padx=10, pady=5)
quitButton.pack(padx=10, pady=5)

top.mainloop()
