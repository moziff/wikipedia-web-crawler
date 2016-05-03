from bs4 import BeautifulSoup, SoupStrainer
# indications on stack overflow point to Beautiful Soup to be like Nokogiri for ruby
import requests
import re
import plotly.plotly
import plotly.graph_objs as go

class RandomPhilosophyWiki:

    page_philo=0
    total=0

    def __init__(self):
        self.page_distribution={'unavailable': 0} #cache each request to show page distribution

    def web_crawler(self):
        url = 'http://en.wikipedia.org/w/index.php?title=Special:Random' #random url
        r = requests.get(url)
        data = r.text #HTML source of the page
        soup = BeautifulSoup(data,"html.parser") #Create BeautifulSoup object from HTML
        print(r.url)
        original_page=r.url # URL of current page
        i=0 # link count to philo page

        while (r.url != 'https://en.wikipedia.org/wiki/Philosophy') and i<35: # keep running unless Philosophy page is reached or unless it is recursive
            count=0
            first_link=None
            while first_link == None: # iterates through each paragraph until it finds it's first link
                if count>(len(soup.select('div#mw-content-text > p'))-1): # if no links on page add to unavailable pile
                    print "\nNo links found on page.\n"
                    self.page_distribution['unavailable']+=1
                    return
                paragraph = soup.select('div#mw-content-text > p')[count] #find paragraph with first real link
                for span in paragraph.find_all("span"):
                    span.replace_with("")# remove all spans(i tags)
                para = str(paragraph)
                para = re.sub(r' \(.*?\)', '', para) # remove parantheses ....not really familiar with regex
                paragraph = BeautifulSoup(para,"html.parser") # create soup of paragraph to find first link
                first_link = paragraph.find(href = re.compile('/wiki/'))
                count+=1

            url = 'http://en.wikipedia.org' + first_link.get('href') #final url for next page
            r = requests.get(url)
            soup = BeautifulSoup(r.text,"html.parser")
            print(r.url) # prints first link of page to console
            i+=1
        if i==35: # if in recursive loop add link to unavailable pile
            self.page_distribution['unavailable']+=1
        else:
            self.page_philo+=1 # add successful page to
            try:
                self.page_distribution[i]+=1 # the number of occurences of path length, i.e. there have been 5 times that it took 15 links to get to philo page
            except KeyError: # if key value pair didnt exist
                self.page_distribution[i]=1
        self.total+=1
        self.percentage = (self.page_philo/float(self.total))*100
        print "\nCount to get to Philosophy Page: ",i
        print "\n",self.percentage,"percent of all links have gone to Philosophy Page. Total Links:",self.total," Succesful Links:",self.page_philo,"\n"


    def distribution_500(self):
        i=0
        while i <500: # iterate through 500 random links
            self.web_crawler() # web crawler to get to Philo
            i+=1
            print self.page_distribution
            print("\nkey: # of links to philo page (path length) | value: occurences of path length #\n")

        self.plot(self.page_distribution)

    def distribution_15(self):
        i=0
        while i <15:
            self.web_crawler()
            i+=1
            print "Distribution = ",self.page_distribution
            print("\nFor Distribution -- key: # of links to philo page (path length) | value: occurences of path length #\n")

        self.plot(self.page_distribution)


    def plot(self,distrib_dict):
        i=0
        average=0
        total=0
        # print distrib_dict.keys()
        while i<len(distrib_dict.keys()):
            if isinstance(distrib_dict.keys()[i],int):
                average+=distrib_dict.keys()[i]*distrib_dict.values()[i]
                total+=distrib_dict.values()[i]
            i+=1
        average=average/int(total)
        print "\nThe average path length to Philosophy page was ",average,"links.\n"
        plotly.offline.plot({
            "data": [
                plotly.graph_objs.Bar(x=distrib_dict.keys(),y=distrib_dict.values())
            ]
        })

random = RandomPhilosophyWiki()
# random.distribution_500() # -----> use to go through 500 random links
random.distribution_15() # ------> use to go through 15 random links
