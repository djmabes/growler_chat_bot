#!/usr/bin/env python
# coding: utf-8

# Name: Daniel Mabie and Elliot Ansari   
# Purpose: Final Project  
# Date last updated: 5/9/2020  
# ENGR 120  

# In[1]:


# import libraries run first
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:


# scrape URL functions, 
def scrape(url):
    """Returns parsed HTML content for desired url"""
    
    # open and read HTML file
    response = urlopen(url)
    content = response.read()
    
    # parse HTML file
    soup = BeautifulSoup(content, 'html.parser')
    return soup


# In[3]:


def beerscraper(beer_urls):
    """Returns top 3 beers for each modified pre-scraped beer url"""
    
    # This finds all available "beer items" at the scraped url
    beer = beer_urls.find_all(class_="beer-container beer-list pad")
    items = beer_urls.find_all(class_= 'beer-item')
    
    # this is a boolean to return "True" if no beers are available at the url
    if len(items) == 0:
        return(True)
    
    # this stops the function from returning more than 3 beer names and changes the scraped beer details into readable text
    else:
        count=0
        for item in items:
            if count >= 3:
                break
            details = item.find(class_= 'beer-details')
            name = details.find(class_= 'name')
            print(name.text)
            count+=1
    
        


# The following code is our **Growler Chat Bot**. It takes users input of their preferred country, beer style, and finally beer type, and returns the top three recommended beers from that specific country based on their preferences. It will run until the user decides they are done finding beers. ***Happy crushing!*** 

# In[ ]:


while True:

