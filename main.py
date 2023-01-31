from json import load

arrAll = []

def readFilesJSON(file1,file2):
    with open(file1) as f:
        ## Destinations file
        datadest = load(f) 
    with open(file2) as f:
        ## Drivers file
        datadriv = load(f)
    return datadest['shipments'],datadriv['drivers']

def getVowels(string):
    count = 0
    ucount = 0
    for word in string:
        if word.lower() in "aeiou":
            count += 1
        if word.lower() in ('bcdfghjklmnñpqrstvwxyz'):
            ucount += 1
    return count ,ucount 

def getBaseScore(str1,str2):
    destName = str1.lower()
    driver = str2.lower()
    vowels, uvowels = getVowels(driver)  
    if len(destName) % 2 == 0:
        return 1.5 * vowels
    else:
        return 1 * uvowels
    
def getScore(str1,str2):
    baseScore = getBaseScore(str1, str2)
    assignments = {}
    
    if (len(str1) > 1 and len(str2) > 1 and len(str1) == len(str2)):
        baseScore += baseScore * .5	

    assignments['Address']=str1
    assignments['Driver']=str2 
    assignments['Score']=baseScore

    arrAll.append(assignments)
    return baseScore

def matchDestinations(arrdest,arrdriv):
    score = 0    
    matches = dict()
    
    for destination in arrdest:
        bestDriver = ''
        bestScore = ''
        for driver in arrdriv:
            score = getScore(destination, driver)
   
if __name__ == "__main__":
    
    count = 0
    try:
        ## Run funtionto read files
        destinations, drivers = readFilesJSON('destinations.json','drivers.json')

        ## Run funtion to get Score
        matchDestinations(destinations, drivers)

        ## Sort array by Score
        arrSort=sorted(arrAll, key=lambda k: k['Score'], reverse=True)
        
        ## Sort aarrSort by Address
        arrSort2=sorted(arrSort, key=lambda k: k['Address'], reverse=True)
 
        arrFinally = []
  
    
        for i in arrSort2:
            if count == 0:
                arrFinally.append(i)
            aaddress = {item['Address']:item for item in arrSort2}

            if  count==len(aaddress):
                result = [x for x in arrFinally if x["Driver"]==i['Driver']]
                if(result):
                    continue;
                else:
                    arrFinally.append(i)                  
                count=1
            count = count + 1
        #print(arrFinally)  
          
        for f in arrFinally:
            print("Match " + "Destination: " + f['Address']+ "| Driver: " + f['Driver']+ "| Score: " + str(f['Score']))    
    
    except:
        print('Fail, please check files')

    
