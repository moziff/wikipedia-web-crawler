# wikipedia-web-crawler

DOCUMENTATION

Steps to run program:

1. BeautifulSoup Installation: pip install beautifulsoup4

2. Requests Installation: pip install requests

3. Plotly Installation: pip install plotly

4. Run Program: python philosophy.py



Warning: Will take a few minutes to make full distribution show up. You will still see the program choosing first links though. Recursive loops will eventually get out after 35 links



•  What percentage of pages often lead to philosophy?



        97.52 percent of all links have gone to Philosophy Page. Total Links: 500  Successful Links: 472  Unsuccessful Links: 28

       My Percentage = 97.52% ----> Wikipedia Percentage for 2011 = 94%



•  Using the random article link (found on any wikipedia article in the left sidebar),what is the distribution of

   path lengths for 500 pages, discarding those paths that never reach the Philosophy page?



  The average path length to Philosophy page was 13 links.  Log-Normal distribution (could also probably fit a Normal distrib. as well, but is clearly skewed left).

   I used the plotly python module to create a bar chart in order to show the distribution.

   <Inline image 1>


    key: path length (number of links to get to Philo Page)  |  value: number of occurrences of path length

   distribution_data={4: 4, 5: 2, 6: 3, 7: 5, 8: 15, 9: 49, 10: 52, 11: 33, 12: 34, 13: 47, 14: 41, 15: 41, 16: 37, 17: 25, 18: 21, 19: 17, 20: 10, 21: 7, 22: 7, 23: 7, 24: 6, 25: 3, 26: 4, 27: 1, 29: 1, 'unavailable': 28}



•  How can you reduce the number of http requests necessary for 500 random starting pages?

  An ideal way to solve this problem would be to cache each of the requests with their paths to the philosophy page in a database.


  For example, whenever the first link of a page is https://en.wikipedia.org/wiki/Science, the application should know that the next paths will always be: https://en.wikipedia.org/wiki/Knowledge --> https://en.wikipedia.org/wiki/Awareness --> https://en.wikipedia.org/wiki/Conscious --> https://en.wikipedia.org/wiki/Quality_(philosophy) --> https://en.wikipedia.org/wiki/Philosophy. Bingo! You do this 500 times and you will see a lot more patterns with different links. If we store all of those, including the recursive links in the database, then we will only have to make a request for the unknown links, which will end up substantially reducing the number of total requests. Over 80% of links go to the philosophy page, so inevitably there will be overlap amongst the paths.
Status API Training Shop Blog About
