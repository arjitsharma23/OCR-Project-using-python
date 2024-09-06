import abc #abstract class method



class MedicalDocParser(metaclass = abc.ABCMeta):
    def __init__(self,text):
        self.text = text
    

    @abc.abstractmethod #method enforcer
    def parse(self):
        pass

