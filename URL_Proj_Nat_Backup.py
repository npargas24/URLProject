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
import hashlib
import sqlite3
import json
import pickle
from typing import List, Tuple

my_webapp = "https://myapp.com/"
db_name = "/Users/nataliepargas/URLProject/little.db"
conn = None
cursor = None

insert_query = "INSERT INTO minitable (id, data) VALUES (?, ?)"
select_query = "SELECT * FROM minitable WHERE id = ?"

class LongUrl:
    def __init__(self, scheme="", subdomain="", domainName=[], topLevelDomain="", portNumber=int, path=[], queryStringSeparator="", queryString=[], fragment="", hashedrl = ""):
        self.scheme = scheme
        self.subdomain = subdomain
        self.domainName = domainName
        self.topLevelDomain = topLevelDomain
        self.portNumber = portNumber
        self.path = path
        self.queryStringSeparator = queryStringSeparator
        self.queryString = queryString
        self.fragment = fragment 
        self.hash = None
        self.littleurl = None
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


    class ParsedURL:
        def __init__(self, valid: bool):
            self.valid = valid


    def parse(self,long_url):
        self.schemeFunc(long_url)
        self.portDomain(long_url)
        self.domainFunc(long_url)
        self.pathFunc(long_url)
        self.queryFunc(long_url)
        self.fragmentFunc(long_url)

        return self.ParsedURL(valid=True)

    
    def shorten(self,long_url: str):
        parsedrl = self.parse(long_url)
        if parsedrl.valid:
            hashstr = hashlib.sha256(long_url.encode("utf-8"), usedforsecurity=False).hexdigest()
            hashedrl = hashstr[:12]
            
            url_obj = LongUrl(long_url)
            url_obj.hash = hashedrl
            url_obj.littleurl = my_webapp + url_obj.hash
            print("shortened url: " + url_obj.littleurl)

            return url_obj
            

        return None
         
    
    def db_operations(self,long_url):
        self.open_db()
        self.select_db(long_url)
        self.insert_db(long_url)
        self.close_db()

    


    def open_db(self):
        global conn
        global cursor
        
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS minitable (
                id INTEGER PRIMARY KEY,
                data BLOB
            )
        ''')

    def close_db(self):
        global conn
        global cursor

        conn.commit()
        conn.close()

        
        
    def insert_db(self, long_url):
        global conn
        global cursor

        pkl_dat = pickle.dumps(long_url)
        data = (int(long_url.hash, 16), pkl_dat)
        cursor.execute(insert_query, data)

    
    def select_db(self, long_url):
        global conn
        global cursor


        cursor.execute(select_query, (int(long_url.hash, 16),))
        result = cursor.fetchone()
        if result:
            url : LongUrl = pickle.loads(result[1])
            return url
        return None
    




        

        
        
        '''insert_contents = (
            (
            
                       "INSERT INTO urls (scheme,domain,port,path,query,fragment)"
                       "VALUES(?,?,?,?,?,?)"
        )
        )

        cursor.execute(insert_contents, long_url)'''


example = LongUrl()
#example.parse("https://elementor.com/blog/website-url/?query=123#example-url")
example.shorten("https://elementor.com/blog/website-url/?query=123#example-url")
#example.db_operations("https://elementor.com/blog/website-url/?query=123#example-url")


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
        
