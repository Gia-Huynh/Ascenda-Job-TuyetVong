import json

filePath = 'input.json'
def addDate (Y, M, D, addNum):
    #Y, M, D = Year, Month, Day
    #addNum = number of days to add
    
    def getDayInMonth ():
        month = M
        year = Y
        Days_In_Month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (month!=2):
            return Days_In_Month [month]
        elif (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    return 29
                return 28
            return 29
        else:
            return 28
    while (addNum > 0):
        #Some optimization can be done here, instead of
        # adding 1 by 1 to D,
        # we can add the Day in Month minus 1 straight into D
        D = D + 1
        if (D - 1 == getDayInMonth ()):
            D = 1
            M = M+1
            if (M == 13):
                Y = Y+1
                M = 1
        addNum = addNum - 1
    return Y, M ,D
class jsonObject ():
    def __init__ (self):
        self.data = None
    def getData (self):
        return self.data
    def cleanData (self, data):
        #Optional steps, to remove data clutter by removing
        #unused class.
        Category_Keep_list = ["id", "category", "merchants", "valid_to"]
        baka = data
        for a in baka['offers']:
            for key in a.copy():
                if key not in self.keep_list:
                    a.pop (key, None)
        return a
    def readFile (self, filePath):
        with open(filePath) as f:
            self.data = json.load(f)
        
test = jsonObject ()
test.readFile (filePath)
