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
        #put parse method in here

    def longComp(self, long_url):

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

        
        if self.queryStringSeparator in url_rem:
            #split things at the search query
            url_slice = url_rem.split('?')
            
            if len(url_slice) != 2:
                print("invalid URL")
                return long_url
            
            #break apart query operartors
            slice = url_slice.split('/')
            section = 0

            for query in slice:
                if section != 0:
                    print("Query String [" , section, "]: ", query)
                    self.queryString.append(query)
                else:
                    section+=1
                section+=1
        
        if '#' in url_rem:

            url_slice = url_rem.split('#')

            if len(url_slice) != 2:
                print("invalid URL")
                return long_url
            
            self.fragment = url_slice[1]
            print("Fragment: ", self.fragment)

            







            
        


'''from typing import List, Tuple
import hashlib
import sqlite3
import json
import pickle

my_webapp = "https://myapp.com/"
db_name = "mini.db"
conn = None
cursor = None

insert_query = "INSERT INTO minitable (id, data) VALUES (?, ?)"
select_query = "SELECT * FROM minitable WHERE id = ?"
#try : around the insert
#except: Exception as E
class Url():
    valid : bool = False
    long_url : str = ""
    proto : str = ""
    domains : List[str] = []
    port : str = ""
    path : List[str] = []
    query : List[Tuple[str, str]] = []
    fragment : str = ""
    hash : str = ""
    miniurl = ""

def parse_url(long_url : str) -> Url:

    url = Url()
    cnt : int = 0

    url.long_url = long_url
    url_parts = long_url.split("://")
    
    if len(url_parts) != 2:
        print("parsing failed")
        return url
    
    url.proto = url_parts[0]
    print("proto: " + url.proto)
    url_rem = url_parts[1]

    if ":" in url_rem:
        url_splits = url_rem.split(":")
        
        if len(url_splits) != 2:
            print("parsing failed")
            return url
        
        
        domains = url_splits[0]
        cnt = 0
        
        for domain in domains.split("."):
            print("domain[" + str(cnt) + "]: " + domain)
            url.domains.append(domain)
            cnt += 1
        splits = url_splits[1].split("/")
        
        if len(splits) >= 2:
            url.port = splits[0]
            print("port: " + url.port)
        else:
            print("parsing failed")
            return url
    
    elif "/" in url_rem:
        url_splits = url_rem.split("/")
        domains = url_splits[0]
        cnt = 0
        for domain in domains.split("."):
            print("domain[" + str(cnt) + "]: " + domain)
            url.domains.append(domain)
            cnt += 1

    if "?" in url_rem:
        url_splits = url_rem.split("?")
        if len(url_splits) != 2:
            print("parsing failed")
            return url
        splits = url_splits[0].split("/")
        cnt = 0
        for split in splits:
            if cnt == 0:
                pass
            if cnt >= 1:
                url.path.append(split)
                print("path[" + str((cnt - 1)) + "]: " + url.path[cnt - 1])
            cnt += 1
        
        if "#" in url_rem:
            url_splits = url_rem.split("#")
            
            if len(url_splits) != 2:
                print("parsing failed")
                return url
            url.fragment = url_splits[1]
            print("fragment: " + url.fragment)
            splits = url_splits[0].split("?")
            
            if len(splits) != 2:
                print("parsing failed")
                return url
            query = splits[1]
            cnt = 0
            
            for query_part in query.split("&"):
                qparts = query_part.split("=")
                if len(qparts) != 2:
                    print("parsing failed")
                    return url
                url.query.append((qparts[0], qparts[1]))
                print("query[" + str(cnt) + "]: " + qparts[0] + "=" + qparts[1])
                cnt += 1
        
        else:
            query = url_splits[1]
            cnt = 0
            for query_part in query.split("&"):
                qparts = query_part.split("=")
                if len(qparts) != 2:
                    print("parsing failed")
                    return url
                url.query.append((qparts[0], qparts[1]))
                print("query[" + str(cnt) + "]: " + qparts[0] + "=" + qparts[1])
                cnt += 1

    elif "#" in url_rem:
        url_splits = url_rem.split("#")
        if len(url_splits) != 2:
            print("parsing failed")
            return url
        url.fragment = url_splits[1]

    url.valid = True

    return url

def minify(long_url : str) -> Url:
    
    url = parse_url(long_url)
    if url.valid:
        hashstr = hashlib.md5(long_url.encode("utf-8"), usedforsecurity=False).hexdigest()
        hash = hashstr[:12]
        url.hash = hash
        url.miniurl = my_webapp + hash
        print("miniurl: " + url.miniurl)

    return url

def open_db():
    global conn
    global cursor

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
'''     CREATE TABLE IF NOT EXISTS minitable (
            id INTEGER PRIMARY KEY,
            data BLOB
        )
    )

