#John Liu
#6/4/24
#Collectible Charm class


from charm import Charm

class CollectibleCharm(Charm):
    
    def __init__(self, name, description, retailPrice, condition, serialNumber):
        '''
        Purpose: Initialize Collectible charm attributes and inherit from Charm
        Parameters: name, description, retailPrice, condition, serialNumber
        Return: none
        Sample Call: charm = CollectibleCharm("Capital C", "A translucent resin cube...", 0.25, Charm.Condition.VERY_GOOD, "C")
        '''
        super().__init__(name, description, retailPrice, condition)
        self.__serialnumber = serialNumber
    
    def getSerialNumber(self):
        '''
        Purpose: get the serial number 
        Parameters: self
        Return: self.__serialNumber
        Sample call: charm.getSerialNumber()
        '''
        return self.__serialnumber
    
    def getMarketValue(self):
        '''
        Purpose: get the market value of its condition and round to two decimal places 
        Parameters: self
        Return: round(marketValue, 2)
        Sample call: charm.getMarketValue()
        '''
        marketValue = float(self.getRetailPrice() * (self.getCondition().value / 100.0))
        return round(marketValue, 2)
    
    def __str__(self):
        '''
        Purpose: print the name with the serial number in brackets
        Parameters: self
        Return: f"{self.getName()} [{self.getSerialNumber()}]"
        Sample call: print(charm)
        '''
        return f"{self.getName()} [{self.getSerialNumber()}]"
    
    def __lt__(self, other):
        '''
        Purpose: compare two objects with <
        Parameters: self, other
        Return: self.getMarketValue() < other.getMarketValue()
        Sample call: print(charm1 < charm2)
        '''
        return self.getMarketValue() < other.getMarketValue()
    
    def __le__(self, other):
        '''
        Purpose: compare two objects with <=
        Parameters: self, other
        Return: self.getMarketValue() <= other.getMarketValue()
        Sample call: print(charm1 <= charm2)
        '''
        return self.getMarketValue() <= other.getMarketValue()
    
    def __gt__(self, other):
        '''
        Purpose: compare two objects with >
        Parameters: self, other
        Return: self.getMarketValue() > other.getMarketValue()
        Sample call: print(charm1 > charm2)
        '''
        return self.getMarketValue() > other.getMarketValue()

    def __ge__(self, other):
        '''
        Purpose: compare two objects with >=
        Parameters: self, other
        Return: self.getMarketValue() >= other.getMarketValue()
        Sample call: print(charm1 >= charm2)
        '''
        return self.getMarketValue() >= other.getMarketValue()
    
    def __eq__(self, other):
        '''
        Purpose: compare two objects with ==, all attributes have to match, otherwise return True
        Parameters: self, other
        Return: True or False
        Sample call: print(charm1 == charm2)
        '''
        if self.getName() != other.getName():
            return False
        if self.getDescription() != other.getDescription():
            return False
        if self.getRetailPrice() != other.getRetailPrice():
            return False
        if self.__serialnumber != other.getSerialNumber():
            return False
        if self.getCondition() != other.getCondition():
            return False
        return True    
    def __ne__(self, other):
        '''
        Purpose: compare two objects with !=, all attributes cannot match, otherwise return False
        Parameters: self, other
        Return: True or False 
        Sample call: print(charm1 != charm2)
        '''
        if self.getName() != other.getName():
            return True
        if self.getDescription() != other.getDescription():
            return True
        if self.getRetailPrice() != other.getRetailPrice():
            return True
        if self.__serialnumber != other.getSerialNumber():
            return True
        if self.getCondition() != other.getCondition():
            return True 
        return False
