class Timer:
    def __init__(self, hours = 0, min = 0, seconds = 0):
        self.__hours = hours
        self.__min = min
        self.__seconds = seconds

    def __str__(self):
        timer = [ str(self.__hours), str(self.__min), str(self.__seconds)]
        ret = ''
        for t in timer:
            if len(t) < 2:
                t = '0'+ t
            ret += t + ':'
        return ret[0 : 8]

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__min += 1
            if self.__min == 60:
                self.__min = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0
                    
    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__min -= 1
            if self.__min == -1:
                self.__min = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23 


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
