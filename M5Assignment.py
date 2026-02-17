#Main program- Searches a website and returns the number and name
#of each link
import sys
from M5Formatsite import processSite
import M5SearchSite

running = True
print("Welcome to The Missing Link\n")

while(running):
    print("please enter a site to analyze or just enter to exit")
    domain = input("https://")
    if not domain:
        print("Goodbye")
        sys.exit(0)

    site = processSite(domain)
    print (f"You searched for {site}")

    myList = M5SearchSite.loadSite(site)
    if (len(myList) < 1):
        print("Nothing found")
        continue
    pauseToRead = input("Press Enter to see the list")

    for list in myList:
        print(list)