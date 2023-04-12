import requests
import webbrowser
import json
def get_details(query):
    Api = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyAf9Po1YJtv7JTdQGVj_qCX1ZKYd2I0_u0&cx=31bfd5557d3024a45&q={}'.format(query)
    response = requests.get(url=Api)
    print(response)
    count=response.json()['queries']['request'][0]['count']
    title=response.json()['items'][0]['link']
    print(title)
    print(count)
    message=""
    if count<5:
        for i in range(count):
            link=response.json()['items'][i]['link']
            title=response.json()['items'][i]['title']
            link1 = link + '\n'
            message +='['+title+']'+'('+link1+')' + '\n' + '\n'
        return message
    
    else:
        for i in range(5):
            link=response.json()['items'][i]['link']
            title=response.json()['items'][i]['title']
            link1 = link + '\n'
            message +='['+title+']'+'('+link1+')' + '\n' + '\n'
        return message
    

# print(get_details("covid"))    