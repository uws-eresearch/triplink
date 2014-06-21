from triplink import Triplink
import unittest



class TestReadme(unittest.TestCase):
    def test_simpleTriplink(self):
        """Simple URI with all the parts in place"""
        tl = Triplink("http://ontologize.me/?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_o=http://live.dbpedia.org/page/Siluosaurus&tl_s=.")
        self.assertEqual(tl.subject, ".")
        self.assertEqual(tl.predicate, "http://purl.org/dc/terms/creator")
        self.assertEqual(tl.object, "http://live.dbpedia.org/page/Siluosaurus")

    def test_noObject(self):
        """No object present - lets make the silosaurus a creator"""
        tl = Triplink("http://live.dbpedia.org/page/Siluosaurus?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_s=.")
        self.assertEqual(tl.subject, ".")
        self.assertEqual(tl.predicate, "http://purl.org/dc/terms/creator")
        self.assertEqual(tl.object, "http://live.dbpedia.org/page/Siluosaurus")
        
    def test_defaultRendering(self):
        """Check how a simple statement looks"""
        tl = Triplink("http://live.dbpedia.org/page/Siluosaurus?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_s=.")
        self.assertEqual(tl.render("statement"), "Subject: . Predicate: http://purl.org/dc/terms/creator Object: http://live.dbpedia.org/page/Siluosaurus)")
        
    def test_dcCreatorRendering(self):
        """Check how a simple statement about authorship looks"""
        tl = Triplink("http://live.dbpedia.org/page/Siluosaurus?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/triplink/v/0.1&tl_s=.",rendering_template_path="./triplink_template.json")
        self.assertEqual(tl.render("statement"), "The person or agent http://live.dbpedia.org/page/Siluosaurus is a creator of this resource: ")   

    def test_nonTriplinkBadURI(self):
        """Make sure we don't get false positives """
        tl = Triplink("http://ontologize.me/?tl_p=http://purl.org/dc/terms/creator&triplink=http://purl.org/tripylink/v/0.1&tl_o=http://live.dbpedia.org/page/Siluosaurus&tl_s=.")
        self.assertEqual(tl.isValid, False, "Should not be valid")
        #self.assertEqual(tl, None, "Not a triplink, the URI for triplink param is wrong")

    def test_nonTriplink(self):
        """Deal with flaky URIs """
        tl = Triplink("asdasasda")
        self.assertEqual(tl.isValid, False, "Should not be valid")
 
   
     
   
	
if __name__ == '__main__':
    unittest.main()
