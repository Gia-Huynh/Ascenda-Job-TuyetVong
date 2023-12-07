import json
import utils
userInput = "2020-04-24"
filePath = 'input.json'
dateRange = 5
userInput = utils.addDate (userInput, dateRange)
categorySkipList = ['Hotel']
categoryIdSkipList = ['3']
class jsonObject ():
    def __init__ (self, userInput = None, categorySkipList = None, categoryIdSkipList = None):
        self.data = None
        self.categorySkipList = categorySkipList
        self.categoryIdSkipList = categoryIdSkipList
        self.userInput = userInput
    def getData (self):
        return self.data
    def readFile (self, filePath):
        with open(filePath) as f:
            self.data = json.load(f)
    def getCleanedData (self):
        #Optional steps, to remove data clutter by removing
        #unused class.
        category_Keep_list = ["id", "category", "merchants", "valid_to"]
        bak_data = self.data
        for a in bak_data['offers']:
            for key in a.copy():
                if key not in category_Keep_list:
                    a.pop (key, None)
        return bak_data
    def filterOffer (self, offer):
        #step 1: checkin date += 5 (chac la lam ben ngoai luon)
        #Redundant step 2: Convert offer date from string to Num (Chac khong can lam)
        #Step 2 Actual: Convert checkin date to "YYYY-MM-DD" format and just simply
        # do string comparison with offer date
        if (self.categorySkipList != None):
            if (offer["category"] in self.categorySkipList):
                print ("Rejected, category: ", offer)
                return 0
        if (self.categoryIdSkipList != None):
            if (str(offer["id"]) in self.categoryIdSkipList):
                print ("Rejected, categoryID: ", offer)
                return 0
        if (self.userInput != None):
            if (offer["valid_to"] >= self.userInput) == False:
                print ("Rejected, valid date: ",offer)
                return 0
        print ("Accpeted: ",offer)
        return 1
    def getBestOffers(self):
        CleanedData = self.getCleanedData()
        for a in CleanedData['offers']:
            self.filterOffer (a)
        return 0

    
test = jsonObject (userInput, categorySkipList, categoryIdSkipList)
test.readFile (filePath)
test.getBestOffers()
