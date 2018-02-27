from sensorRead import sensorRead
import datetime
from counter import Counter
#import countHuman
#import htmlClass
import time
import json
import requests
class masterLoop:
    def __init__(self, fileName):
        settings = masterLoop.loadPiSettings(fileName)
        pins = [settings['sensorInfo']['leadPin'], settings['sensorInfo']['followerPin']]
        self.sensorControl = sensorRead(pins)
        print("Sensor Set Up.")
        self.stillRunning = True
        self.counter = Counter(pins, [.1, 1.5])
        self.lastUpdate = datetime.datetime.now()
        self.totalCount = 0
        self.run()
    def run(self):
        while(self.stillRunning):
            if  datetime.datetime.now() - self.lastUpdate > datetime.timedelta(seconds = 10):
                count = self.counter.update(self.sensorControl.ReadingQueue)
                #print('Returned Count from Counter is '+ str(count))
		if count != 0:
                    self.postData(count)
                self.totalCount = self.totalCount + count
                #print('Total Count of Pi', self.totalCount)
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
    @staticmethod
    def loadPiSettings(fileName):
        with open(fileName) as jsonFile:
            configSettings = json.load(jsonFile)
        print(configSettings)
        print("JSON LOADED")
        return configSettings
    
    def postData(self, count):
        API_ENDPOINT = 'https://infinite-peak-11670.herokuapp.com/data-add'
        location = 'Rebeccas'
        data = {
            'location_name': location,
            'count': count,
        }
        r = requests.post(url = API_ENDPOINT, data = data)
        print(location + ' ' + r.text)
        
    def __del__(self):
        self.sensorControl.__del__()