This project involves the develpment of a smart wiper system, consisting of 3 ECUs (Electronic Control Unit): Main ECU, Humidity Sensor ECU and Wiper Control ECU.

The **humidity sensor ECU** is going to return random values between 0 and 40 with a 7 second cycle. The below table show the correlation between the sensor value and the rain intensity.
| Sensor value | Rain intensity |
| ------------ | -------------- |
|       0-7    |      no rain   |
|    8-15      |     low        |
|   16-31      |     medium     |
|   32-40      |      high      |

The **wiper control ECU** will receive commands that will control the speed of the wipers. When pressing the 'S' button, the current speed of the wiper will be sent to the BUS.
| Values       | Wipers speed   |
| ------------ | -------------- |
|       0      |    OFF         |
|    1         |      LOW       |
|   2          |        MEDIUM  |
|   3          |       HIGH     |
| anything else|invalid command |

The **main ECU** monitors messages, from the humidity sensor, on the BUS and sends commands to wiper control.
