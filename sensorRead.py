import RPi.GPIO as GPIO
from datetime import datetime
import queue
class sensorRead():
    def __init__(self, inputPins = [1, 1]):
        self.ReadingQueue = []
        self.leadingSensor = inputPins[0]
        self.followSensor = inputPins[1]
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.leadingSensor, GPIO.IN)
        GPIO.setup(self.followSensor, GPIO.IN)  #Read output from PIR motion sensor
        print('Leading Sensor Numbers', self.leadingSensor)
        GPIO.add_event_detect(self.leadingSensor, GPIO.RISING, callback=self.readCallback, bouncetime=30)
        GPIO.add_event_detect(self.followSensor, GPIO.RISING, callback=self.readCallback, bouncetime=30)
    def readCallback(self, channel):
        readinTime = datetime.time(datetime.now()) 
        self.ReadingQueue.append([channel, readinTime])
    def checkOn(self):
        pass
    def __del__(self):
        self.clearEvents()
        GPIO.cleanup(self.leadingSensor)
        GPIO.cleanup(self.followSensor)
        print('Sensor Control has been deleted')
    def clearEvents(self):
        GPIO.remove_event_detect(self.leadingSensor)
        GPIO.remove_event_detect(self.followSensor)
        