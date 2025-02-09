The goal of this project is to develop a system that enables remote control of a door handle, as visually represented by an Arduino's built-in LED. This system will utilize a panel created in Canoe, with code written in CAPL, and will be integrated with an Arduino device. This can be used to create automated test cases based on specific requirements.

The panel contains buttons for controlling COM port, simple lock-unlock, touch lock-unlock and includes input fields for port number and touch duration. Check the panel bellow and code [here](https://github.com/denisboboi492/CAPL-CANoe/blob/main/DoorHandle/CAPL_Node.can):

![panel_snip](https://github.com/user-attachments/assets/45f106f9-2bf8-43a8-9966-ecb5c643f0b8)

Let's examine each button to understand its purpose.

- Open and Close port buttons will open/close a COM port, in my case COM port 2, specified by user.
- The led control component indicates if the connection to the port is successful of not.
- The lock touch and duration components work together to simulate the pressing of lock sensor for a specified period. Same for unlock touch and duration.
- Send lock button will send a stimulus to actuate the sensor. Same for send unlock.

On the Arduino side, code available [here](https://github.com/denisboboi492/CAPL-CANoe/blob/main/DoorHandle/Arduino_side.ino), the lock/unlock sensor, simulated with Arduino's built-in LED, is triggered by commands received from the COM port.
