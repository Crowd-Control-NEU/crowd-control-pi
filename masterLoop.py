from sensorRead import sensorRead
import datetime
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
        self.run()
        
    def run(self):
        startUpTime = datetime.datetime.now()	
        while(self.stillRunning):
            if  datetime.datetime.now() - startUpTime > datetime.timedelta(seconds = 120):
                self.stillRunning = False
                print('Ending loop: current count ', self.sensorControl.ReadingQueue.qsize())
            time.sleep(.1)    
            #self.countHuman.update(sensorInput)
            #decide between reading in loop or use event based system (Advantage only get highs, easier to process repeat)
            #check for count
                #In count object keep queue of inputted signals
                #When queue is full figure out the count
                #set update object for post to check 
            #check posts
            #
        self.close()
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