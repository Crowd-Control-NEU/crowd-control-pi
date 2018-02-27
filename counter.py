import datetime
class Counter:
    def __init__(self, channelInputs, timeControl = [.5, 1.5]):
        self.count = 0
        self.channelIds = channelInputs
        self.timeControl = (datetime.timedelta(seconds = timeControl[0]),datetime.timedelta(seconds = timeControl[1]))
        self.extraReading = ''
    def update(self, readingsQueue):
	print(readingsQueue)
        if not readingsQueue:
            #self.resetExtraReading()
	    print('Empty Reading Queue')
            return 0
        elif len(readingsQueue) ==1:
            self.extraReading = readingsQueue[0]
            return 0
        self.count = 0
        if self.extraReading:
            readingsQueue.insert(0, self.extraReading)
            self.extraReading = ''
        currentItem = readingsQueue[0]
        outside = 0
        inside = 1
        currentItemIndex = 0
        index = 1
        while readingsQueue:
            nextItem = readingsQueue[index]
            if currentItem[0] != nextItem[0] and self.checkTimeControl(currentItem[1], nextItem[1]):
                if currentItem[0] == self.channelIds[outside]:
                     self.count = self.count + 1
                     print('Person entered')
                     print('Time of walkthrough', abs( datetime.datetime.combine(datetime.date.min, currentItem[1]) - datetime.datetime.combine(datetime.date.min, nextItem[1])))
                elif currentItem[0] == self.channelIds[inside]:
                    self.count = self.count - 1
                    print('Person Exits')
                    print('Time of walkthrough', abs( datetime.datetime.combine(datetime.date.min, currentItem[1]) - datetime.datetime.combine(datetime.date.min, nextItem[1])))
                readingsQueue.remove(currentItem)
                readingsQueue.remove(nextItem)
                if not readingsQueue:
                    return self.count
                currentItem = readingsQueue[0]
                currentItemIndex = 0
                index = 0
            index = index+1
            if index >= len(readingsQueue):
                readingsQueue.remove(currentItem)
                if not readingsQueue: return self.count
                elif len(readingsQueue) == 1:
                    self.extraReading = readingsQueue[-1]
                    readingsQueue.remove(self.extraReading)
                    return self.count
                currentItem = readingsQueue[0]
                currentItemIndex = 0
                index = 1
        return self.count
           #Have a current and next item. Update current item when it is counted. If end of the list
    
    def checkTimeControl(self, currentTime, nextTime):
         diffTime = abs( datetime.datetime.combine(datetime.date.min, currentTime) - datetime.datetime.combine(datetime.date.min, nextTime))
	 print('Difference in time is')
	 print(diffTime)
	 if diffTime > self.timeControl[0] and diffTime < self.timeControl[1]:
             return True
         else: return False
