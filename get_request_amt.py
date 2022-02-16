import requests
import time

#The API only gives one page of games. Each page has 1000 entries
#If more pages are needed just add more pages to the function parameter
def getRequest(url, pageAmt=1):
    appId = []

    for x in range(pageAmt):
        response = requests.get(url, params='request=all&page=' + str(x)).json()
        for y in response.keys():
            appId.append(str(y))
        
        #pause a bit for the next page of requests
        time.sleep(5)
    
    return appId