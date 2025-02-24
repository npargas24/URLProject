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


import csv
import urllib.parse
from typing import List

class LongUrl:
    def __init__(self, scheme="", subdomain="", domainName="", topLevelDomain="", portNumber="", path="", queryStringSeparator="", queryString="", fragment=""):
        self.scheme = scheme
        self.subdomain = subdomain
        self.domainName = domainName
        self.topLevelDomain = topLevelDomain
        self.portNumber = portNumber
        self.path = path
        self.queryStringSeparator = queryStringSeparator
        self.queryString = queryString
        self.fragment = fragment

class Url:
    def __init__(self):
        self.valid: bool = False
        self.proto: str = ""
        self.domain: str = ""
        self.port: str = ""
        self.path: List[str] = []
        self.query: str = ""
        self.fragment: str = ""
        self.miniurl: str = ""

def parse_url(long_url: str) -> LongUrl:
    parsed = urllib.parse.urlparse(long_url)
    domain_parts = parsed.netloc.split(".")

    subdomain = ""
    domainName = ""
    topLevelDomain = ""

    if len(domain_parts) > 2:
        subdomain = domain_parts[0]
        domainName = domain_parts[1]
        topLevelDomain = domain_parts[-1]
    elif len(domain_parts) == 2:
        domainName = domain_parts[0]
        topLevelDomain = domain_parts[1]

    # Get port number (if any)
    portNumber = parsed.port if parsed.port else ""

    # Get path, query string, and fragment
    path = parsed.path
    queryStringSeparator = "?" if parsed.query else ""
    queryString = parsed.query
    fragment = parsed.fragment

    return LongUrl(scheme=parsed.scheme, 
                   subdomain=subdomain, 
                   domainName=domainName, 
                   topLevelDomain=topLevelDomain, 
                   portNumber=portNumber, 
                   path=path, 
                   queryStringSeparator=queryStringSeparator, 
                   queryString=queryString, 
                   fragment=fragment)

def minify(long_url: str) -> LongUrl:
    return parse_url(long_url)

# Saving a CSV File
def save_to_csv(url_list, filename="urls.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["Scheme", "Subdomain", "Domain", "Top Level Domain", "Port", "Path", "Query Separator", "Query String", "Fragment"])
        
        # Write each parsed URL's components
        for url in url_list:
            writer.writerow([
                url.scheme, url.subdomain, url.domainName, url.topLevelDomain, 
                url.portNumber, url.path, url.queryStringSeparator, url.queryString, url.fragment
            ])

urls = [
    "https://www.youtube.com/watch?v=a51CXCRuZd0",
    "http://example.com:8080/path/to/page?query=1#section",
    "https://sub.domain.co.uk/path"
]

parsed_urls = [parse_url(url) for url in urls]

save_to_csv(parsed_urls)
print("URLs saved to CSV successfully!")


#do it a different way, set up different functions that scan to see what thing matches given a long url
#ex scan the long_url input and see what matches 'https://' and tht function is scheme
#function for subdomain will take in whatever comes after https:// and ends with a .
#domain takes in whatever comes after top level domain and ends with dot
                







#long_url = input("Please enter your URL: ")