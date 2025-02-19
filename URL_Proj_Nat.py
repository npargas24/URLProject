#Store URL
#Return shortened version of URL =  
        #unique id that is less than 12 ASCII characters.
#https://www.geeksforgeeks.org/components-of-a-url/
    #Scheme : https://
    #Subdomain : https://www.
    #identifier: >12 identifier for specific url
    #3. Domain Name : https://www.example.
    #4. Top-level Domain : https://www.example.co.uk
    #5. Port Number : https://www.example.co.uk:443
    #6. Path : https://www.example.co.uk:443/blog/article/search
    #7. Query String Separator : https://www.example.co.uk:443/blog/article/search?
    #8. Query String : https://www.example.co.uk:443/blog/article/search?docid=720&hl=en
    #9. Fragment : https://www.example.co.uk:443/blog/article/search?docid=720&hl=en#dayone
#shortened URL has:
    #Scheme : https://
    #Domain name: https://example.com
    #IndvName: https://example.com/short123

#count the number of URL’s that have been shortened so far
#can accept user input as text given a prompt



#Make a Long URL class
#Make a Short URL class
#Break the components of Long URL class 

'''import csv

class LongUrl:
    def __init__(self, scheme, subdomain, domainName, topLevelDomain, portNumber, path, queryStringSeparator, queryString, fragment):
        self.scheme = scheme
        self.subdomain = subdomain
        self.domainName = domainName
        self.topLevelDomain = topLevelDomain
        self.portNumber = portNumber
        self.path = path
        self.queryStringSeparator = queryStringSeparator
        self.queryString = queryString
        self.fragment = fragment

    def longComp(self, long_url):

        #url_parts = long_url.split("//:")
        #scheme = url_parts[0]
        #url_rem = url_parts[1]
        #keep cutting
        #for part in url_rem.split("/")
        chunk1 = ""
        chunk2 = ""
        for char in long_url:
            chunk1 = chunk1 + char
            if chunk1 == 'https://':
                self.scheme = chunk1
                long_url = long_url - chunk1
                for char in long_url:
                    chunk2 = chunk2 + char
                    if chunk2 == 'www.':
                        domainName = chunk2
                        long_url = long_url - chunk2'''

from typing import List

class Url():
    valid : bool = False
    proto : str = ""
    domain : str = ""
    port : str = ""
    path : List[str] = ""
    query : str = ""
    fragment : str = ""
    miniurl : str = ""

def parse_url(long_url : str) -> Url:

    url = Url()
    url_parts = long_url.split("//:")
    if len(url_parts) != 2:
        return url
    url.proto = url_parts[0]
    url_rem = url_parts[1]

    if ":" in url_rem:
        url_splits = url_rem.split(":")
        if len(url_splits) != 2:
            return url
        url.domain = url_splits[0]
        splits = url_splits[1].split("/")
        if len(splits) >= 2:
            url.port = splits[0]
        else:
            return url
    else:
        url_splits = url_rem.split("/")
        if len(url_splits) < 2:
            return url
        url.domain = url_splits[0]

    cnt : int = 0

    if "?" in url_rem:
        url_splits = url_rem.split("?")
        splits = url_splits[0].split("/")
        for split in splits:
            if cnt == 0:
                pass
            if cnt > 1:
                url.path.append(split)
            cnt += 1

    #finish parsing here


def minify(long_url : str) -> Url:

    url = parse_url(long_url)
    #do minifying here
    return url

url = minify("https://www.youtube.com/watch?v=a51CXCRuZd0")

#do it a different way, set up different functions that scan to see what thing matches given a long url
#ex scan the long_url input and see what matches 'https://' and tht function is scheme
#function for subdomain will take in whatever comes after https:// and ends with a .
#domain takes in whatever comes after top level domain and ends with dot
                







#long_url = input("Please enter your URL: ")