This project involves the develpment of a smart wiper system, consisting of 3 ECUs (Electronic Control Unit): Main ECU, Humidity Sensor ECU and Wiper Control ECU.

The **humidity sensor ECU** is going to return random values between 0 and 40 with a 7 second cycle. The below table show the correlation between the sensor value and the rain intensity. [Check it here]{https://github.com/denisboboi492/CAPL-CANoe/blob/main/Smart%20Wiper/Sensor_ECU.can}
| Sensor value | Rain intensity |
| ------------ | -------------- |
|       0-7    |      no rain   |
|    8-15      |     low        |
|   16-31      |     medium     |
|   32-40      |      high      |

The **wiper control ECU** will receive commands that will control the speed of the wipers. When pressing the 'S' button, the current speed of the wiper will be sent to the BUS. [Check it here]{https://github.com/denisboboi492/CAPL-CANoe/blob/main/Smart%20Wiper/Wiper_ECU.can}
| Values       | Wipers speed   |
| ------------ | -------------- |
|       0      |    OFF         |
|    1         |      LOW       |
|   2          |        MEDIUM  |
|   3          |       HIGH     |
| anything else|invalid command |

The **main ECU** monitors messages, from the humidity sensor, on the BUS and sends commands to wiper control. [Check it here]{https://github.com/denisboboi492/CAPL-CANoe/blob/main/Smart%20Wiper/Main_ECU.can}

In the print screen below we can observe the behavior of the system:
![image](https://github.com/user-attachments/assets/6947cf4b-4362-4e3b-a266-24bdc3c6bb71)
