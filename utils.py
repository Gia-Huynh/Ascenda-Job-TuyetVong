def addDate (stringInput, addNum):
    def addDate (Y, M, D, addNum):
        #Y, M, D = Year, Month, Day
        #addNum = number of days to add
        def getDayInMonth ():
            Days_In_Month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (M!=2):
                return Days_In_Month [M]
            elif (Y % 4 == 0):
                if (Y % 100 == 0):
                    if (Y % 400 == 0):
                        return 29
                    return 28
                return 29
            else:
                return 28
        while (addNum > 0):
            #Some optimization can be done here, instead of
            # adding 1 by 1 to D,
            # we can add the Day in Month minus 1 straight into D
            # Done, the above sentence is incorrect, but hey
            # Tested and made sure that it's working
            #print (addNum, ' ', D,' ',getDayInMonth ())

            if (getDayInMonth() - D < addNum):
                addNum = addNum - (getDayInMonth() - D)
                D = getDayInMonth()
                
            D = D + 1
            if (D - 1 == getDayInMonth ()):
                D = 1
                M = M+1
                if (M == 13):
                    Y = Y+1
                    M = 1
            addNum = addNum - 1
        return Y, M ,D
    #Y = int(stringInput.split('-')[0])
    #M = int(stringInput.split('-')[1])
    #D = int(stringInput.split('-')[2])
    T = stringInput.split('-')
    Y, M, D = addDate (int (T[0]),int (T[1]),int (T[2]),addNum)
    result = f'{Y:04d}-{M:02d}-{D:02d}'
    return result
