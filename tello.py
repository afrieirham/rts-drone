# This code is adopted from https://learn.droneblocks.io/p/tello-drone-programming-with-python/
# Import the necessary modules
import socket
import threading
import time

# Travel to/from starting checkpoint 0 from/to the charging base
from threading import Thread

frombase = ["forward", 50, "ccw", 150]
tobase = ["ccw", 150, "forward", 50]

# Flight path to Checkpoint 1 to 5 and back to Checkpoint 0 sequentially
checkpoint = [
    [1, "cw", 90, "forward", 100],
    [2, "ccw", 90, "forward", 80],
    [3, "ccw", 90, "forward", 40],
    [4, "ccw", 90, "forward", 40],
    [5, "cw", 90, "forward", 60],
    [0, "ccw", 90, "forward", 40]
]


class Tello():
    parameter_sweep_thread: Thread
    parameter_sweep_lock = False

    def __init__(self):
        # IP and port of Tello
        self.tello_address = ('192.168.10.1', 8889)

        # IP and port of local computer
        self.local_address = ('', 9000)

        # Create a UDP connection that we'll send the command to
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to the local address and port
        self.sock.bind(self.local_address)

        # Create and start a listening thread that runs in the background
        # This utilizes our receive functions and will continuously monitor for incoming messages
        self.receiveThread = threading.Thread(target=self.receive)
        self.receiveThread.daemon = True
        self.receiveThread.start()

        # Put Tello into command mode
        self.send("command", 3)

    # Send the message to Tello and allow for a delay in seconds
    def send(self, message, delay=1):
        # Try to send the message otherwise print the exception
        try:
            self.sock.sendto(message.encode(), self.tello_address)
            print("Sending message: " + message)
        except Exception as e:
            print("Error sending: " + str(e))

        # Delay for a user-defined period of time
        time.sleep(delay)

    # Receive the message from Tello
    def receive(self):
        # Continuously loop and listen for incoming messages
        while True:
            # Try to receive the message otherwise print the exception
            try:
                response, ip_address = self.sock.recvfrom(128)
                print("Received message: " + response.decode(encoding='utf-8'))
            except Exception as e:
                # If there's an error close the socket and break out of the loop
                self.sock.close()
                print("Error receiving: " + str(e))
            break

    def takeoff(self):
        # Send the takeoff command
        self.send("takeoff", 3)

    def reset_position(self):
        # Start at checkpoint 1 and print destination
        self.send(frombase[0] + " " + str(frombase[1]), 4)
        self.send(frombase[2] + " " + str(frombase[3]), 4)
        print("Current location: Checkpoint 0 " + "\n")

    def sweep(self):
        # Billy's flight path
        for i in range(len(checkpoint)):
            if i == len(checkpoint) - 1:
                print("Returning to Checkpoint 0. \n")

            self.send(checkpoint[i][1] + " " + str(checkpoint[i][2]), 4)
            if not self.parameter_sweep_lock: return False
            self.send(checkpoint[i][3] + " " + str(checkpoint[i][4]), 4)
            if not self.parameter_sweep_lock: return False

            print("Arrived at current location: Checkpoint " + str(checkpoint[i][0]) + "\n")
            time.sleep(4)

    def ready_to_land(self):
        # Reach back at Checkpoint 0
        self.send(tobase[0] + " " + str(tobase[1]), 4)
        self.send(tobase[2] + " " + str(tobase[3]), 4)

        # Turn to original direction before land
        print("Turn to original direction before land.\n")
        self.send("cw 180", 4)

    def land(self):
        # Land
        self.send("land", 3)

    def close_socket(self):
        # Close the socket
        self.sock.close()

    def run_sweep(self):
        self.parameter_sweep_thread = threading.Thread(target=self.sweep)
        self.parameter_sweep_thread.daemon = True
        self.parameter_sweep_lock = True
        self.parameter_sweep_thread.start()

    def terminate_sweep(self):
        self.parameter_sweep_lock = False

    def forward(self):
        self.send("forward 10")

    def back(self):
        self.send("back 10")

    def turn_left(self):
        self.send("cw 90")

    def turn_right(self):
        self.send("ccw 90")