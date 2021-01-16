import sys

from pip._vendor.distlib.compat import raw_input

from tello import Tello

billy = Tello()

# Tell the user what to do
print('Type in a Tello SDK command and press the enter key. Enter "quit" to exit this program.')

# Loop infinitely waiting for commands or until the user types quit or ctrl-c
while True:

    try:
        # Read keyboard input from the user
        if sys.version_info > (3, 0):
            # Python 3 compatibility
            message = input('')
        else:
            # Python 2 compatibility
            message = raw_input('')

        # If user types quit then lets exit and close the socket
        if 'quit' in message:
            print("Program exited successfully")
            billy.close_socket()
            break

        # Run parameter sweep function
        if 'sweep' in message:
            print("Initiate parameter sweep")
            billy.run_sweep()

        # Override parameter sweep
        if 'override' in message:
            print("Parameter sweep overridden")
            billy.terminate_sweep()

        # Send the command to Tello
        billy.send(message)

    # Handle ctrl-c case to quit and close the socket
    except KeyboardInterrupt as e:
        billy.close_socket()
        break
