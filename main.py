import json
import utils
userInput = "2020-11-10"
filePath = 'input.json'
print (utils.addDate (userInput, 5))

class jsonObject ():
    def __init__ (self):
        self.data = None
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
    def filterOffer (offer):
        #step 1: checkin date += 5 (chac la lam ben ngoai luon)
        #Redundant step 2: Convert offer date from string to Num (Chac khong can lam)
        #Step 2 Actual: Convert checkin date to "YYYY-MM-DD" format and just simply
        # do string comparison with offer date
        if date_compare (offer["valid_to"], input_date) == True:
            return 0
        return 1

    
test = jsonObject ()
test.readFile (filePath)
