from gpiozero import OutputDevice, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause

garden = OutputDevice(17)
motion = MotionSensor(4)
light = LightSensor(5)

garden.source = all_values(booleanized(light, 0, 0.1), motion)

pause()