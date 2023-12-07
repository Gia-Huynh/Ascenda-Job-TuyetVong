import json
import utils
userInput = "2019-12-25"
filePath = 'input.json'
dateRange = 5
userInput = utils.addDate (userInput, dateRange)
categorySkipList = ['3']
class jsonObject ():
    def __init__ (self, userInput = None, categorySkipList = None, numOfferNeeded = 2):
        self.data = None
        self.categorySkipList = categorySkipList
        self.userInput = userInput
        #This class should only return 2 offers even though there are several eligible offers
        #Make it N possible offers
        self.numOfferNeeded = numOfferNeeded
    def getData (self):
        return self.data
    def readFile (self, filePath):
        with open(filePath) as f:
            self.data = json.load(f)
    def getCleanedData (self, debugMode = 0):
        data = self.data
        #"If an offer is available in multiple merchants, only select the closest merchant"
        for offer in data ['offers']:
            if len (offer['merchants'])>1:
                bestMerchant = offer['merchants'][0]
                for merchant in offer['merchants']:
                    if (merchant['distance'] < bestMerchant['distance']):
                        bestMerchant = merchant
                offer['merchants'].clear()
                offer['merchants'].append (bestMerchant)
        if (debugMode == 0):
            return data
        #Optional steps, to remove data clutter by removing
        #unused class. Used while debugging to return only important information.
        category_Keep_list = ["id", "category", "merchants", "valid_to"]
        for offer in data['offers']:
            for key in offer.copy():
                if key not in category_Keep_list:
                    offer.pop (key, None)
        return data
    
    def ValiDate (self, offer):
        #Heh, Validate date
        #Validate if offer is valid up to the day that the user inputs + 5 days.
        #Also return false if category is in the banned category list.

        #Check for None in case there is no rule defined
        if (self.categorySkipList != None):
            if (str(offer["category"]) in self.categorySkipList):
                return False
        if (self.userInput != None):
            if (offer["valid_to"] >= self.userInput) == False:
                return False
        return True
    
    def getBestOffers(self):
        Data = self.getCleanedData(0)

        #One liner: sorted([offer for offer in Data['offers'] if self.ValiDate (offer)], key=lambda d: d['merchants'][0]['distance'])
        #Nhung chac chan khong doc duoc roi

        #chua duoc sort, se sort o duoi
        sortedOffer = [offer for offer in Data['offers'] if self.ValiDate (offer)]
        idx = [i for i in range (0, len(sortedOffer))]
        #If there are multiple offers in the same category *give priority to the closest merchant offer*.
        #If there are multiple offers with different categories, *select the closest merchant offers when selecting 2 offers*.
        pos = 0
        sortedOffer = sorted(sortedOffer, key=lambda d: d['merchants'][0]['distance'])
        #Gnomesort, cuz I'm lazy coding this
        #while (pos + 1 < len(idx)):
        #    if (pos == 0) or (sortedOffer[idx[pos]]['merchants'][0]['distance'] > sortedOffer[idx[pos-1]]['merchants'][0]['distance']):
        #        pos = pos+1
        #    else:
        #        #swap idx[pos] with idx[pos-1]
        #        idx[pos] = idx [pos] + idx[pos-1]
        #        idx[pos-1] =  idx [pos] - idx[pos-1]
        #        idx [pos] =  idx [pos] - idx[pos-1]
        #        pos = pos-1
        #sortedOffer = [sortedOffer[i] for i in range (0, len(idx))]
        #print (sortedOffer)
        count = 0
        selectedOffers = []
        for i in range (0, len(idx)):
            if (count == self.numOfferNeeded):
                break
            #"selected offers should be in different categories"
            categoryExistCheck = 0
            for a in selectedOffers:
                if (a['category'] == sortedOffer[idx[i]]['category']):
                    categoryExistCheck = 1
                    break
            if (categoryExistCheck == 0):
                selectedOffers.append (sortedOffer[idx[i]])
            count = count + 1
        result = {'offers':selectedOffers}
        return result

    
test = jsonObject (userInput, categorySkipList)
#test = jsonObject ()
test.readFile (filePath)
result = test.getBestOffers()
with open('output.json', 'w') as f:
  json.dump(result, f, ensure_ascii=False, indent=2)
