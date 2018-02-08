# GPIO pins 2, 3, 4, 17, 27, 22, 10, 9, 11, 5
import RPi.GPIO as IO

IO.setwarnings(False)       #do not show any warnings
IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(02,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(03,IO.OUT)
IO.setup(04,IO.OUT)
IO.setup(17,IO.OUT)
IO.setup(27,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(10,IO.OUT)
IO.setup(09,IO.OUT)
IO.setup(11,IO.OUT)
IO.setup(05,IO.OUT)

leds = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5]
percentage = 10

if percentage % 10 >= 5:
    percentage = percentage/10
# round percentage, reduce to 0 to 9 or 1 to 10

IO.out(leds[percentage], true)

# when new percentage received, turn off leds and rerun program? can you run python scripts from python
