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


def takeoff():
    print("Drone takeoff")
    billy.takeoff()


def reset_position():
    print("Go to checkpoint 0")
    billy.reset_position()


def ready_to_land():
    print("Return to charging base")
    billy.ready_to_land()


def land():
    print("Drone landing")
    billy.land()


# Add dashboard button
resetPositionButton = Button(top, height=2, width=20, text="Ready position", command=reset_position)
takeoffButton = Button(top, height=2, width=20, text="Take Off", command=takeoff)
landButton = Button(top, height=2, width=20, text="Land", command=land)
sweepButton = Button(top, height=2, width=20, text="Run sweep", command=start_sweep)
overrideButton = Button(top, height=2, width=20, text="Override", command=override_sweep)
readyToLandButton = Button(top, height=2, width=20, text="Prepare to land", command=ready_to_land)
quitButton = Button(top, height=2, width=20, text="Quit", command=quit_dashboard)

resetPositionButton.pack(padx=10, pady=5)
takeoffButton.pack(padx=10, pady=5)
landButton.pack(padx=10, pady=5)
sweepButton.pack(padx=10, pady=5)
overrideButton.pack(padx=10, pady=5)
readyToLandButton.pack(padx=10, pady=5)
quitButton.pack(padx=10, pady=5)

top.mainloop()
