import translator1

import translator1


import unittest
def englishtoFre(text):
     return  translator1.english_to_french("hello")


def frenctoEng(text):
     return translator1.french_to_english("bonjour")


class MyModuleTest(unittest.TestCase):
     def test_english_to_FR(self):
          self.assertEqual(englishtoFre("hello"),"Bonjour")

     def test_notequal_english_to_FR(self):  
          self.assertNotEqual(englishtoFre("hello"),"HOLA")

     def test_french_to_EN(self):
          self.assertEqual(frenctoEng("Bonjour"),"Hello")

     def test_notequal_french_to_EN(self):
          self.assertNotEqual(englishtoFre("Bonjour"),"not hello")

          
     




if __name__=="__main__":
     unittest.main()

# print(translator1.frenchtoEnglish("bonjour"))
