"""  
Given a url startUrl and an interface HtmlParser, 
implement a Multi-threaded web crawler to crawl all links that are under the same hostname as startUrl. 

Return all urls obtained by your web crawler in any order.

Your crawler should:

- Start from the page: startUrl
- Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
- Do not crawl the same link twice.
- Explore only the links that are under the same hostname as startUrl.

Note that getUrls(String url) simulates performing a HTTP request. 
You can treat it as a blocking function call which waits for a HTTP request to finish. 
It is guaranteed that getUrls(String url) will return the urls within 15ms.  
Single-threaded solutions will exceed the time limit so, can your multi-threaded web crawler do better?

Follow up:

1. Assume we have 10,000 nodes and 1 billion URLs to crawl. 
We will deploy the same software onto each node. The software can know about all the nodes. 
We have to minimize communication between machines and make sure each node does equal amount of work. 
How would your web crawler design change?

2. What if one node fails or does not work?

3. How do you know when the crawler is done?
"""

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from concurrent import futures
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {startUrl}
        host_name = self.getHostName(startUrl)
        
        # a pool of at most max_workers to threads to excecute getUrl calls asynchronously
        with futures.ThreadPoolExecutor(max_workers=16) as excecutor:
            # schedule a callable to excecute getUrls on the given url
            tasks = deque([excecutor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                url_future = tasks.popleft()
                try:
                    urls = url_future.result(timeout=15)
                    for url in urls:
                        if self.getHostName(url) == host_name and url not in visited:
                            visited.add(url)
                            # do getUrls on the current url
                            tasks.append(excecutor.submit(htmlParser.getUrls, url))
                except Exception as e:
                    print('%r generated an exception: %s' % (url, e))
        
        return list(visited)
    
    def getHostName(self, url: str):
        return url.split('/')[2]