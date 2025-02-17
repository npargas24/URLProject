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

import csv

long_url = input("Please enter your URL")