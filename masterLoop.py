from sensorRead import sensorRead
import datetime
from counter import Counter
#import countHuman
#import htmlClass
import time
import json
class masterLoop:
    def __init__(self, fileName):
        settings = masterLoop.loadPiSettings(fileName)
        pins = [settings['sensorInfo']['leadPin'], settings['sensorInfo']['followerPin']]
        self.sensorControl = sensorRead(pins)
        print("Sensor Set Up.")
        self.stillRunning = True
        self.counter = Counter(pins, [.5, 1.5])
        self.lastUpdate = datetime.datetime.now()
        self.totalCount = 0
        self.run()
    def run(self):
        while(self.stillRunning):
            if  datetime.datetime.now() - self.lastUpdate > datetime.timedelta(seconds = 10):
                count = self.counter.update(self.sensorControl.ReadingQueue)
                self.totalCount = self.totalCount + count
                print('Total Count of Pi', self.totalCount)
                self.lastUpdate = datetime.datetime.now()
                time.sleep(.1)
            #check for count
                #In count object keep queue of inputted signals
                #When queue is full figure out the count
                #set update object for post to check 
            #check posts
        self.__del__()
    def countUpdate(self):
        pass
    def loadPiSettings(fileName):
        with open(fileName) as jsonFile:
            configSettings = json.load(jsonFile)
        print(configSettings)
        print("JSON LOADED")
        return configSettings
    def __del__(self):
        self.sensorControl.__del__()