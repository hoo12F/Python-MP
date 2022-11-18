import requests
get = requests.get('https://quote-garden.herokuapp.com/api/v3/quotes/random')
if get.status_code == 200:
    jsonStuff = get.json()
    data = jsonStuff['data']

    print(data[0]['quoteText'])

else:
    print("Error. Different status code detected")
    print(get.status_code)
    quit()