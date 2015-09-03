import random 

class StringQuestions():

    def convertToFloat(self):
        #The string given to process 
        toBeConverted = 'A-DSPAM-Confidence: 0.8475'
        #getting the index of the char 2 columns after the colon ie: index of 0
        indexOfColon = toBeConverted.find(' ') + 1
        #using that index to  slice the given string down to only include chars from that point on
        portionAfterColon = toBeConverted[indexOfColon:]
        #converting that portion of the string to a float and return it
        floatOfPortionAfterColon = float(portionAfterColon)
        return floatOfPortionAfterColon
    
    def convertFileToUpperCase(self, fileName):
        #get the file
        text = self.getFileByName(fileName)
        #print it line by line
        self.printLineByLine(text)

    def getFileByName(self, fileName):
        return open(fileName)

    def toUpperCase(self, text):
        return text.upper()

    def printLineByLine(self, text):
        for line in text:
            print self.toUpperCase(line)

class CoinToss():
    def toss(self):
        return random.choice([0, 1])

    def customTosser(self, number, doSomething, doEvery):
        heads = 0
        tails = 0
        tossed = 0
        #toss the coin the number of times requested
        for i in range(number): #range has start defaulted to 0
            result = self.toss()
            #decide if it was heads or tails
            if(result == 0):
                heads = heads + 1
            else:
                tails = tails + 1
            #increase the counter for the number of tosses completed
            tossed = tossed + 1
            #do the requested action if it is at the requested interval ie 100 % 100 = 0 therefore do the action
            if(tossed % doEvery == 0):
                doSomething([heads, tails])
        #return a list with two items the number of heads and the number of tails
        return [heads, tails]

    def getProportion(self, a, b):
        #get proportion as a float
        return float(a) / float(b)

    def questionOne(self):
        def doThis(res):
            #we were asked to print the proportion of the rsults minus 1/2, 1/2 => 0.5
            print(self.getProportion(res[0], res[1]) - 0.5)

        def nowDoThis(res):
            #for part two we need to print the proportion of results minus 1/2 AND
            #print the number of heads less half the number of tosses
            # this number approaches zero because as N increases the number of heads results will approach 50%
            doThis(res)
            print(res[0] - 2500)


        self.customTosser(5000, doThis, 100)
        print('No these numbers appear to be approaching 0.5 not 0 as N increases')

        self.customTosser(5000, nowDoThis, 100)
        print('the number of heads less half the number of tosses appears to be approaching zero as N increases')

    def questionTwo(self):
        results = [0, 0]
        # this function returns true if the proportion of toss results is within the
        #parameters given by the question ie p is within 0.1 of 0.5
        def isWithinParams(res):
            p = self.getProportion(res[0], res[1]) - 0.5
            return p > 0.4 and p < 0.6 

        def doThis(res):
            #record the results of each run of the experiement
            if(isWithinParams(res)):
                results[0] = results[0] + 1
            else:
                results[1] = results[1] + 1

        #run the experiment 100 times
        for i in range(100):
            self.customTosser(1500, doThis, 1500)
        

        print('the proportion of results within our params was :')
        print(results[0], results[1])
        print('N needs to be approximately 1200 - 1500 to so that approx 95 out of 100 times the proportion of heads is between .4 and .6')




def run():
    print('Mark Moore solutions for CS-583 - Week 1')
    print('Informatics Problem 6.14.5:') 
    print('When you slice the given string after the colon and convert to a float you get %s' % StringQuestions().convertToFloat())
    print('Informatics Problem 7.11.1:')
    print('The required file in uppercase is:')
    StringQuestions().convertFileToUpperCase('./app/mobox-short.txt')
    print('Probability Page 12, Problem 1')
    CoinToss().questionOne()
    print('Probability Page 12, Problem 2')
    CoinToss().questionTwo()


if __name__ == '__main__':
    run()
