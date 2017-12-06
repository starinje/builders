import time
import grovepi

print "hello world"

# The electromagnet can hold a 1KG weight
# SIG,NC,VCC,GND
electromagnet = 7

# something

grovepi.pinMode(electromagnet,"OUTPUT")
time.sleep(1)

while True:
  try:
    # Switch on electromagnet
    grovepi.digitalWrite(electromagnet,1)
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



