import URL_Proj_Nat as Url
import unittest

class UrlTest(unittest.TestCase):
    def test(self):
        url_obj = Url.UrlHandler("https://www.google.com/search?q=how+to+impo&oq=how+to+impo&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABixAxiABDIHCAIQABiABDIKCAMQABixAxiABDIKCAQQABixAxiABDIHCAUQABiABDIKCAYQABixAxiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTcwODgwajBqN6gCCLACAfEFHincNqIHq3w&sourceid=chrome&ie=UTF-8")
        assert url_obj.valid == True


url_test = UrlTest()
url_test.test()
