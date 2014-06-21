

# Server mode:
#           href, [referer] -> referer/subject, predicate, object
# Format html mode:
#           change a elements into rdfa via template & other metadata



from urlparse import urlsplit, parse_qs, urlunsplit
from urllib import urlencode
from urlparse import urlparse
from urlparse import parse_qs
import types, json
import re, os

class Triplink(object):
    def __init__(self, url, content="", referer=".", rendering_template_path=None):
        url_obj = urlparse(url)
        self.__rendering_template_path = rendering_template_path
        self.__referer = referer
        self.__params = parse_qs(url_obj.query)
        self.__url  = url
        if not self.isValid:
            self = None
            return
        self.__urlParts = url_obj
        self.__subject = self.getParam("tl_s", self.__referer)
        self.__predicate = self.getParam("tl_p", None)
        obj = self.getParam("tl_o", None)
        
        #If there's no object then assume that the main URI is the object and the triplink
        #is decribing it
        if obj is None:
            params = self.__params.copy()
            if params.has_key("tl_p"):
                params.pop("tl_p")
            if params.has_key("tl_s"):
                params.pop("tl_s")
            params.pop("triplink")
            query = urlencode(params)
            obj = urlunsplit((self.__urlParts.scheme, self.__urlParts.netloc, 
                    self.__urlParts.path, query, self.__urlParts.fragment))
        self.__object =  obj

        self.__content = content
        self.__text = re.sub("<.*?>","", content)
       
        self.__loadTemplate()
        
    def __loadTemplate(self):
        if self.__rendering_template_path <> None:
            f = open(self.__rendering_template_path, "rb")
            self.triplink_template = json.loads(f.read())
            f.close()
        else:
            self.triplink_template = { "default":  {
                                        "statement": "Subject: $subject Predicate: $predicate Object: $object)",
                                        "urltitle": "Predicate: $predicate Object: $object)",
                                        "RDFaTemplate": "<span rel='$predicate' resource='$object'>$text</span>"
                                        }
                                    }        
 
    @property
    def content(self):
        return self.__content

    @property
    def text(self):
        return self.__text

    @property
    def subject(self):
        return self.__subject
    
    @property
    def predicate(self):
        return self.__predicate
    
    @property
    def object(self):
        return self.__object
        
    @property
    def url(self):
        return self.__url
    
    @property
    def isValid(self):
        return self.getParam("triplink", "").startswith("http://purl.org/triplink/v/0.1")
    
    def getParam(self, name, default=None):
        p = self.__params.get(name, [])
        if(len(p)>0):
            return p[0]
        return default

    def render(self, category):  
        """ Renders a human or machine readable version of a triplink for use in tooltips, HTML etc """
        if self.isValid:
            tempData = self.triplink_template.get(self.predicate, \
                        self.triplink_template.get("default", {}))
            return self.__substitute(tempData[category])
            
        else:
            return None
        
    def __substitute(self,format_string):
        return format_string.replace("$predicate", self.predicate). \
                    replace("$object", self.object). \
                    replace("$content", self.content). \
                    replace("$text", self.text). \
                    replace("$subject", self.subject). \
                    replace("$url", self.url)


