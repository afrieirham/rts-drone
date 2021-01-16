from tkinter import *

from tello import Tello

# Initialize tello
billy = Tello()

# Setup tkinter window
top = Tk()
top.title('Tello Controller')
top.geometry('1100x600')


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


def forward():
    print("Move forward 10cm")
    billy.forward()


def back():
    print("Move back 10cm")
    billy.back()


def turn_left():
    print("Rotate left 90 degree")
    billy.turn_left()


def turn_right():
    print("Rotate right 90 degree")
    billy.turn_right()


# Create dashboard button
readyToLandButton = Button(top, height=2, width=20, text="Prepare to land", command=ready_to_land)
landButton = Button(top, height=2, width=20, text="Land", command=land)
sweepButton = Button(top, height=2, width=20, text="Run sweep", command=start_sweep)
takeoffButton = Button(top, height=2, width=20, text="Take Off", command=takeoff)
resetPositionButton = Button(top, height=2, width=20, text="Ready position", command=reset_position)

forwardButton = Button(top, height=2, width=20, text="Forward 10cm", command=forward)

leftButton = Button(top, height=2, width=20, text="Rotate left", command=turn_left)
overrideButton = Button(top, height=2, width=20, text="Override", command=override_sweep)
rightButton = Button(top, height=2, width=20, text="Rotate right", command=turn_right)

backButton = Button(top, height=2, width=20, text="Back 10cm", command=back)
quitButton = Button(top, height=2, width=20, text="Quit", command=quit_dashboard)

# Setup button layout
readyToLandButton.grid(row=1, column=1)
landButton.grid(row=1, column=2)
sweepButton.grid(row=1, column=4)
takeoffButton.grid(row=1, column=6)
resetPositionButton.grid(row=1, column=7)

forwardButton.grid(row=3, column=4)

leftButton.grid(row=5, column=3)
overrideButton.grid(row=5, column=4)
rightButton.grid(row=5, column=5)

backButton.grid(row=7, column=4)
quitButton.grid(row=9, column=4)


top.mainloop()
