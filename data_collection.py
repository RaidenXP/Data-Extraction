import pandas as pd
import get_request_amt
import requests

def get_dataset(filename, rows=None):
    gameDB = pd.DataFrame(columns=["appid", "name", "developer", "publisher", "positive", "negative", "owners", 
                               "average_forever", "median_forever", "ccu", "price", "initialprice",
                               "discount", "tags", "languages", "genre"])
    
    url = "https://steamspy.com/api.php"

    responses = get_request_amt.getRequest(url)

    current = 0
    for x in responses:
        if(current == rows):
            break

        anotherResp = requests.get(url, params='request=appdetails&appid=' + x).json()
        gameDB = gameDB.append({
            'appid': anotherResp['appid'],
            'name': anotherResp['name'],
            'developer': anotherResp['developer'],
            'publisher':anotherResp['publisher'],
            'positive':anotherResp['positive'],
            'negative':anotherResp['negative'],
            'owners': anotherResp['owners'],
            'average_forever': anotherResp['average_forever'],
            'median_forever': anotherResp['median_forever'],
            'ccu': anotherResp['ccu'],
            'price': anotherResp['price'],
            'initialprice': anotherResp['initialprice'],
            'discount': anotherResp['discount'],
            'tags': anotherResp['tags'],
            'languages': anotherResp['languages'],
            'genre': anotherResp['genre']
            }, ignore_index=True)
        
        current = current + 1
    
    gameDB.to_csv(filename)