def close_db():
    global conn
    global cursor

    conn.commit()
    conn.close()

def insert_db(url : Url):
    global conn
    global cursor

    pkl_dat = pickle.dumps(url)
    data = (int(url.hash, 16), pkl_dat)
    cursor.execute(insert_query, data)

def select_db(hash : str) -> Url:
    global conn
    global cursor

    cursor.execute(select_query, (int(hash, 16),))
    result = cursor.fetchone()
    if result:
        url : Url = pickle.loads(result[1])
        return url
    return None

open_db()

url = minify("https://www.youtube.com/watch?v=a51CXCRuZd0")
insert_db(url)
ret_url : Url = select_db(url.hash)
print("returned miniurl from db: " + url.miniurl)

url = minify("https://www.youtube.com/watch?v=a51CXCRuZd0#dude")
insert_db(url)
ret_url : Url = select_db(url.hash)
print("returned miniurl from db: " + url.miniurl)

url = minify("https://www.google.com/search?q=python+list+of+tuples+typing&sca_esv=62854facdc4565ec&ei=x021Z-6sIOrZ5NoP69GPQQ&ved=0ahUKEwiurMfQ486LAxXqLFkFHevoIwgQ4dUDCBE&uact=5&oq=python+list+of+tuples+typing&gs_lp=Egxnd3Mtd2l6LXNlcnAiHHB5dGhvbiBsaXN0IG9mIHR1cGxlcyB0eXBpbmcyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigVIz25Qy2JY2W1wAngBkAEAmAFqoAGFA6oBAzYuMbgBA8gBAPgBAZgCCaAClwPCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICBRAAGIAEwgIIEAAYgAQYogTCAgUQABjvBZgDAIgGAZAGCpIHAzguMaAH2iU&sclient=gws-wiz-serp#2111")
insert_db(url)
ret_url : Url = select_db(url.hash)
print("returned miniurl from db: " + url.miniurl)

url = minify("https://www.google.com:8080/search?q=python+list+of+tuples+typing&sca_esv=62854facdc4565ec&ei=x021Z-6sIOrZ5NoP69GPQQ&ved=0ahUKEwiurMfQ486LAxXqLFkFHevoIwgQ4dUDCBE&uact=5&oq=python+list+of+tuples+typing&gs_lp=Egxnd3Mtd2l6LXNlcnAiHHB5dGhvbiBsaXN0IG9mIHR1cGxlcyB0eXBpbmcyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigVIz25Qy2JY2W1wAngBkAEAmAFqoAGFA6oBAzYuMbgBA8gBAPgBAZgCCaAClwPCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICBRAAGIAEwgIIEAAYgAQYogTCAgUQABjvBZgDAIgGAZAGCpIHAzguMaAH2iU&sclient=gws-wiz-serp#2111")
insert_db(url)
ret_url : Url = select_db(url.hash)
print("returned miniurl from db: " + url.miniurl)

close_db()
'''


#take in mini URL if we have it 
#if not, return none
#wrap mini url func around select'''









#long_url = input("Please enter your URL: ")