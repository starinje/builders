import time
import grovepi

print "hello world"

# The electromagnet can hold a 1KG weight

# Connect the Grove Electromagnet to digital port D4
# SIG,NC,VCC,GND
electromagnet_1 = 7
electromagnet_2 = 8

# something

grovepi.pinMode(electromagnet,"OUTPUT")
time.sleep(1)

while True:
  try:
    # Switch on electromagnet
    grovepi.digitalWrite(electromagnet_1,1)
    grovepi.digitalWrite(electromagnet_2,1)
    print "turning on"
    time.sleep(100)

    # Switch off electromagnet
    # grovepi.digitalWrite(electromagnet,0)
    # print "off"
    # time.sleep(2)

  except KeyboardInterrupt:
    grovepi.digitalWrite(electromagnet,0)
    break
  except IOError:
    print "Error"



