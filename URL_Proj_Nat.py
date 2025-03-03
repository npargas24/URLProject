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

class UrlHandler:

    scheme = ""
    subdomain = ""
    domainName = []
    topLevelDomain = ""
    portNumber = 0
    path = []
    queryStringSeparator = ""
    queryString = []
    fragment = ""
    hash = ""
    littleurl = ""
    valid = False

    def __init__(self, long_url):
        self.parse(long_url)
        self.shorten(long_url)

    
    def schemeFunc(self, long_url):
        url_parts = long_url.split("://")
        
        if len(url_parts) < 2:
            return False
        
        self.scheme = url_parts[0]
        print("Scheme: ", self.scheme)
        return True

    
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
                return False
        return True

    
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
                full_path = full_path.split('?')[0]
            if '#' in full_path:
                full_path = full_path.split('#')[0]
            
            for path_part in full_path.split('/'):
                if len(path_part) > 0:
                    self.path.append(path_part)
                    print('Path part: ', path_part)
        
        else:
            print('No path')
            return long_url
        
        return True


    
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
                return False
                
            self.fragment = url_slice[1]
            print("Fragment: ", self.fragment)



    def parse(self,long_url):
        if self.schemeFunc(long_url) == False : 
            self.valid = False
            return
        if self.portDomain(long_url) == False:
            self.valid = False
            return
        if self.domainFunc(long_url) == False:
            self.valid = False
            return
        if self.pathFunc(long_url) == False:
            self.valid = False
            return
        if self.queryFunc(long_url) == False:
            self.valid = False
            return
        if self.fragmentFunc(long_url) == False:
            self.valid = False
            return
        self.valid = True





    def shorten(self,long_url: str):

        if self.valid:
            hashstr = hashlib.md5(long_url.encode("utf-8"), usedforsecurity=False).hexdigest()
            hashedrl = hashstr[:12]
            
            self.hash = hashedrl
            self.littleurl = my_webapp + self.hash
            print("shortened url: " + self.littleurl)


class Database() : 
    db_name = "/Users/nataliepargas/URLProject/little.db"
    conn = None
    cursor = None
    
    def __init__(self):
        
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS minitable (
                id INTEGER PRIMARY KEY,
                data BLOB
            )
        ''')


    
    def insert_db(self, long_url):

        pkl_dat = pickle.dumps(long_url)
        data = (int(long_url.hash, 16), pkl_dat)
        self.cursor.execute(insert_query, data)

    
    def select_db(self, short_url):
        
        hash = short_url.split('://')[1].split('/')[1]
        
        self.cursor.execute(select_query, (int(hash, 16),))
        result = self.cursor.fetchone()
        if result:
            url : UrlHandler = pickle.loads(result[1])
            return url
        return None
    
    def __exit__(self):

        conn.commit()
        conn.close()

   


url_obj = UrlHandler("https://elementor.com/blog/website-url/?query=123#example-url")
#url_obj.parse("https://elementor.com/blog/website-url/?query=123#example-url")
#url_obj.shorten("https://elementor.com/blog/website-url/?query=123#example-url")

db = Database()
db.insert_db(url_obj)
url_obj2 = None
url_obj2 = db.select_db(url_obj.littleurl)
print('url read out of database: ' , url_obj2.littleurl)
print('url read out of database: ' , url_obj2.domainName)
print('url read out of database: ' , url_obj2.path)

'''url_obj2 = UrlHandler()
url_obj2.parse("https://github.com/npargas24/URLProject/blob/Nat_Branch/URL_Proj_Nat.py")

url_obj3 = UrlHandler()
url_obj3.parse("https://stackoverflow.com/questions/70307348/how-do-you-update-a-git-repository-from-visual-studio")
'''


