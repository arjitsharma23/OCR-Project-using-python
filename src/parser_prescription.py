from parser_genric import MedicalDocParser
import re

class PresprciptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self,text)
    
    def parse(self):
        return{
            'paitent_name': self.get_field('paitent_name'),
            'address': self.get_field('address'),
            'medicines': self.get_field('medicines'),
            'directions': self.get_field('directions'),
            'refill':self.get_field('refill')
        }

    def get_field(self,field_name):
        pattern_dict ={
            'paitent_name':{'pattern':'Name:(.*)Date', 'flags' : 0},
            'address':{'pattern':'Address:(.*)\n', 'flags' : 0},
            'medicines':{'pattern':'Address[^\n]*(.*)Directions', 'flags' : re.DOTALL},
            'directions':{'pattern':'Directions:(.*)Refill', 'flags' : re.DOTALL},
            'refill':{'pattern':'Refill:(.*)times', 'flags' : 0},
        }

        pattern_object =pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'],self.text,flags = pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()
               
    
if __name__ =='__main__':

    text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    pp = PresprciptionParser(text)
    print(pp.parse())

