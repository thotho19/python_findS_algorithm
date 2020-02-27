data=[['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
      ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
      ['Rainy','Cold','High','Strong','Warm','Change','No'],
      ['Sunny','Warm','High','Strong','Cool','Change','Yes']
     ]
def nestedListsChecker(data): # this function to check the length of each nested lists inside data 
    lenSize = len(data[0]) #init length
    comparingState = True #init boolean variable
    for d in data: 
        if lenSize != len(d): #if the nested lists length is not equail then false 
            comparingState = False
        else:                #else do nothing
            pass
    return comparingState  #return the boolean 

def findS(data):
    h = []   #init empty list
    for d in range(len(data[0])-1): #append first nested list to h list for comparing 
        h.append(data[0][d])
    for d in data:
        if d[len(d)-1] == 'Yes': #finds Alogrithm training only on positive class +ve (no -ve) 
            for i in range(len(d)-1):
                if h[i] != d[i]: 
                    h[i] = '?'
    return h

State = nestedListsChecker(data)
if State != True:
    print('Error the length of attributes is not equivalent')
else:
    hypothesis = findS(data)

print("Most Hypothesis:",hypothesis)

