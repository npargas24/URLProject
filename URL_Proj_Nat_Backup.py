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
from typing import List, Tuple

class LongUrl:
    def __init__(self, scheme="", subdomain="", domainName=[], topLevelDomain="", portNumber=int, path=[], queryStringSeparator="", queryString=[], fragment=""):
        self.scheme = scheme
        self.subdomain = subdomain
        self.domainName = domainName
        self.topLevelDomain = topLevelDomain
        self.portNumber = portNumber
        self.path = path
        self.queryStringSeparator = queryStringSeparator
        self.queryString = queryString
        self.fragment = fragment 
        #put parse method in here

    
    def schemeFunc(self, long_url):
        url_parts = long_url.split("://")
        self.scheme = url_parts[0]
        print("Scheme: ", self.scheme)

    
    def portDomain(self, long_url):
        url_parts = long_url.split("://")
        url_rem = url_parts[1]
        if ':' in url_rem:
        #in case there's a port number
            slice = url_rem.split(':')

            if len(slice) != 2:
                print("invalid URL")
                return long_url

            domains = slice[0]
            section = 0

            for domain in domains.split('.'):
                #split on each subdomain
                print("Subdomain [" , section, "]: ", domain)
                self.domainName.append(domain)
                section+=1

            slice = url_rem[1].split('/')

            if len(slice) >= 2:
                #number before / in url should be port number
                self.portNumber = slice[0]
                print("port: " + self.portNumber)
            else:
                #if there's no slash but there was still a : aside from :// then it's invalid
                print("invalid URL")
                return long_url

    
    def domainFunc(self,long_url):
        url_parts = long_url.split("://")
        url_rem = url_parts[1]
        section = 0

        if "/" in url_rem:
            url_slice = url_rem.split("/")
            domains = url_slice[0]
            print("The full domain is: ", domains)
            for domain in domains.split("."):
                print("domain[" + str(section) + "]: " + domain)
                self.domainName.append(domain)
                section += 1

    def pathFunc(self,long_url):
        url_parts = long_url.split("://")
        url_rem = url_parts[1]
        
        url_slice = url_rem.split("/", 1)

        if len(url_slice) > 1:
            full_path = url_slice[1]

            if '?' in full_path:
                full_path = full_path.split('?', 1)[0]
            if '#' in full_path:
                full_path = full_path.split('#', 1)[0]
            
            for path_part in full_path.split('/'):
                self.path.append(path_part)
                print('Path part: ', path_part)
        
        else:
            print('No path')
            return long_url


    
    def queryFunc(self, long_url):
        url_parts = long_url.split("://")
        url_rem = url_parts[1]
        
        if '?' in url_rem:
            query_split = url_rem.split('?')

            if '#' in query_split[1]:
                query_split_split = query_split[1].split('#')
                self.queryString.append(query_split_split[0])
                print("A query part: ", self.queryString)
            else:
               self.queryString.append(query_split[1])
               print('a query part: ', self.queryString)


    def fragmentFunc(self, long_url):
        url_parts = long_url.split("://")
        url_rem = url_parts[1]
        if '#' in url_rem:
            
            url_slice = url_rem.split('#')

            if len(url_slice) != 2:
                print("invalid URL")
                return long_url
                
            self.fragment = url_slice[1]
            print("Fragment: ", self.fragment)



    def parse(self,long_url):
        self.schemeFunc(long_url)
        self.portDomain(long_url)
        self.domainFunc(long_url)
        self.pathFunc(long_url)
        self.queryFunc(long_url)
        self.fragmentFunc(long_url)


            


example = LongUrl()
example.parse("https://elementor.com/blog/website-url/?query=123#example-url")

example2 = LongUrl()
example2.parse("https://github.com/npargas24/URLProject/blob/Nat_Branch/URL_Proj_Nat.py")

example3 = LongUrl()
example3.parse("https://stackoverflow.com/questions/70307348/how-do-you-update-a-git-repository-from-visual-studio")





'''  def longParse(self, long_url):

        self.queryStringSeparator = "?"
    
        url_parts = long_url.split("://")
        self.scheme = url_parts[0]
        print("Scheme: ", self.scheme)
        url_rem = url_parts[1]

        if len(url_parts) != 2:
            print("invalid URL")
            return long_url


        if ':' in url_rem:
        #in case there's a port number
            slice = url_rem.split(':')

            if len(slice) != 2:
                print("invalid URL")
                return long_url

            domains = slice[0]
            section = 0

            for domain in domains.split('.'):
                #split on each subdomain
                print("Subdomain [" , section, "]: ", domain)
                self.domainName.append(domain)
                section+=1

            slice = url_rem[1].split('/')

            if len(slice) >= 2:
                #number before / in url should be port number
                self.portNumber = slice[0]
                print("port: " + self.portNumber)
            else:
                #if there's no slash but there was still a : aside from :// then it's invalid
                print("invalid URL")
                return long_url
        
        
        elif "/" in url_rem:
        #no port number
            slice = url_rem.split("/")
            domains = slice[0]
            section = 0
            for domain in domains.split("."):
                print("Subdomain [" , section, "]: ", domain)
                self.domainName.append(domain)
                section+=1
            
        
        if '?' in url_rem:
            #split things at the search query
            url_slice = url_rem.split('?')
            
            if len(url_slice) != 2:
                print("invalid URL")
                return long_url
            
            #break apart query operartors
            slice = url_slice[0].split('/')
            section = 0

            for path_part in slice:
                if section == 0:
                    pass
                if section >= 1:
                    self.path.append(path_part)
                    print("Query String [" , (section - 1), "]: ", self.path[section -1])
                section+=1
        
            if '#' in url_rem:

                url_slice = url_rem.split('#')

                if len(url_slice) != 2:
                    print("invalid URL")
                    return long_url
                
                self.fragment = url_slice[1]
                print("Fragment: ", self.fragment)

                # splitting again on '?' because it was a local variable
                #or maybe not
                slice = url_slice[0].split('?')
                queries = slice[1]

                section = 0
                
                #split apart query on delimiters
                for query_part in queries.split('&'):
                    query_smaller = query_part.split('=')
                    
                    if len(query_smaller) != 2:
                        print("skipping weird query")
                        continue
                        
                    #add separated query parts
                    query_rejoined = (query_smaller[0], query_smaller[1])
                    self.queryString.append(query_rejoined)
                    print("Query String [" + str(section) + "]: " + query_smaller[0] + "=" + query_smaller[1])
                    section+=1
            
            else:
                queries = url_slice[1]
                section = 0
                #split apart query on delimiters
                for query_part in queries.split('&'):
                    query_smaller = query_part.split('=')
                    #add separated query parts
                    self.queryString.append(query_smaller[0], query_smaller[1])
                    print("Query String [" + section + "]: " + query_smaller[0] + "=" + query_smaller[1])
                    section+=1
        
        
        elif '#' in url_rem:
    
            url_slice = url_rem.split('#')

            if len(url_slice) != 2:
                print("invalid URL")
                return long_url 
            #only need this because if there's a fragment it goes at the end
            self.fragment = url_slice[1]
            print("Fragment: ", self.fragment)'''
        
