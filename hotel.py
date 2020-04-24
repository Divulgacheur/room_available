import requests
import pprint
import re
import time

def get_av(hotel):
    headers = { 'x-OTL-api-key': 'Your own API key for your account' }

    params = (
        ('hotelCodes', hotel),

        ('rateCodes', 'IGCOR'), 

        ('startDate', '2020-05-10T00:00:00Z'),
        ('endDate', '2020-06-29T00:00:00Z'),
        ('lengthOfStay', '1'),
    )

    response = requests.get('https://apis.OTL.com/availability/v1/windows', headers=headers, params=params)
    

    #pprint.pprint(response.json() )
    
    try:
        for i in response.json()['hotels'][0]['rates'][0]['windows']:
            monnaie = response.json()['hotels'][0]['currencyCode']
            print(i['startDate'],i['totalAmount'],monnaie )
        time.sleep(2)

    except:
        print('pas dispo\n')
    return response

def get_hotels(state,city):
    
    url = 'https://www.OTL.com/destinations/fr/fr/'+state+'/'+city+'-hotels'
    print(url)
    response = requests.get(url)

    resultats = re.findall('name: "([^\n]*)",\n[^\n]*\n[^\n]*\n[^\n]*\n[^\n]*\n[^h]*hotelCode: "([^"]*)",', response.text, flags=re.S)
        
    
    total = str(len(resultats))
    pprint.pprint(resultats)
    print(total+' hotel(s) à '+city)
    return resultats

get_av('MRSHA') #show all availibility for 1 night stay at the Intercontinental Marseille - Hotel Dieu (hotel code MRSHA) - from 10/05/2020 to 29/06/2020





for hotel in get_hotels('france','paris'): # show same but for all Paris's OTL hotels
    print('\n\n'+hotel[0]+'\n')
    get_av(hotel[1])

