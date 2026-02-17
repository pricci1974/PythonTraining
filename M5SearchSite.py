#This script conducts the actual search of the website
#then using regular expressions identifies the number and names
#of all the links. Returns the list to the main program
import urllib.request as request
import re as regEx

def loadSite(url):
    try:
        with request.urlopen(url) as response:
            html_content = response.read()
            decodedString = html_content.decode("utf-8")
    
            link_list = regEx.findall(r'href=["\']?([^"\' >]+)', decodedString)
            print(f"Found {len(link_list)} links:")
            return link_list
    except:
        print("Could not open site")
        return []
