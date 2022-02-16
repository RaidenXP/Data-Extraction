import pandas as pd
import get_request_amt
import requests

def get_dataset(filename, rows=None):
    gameDB = pd.DataFrame(columns=["appid", "name", "developer", "publisher", "positive_rev", "negative_rev", "owners", 
                               "average_forever_playtime", "median_forever_playtime", "Concurrent_Users", "price", "initialprice",
                               "discount", "tags", "languages", "genre"])
    
    #our api that we are using
    url = "https://steamspy.com/api.php"

    #Add page amount here for more entries
    #The API only returns one page at a time with 1000 games
    #For more pages add more pages. Not really sure how many pages
    #There are
    responses = get_request_amt.getRequest(url, 4)

    current = 0
    for x in responses:
        if(current == rows):
            break

        anotherResp = requests.get(url, params='request=appdetails&appid=' + x).json()
        tempDB = pd.DataFrame({
            'appid': [anotherResp['appid']],
            'name': [anotherResp['name']],
            'developer': [anotherResp['developer']],
            'publisher':[anotherResp['publisher']],
            'positive_rev':[anotherResp['positive']],
            'negative_rev':[anotherResp['negative']],
            'owners': [anotherResp['owners']],
            'average_forever_playtime': [anotherResp['average_forever']],
            'median_forever_playtime': [anotherResp['median_forever']],
            'Concurrent_Users': [anotherResp['ccu']],
            'price': [anotherResp['price']],
            'initialprice': [anotherResp['initialprice']],
            'discount': [anotherResp['discount']],
            'tags': [anotherResp['tags']],
            'languages': [anotherResp['languages']],
            'genre': [anotherResp['genre']]
            })
        
        gameDB = pd.concat([gameDB, tempDB], ignore_index=True)

        current = current + 1
    
    gameDB.to_csv(filename)