# Growler introduction

    proceed = input('''Cheers! Welcome to Growler, a beer lovers best friend. If you would like to recieve personal
beer recommendations from a select list of countries please respond with "Yes". If you would 
like to exit Growler please say "No".
    ''').lower()
    while proceed not in ["yes", "no"]:
        print('Sorry that is not a valid response. Please try again.')
        proceed = input('''Cheers! Welcome to Growler, a beer lovers best friend. If you would like to recieve personal
beer recommendations from a select list of countries please respond with "Yes". If you would 
like to exit Growler please say "No".
    ''').lower()
    if proceed == "yes":
        print('Perfect! Let\'s get started.')

        # Takes users input on what country they are interested in

        user_country = input("""Of the following ten countries, please pick one that you want beer recommendations from.
United States
Germany
Brazil
England
Japan
Belgium
Ireland
Italy
South Africa
Mexico
    """).lower()
        while user_country not in ["united states", "germany", "brazil", "england", "japan", "belgium", "ireland", "italy", "south africa", "mexico"]:
            print("Sorry, that is not a valid country. Please try again.")
            user_country = input("""Of the following ten countries, please pick one that you want beer recommendations from.
United States
Germany
Brazil
England
Japan
Belgium
Ireland
Italy
South Africa
Mexico
    """).lower()
        if user_country == "united states":
            print("Great! You will recieve beer recommendations from the United States.")
        elif user_country == "germany":
            print("Great! You will recieve beer recommendations from Germany.")
        elif user_country == "brazil":
            print("Great! You will recieve beer recommendations from Brazil.")
        elif user_country == "england":
            print("Great! You will recieve beer recommendations from England.")
        elif user_country == "japan":
            print("Great! You will recieve beer recommendations from Japan.")
        elif user_country == "belgium":
            print("Great! You will recieve beer recommendations from Belgium.")
        elif user_country == "ireland":
            print("Great! You will recieve beer recommendations from Ireland.")
        elif user_country == "italy":
            print("Great! You will recieve beer recommendations from Italy.")
        elif user_country == "south africa":
            print("Great! You will recieve beer recommendations from South Africa.")
        elif user_country == "mexico":
            print("Great! You will recieve beer recommendations from Mexico.")

        # Takes users input on what style of beer they are interested in

        user_beer_style = input("""Which style of beer are you interested in?
IPA
Belgian
Pilsner
Stout
Pale Ale
Cider
Porter
Bock
Brown Ale
Sour
    """).lower()
        while user_beer_style not in ["ipa", "belgian", "pilsner", "stout", "pale ale", "cider", "porter", "bock", "brown ale", "sour"]:
            print("Sorry, that is not a valid style of beer. Please try again.")
            user_beer_style = input("""Which style of beer are you interested in?
IPA
Belgian
Pilsner
Stout
Pale Ale
Cider
Porter
Bock
Brown Ale
Sour
    """).lower()
        if user_beer_style == "ipa":
            user_beer_type = input("""Which type of IPA are you interested in? 
New England
Triple
Imperial Double
    """).lower()
            while user_beer_type not in ["new england", "triple", "imperial double"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of IPA are you interested in? 
New England
Triple
Imperial Double
    """).lower()
        elif user_beer_style == "belgian":
            user_beer_type = input("""Which type of Belgian are you interested in?
Blonde
Dubel
Strong Dark Ale
    """).lower()
            while user_beer_type not in ["blonde", "dubel", "strong dark ale"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Belgian are you interested in?
Blonde
Dubel
Strong Dark Ale
    """).lower()
        elif user_beer_style == "pilsner":
            user_beer_type = input("""Which type of Pilsner are you interested in?
German
Imperial Double
Other
    """).lower()
            while user_beer_type not in ["german", "imperial double", "other"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Pilsner are you interested in?
German
Imperial Double
Other
    """).lower()
        elif user_beer_style == "stout":
            user_beer_type = input("""Which type of Stout are you interested in?
Coffee
Irish Dry
Milk Sweet
    """).lower()
            while user_beer_type not in ["coffee", "irish dry", "milk sweet"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Stout are you interested in?
Coffee
Irish Dry
Milk Sweet
    """).lower()
        elif user_beer_style == "pale ale":
            user_beer_type = input("""Which type of Pale Ale are you interested in?
American
Milkshake
English
    """).lower()
            while user_beer_type not in ["american", "milkshake", "english"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Pale Ale are you interested in?
American
Milkshake
English
    """).lower()
        elif user_beer_style == "cider":
            user_beer_type = input("""Which type of Cider are you interested in?
Dry
Sweet
Traditional
    """).lower()
            while user_beer_type not in ["dry", "sweet", "traditional"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Cider are you interested in?
Dry
Sweet
Traditional
    """).lower()
        elif user_beer_style == "porter":
            user_beer_type = input("""Which type of Porter are you interested in?
Coffee
Double
American
    """).lower()
            while user_beer_type not in ["coffee", "double", "american"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Porter are you interested in?
Coffee
Double
American
    """).lower()
        elif user_beer_style == "bock":
            user_beer_type = input("""Which type of Bock are you intereseted in?
Doppelbock
Eisbock
Weizenbock
    """)
            while user_beer_type not in ["doppelbock", "eisbock", "weizenbock"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Bock are you intereseted in?
Doppelbock
Eisbock
Weizenbock
    """)
        elif user_beer_style == "brown ale":
            user_beer_type = input("""Which type of Brown Ale are you interested in?
American
Belgian
English
    """).lower()
            while user_beer_type not in ["american", "belgian", "english"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input(""""Which type of Brown Ale are you interested in?
American
Belgian
English
    """).lower()
        elif user_beer_style == "sour":
            user_beer_type = input("""Which type of Sour are you interested in?
Gose
Fruited
Other
    """).lower()
            while user_beer_type not in["gose", "fruited", "other"]:
                print("Sorry, that is not a valid response. Please try again.")
                user_beer_type = input("""Which type of Sour are you interested in?
Gose
Fruited
Other
    """).lower()

        # Changes their inputs into URL format
        country_url_insert = user_country.replace(" ", "-")
        beer_url_insert = user_beer_style + "-" + user_beer_type
        beer_url_insert = beer_url_insert.replace(" ", "-")

        # add to base URL so that the scrape function will work depending on user's input

        # base url = https://untappd.com/beer/top_rated?type=xxx&country=xxx 
        # the "xxx" denote where users input needs to be inserted
        
        # inserts users input into the base url
        beer_url = "https://untappd.com/beer/top_rated?type=%s&country=%s" % (beer_url_insert, country_url_insert)
        
        #scrapes the newly made custome beer_url
        beer_rec = scrape(beer_url)
        
        #prints a blank line so they can clearly see their recommended beers
        print()
        
        # Gives the recommendations to the user
        
        # Returns a "sorry" message if the beersraper function returns 0 results
        if beerscraper(beer_rec) == True:
            print("Sorry, there are no beers available for that type in that country. Please try again!")
        
        # Prints their recomended beers, thanks them, and gives them the option to continue with the Growler bot
        else:
             print( "Above are the top " + user_beer_style + " style " + user_beer_type + "s " + "from " + user_country.capitalize() +                    ". Here is the link to learn more about those beers! " + beer_url + " Thanks for using Growler!")
        

    elif proceed == "no":
        print("Thanks for using Growler! Go crush some cans!")
        break


# In[ ]:




