#John Liu, jl4582
#6/4/24
#My custom charm class called MyCharm


from charm import Charm

class MyCharm(Charm):
    
    def __init__(self, name, description, retailPrice, condition, material):
        '''
        Purpose: Initialize Collectible charm attributes and inherit from Charm
        Parameters: name, description, retailPrice, condition, material
        Return: none
        Sample Call: charm = CollectibleCharm("Capital C", "A translucent resin cube...", 0.25, Charm.Condition.VERY_GOOD, "Plastic")
        '''
        super().__init__(name, description, retailPrice, condition)
        self.__material= material
    
    def getMaterial(self):
        '''
        Purpose: get the material
        Parameters: self
        Return: self.__material
        Sample call: charm.getMaterial()
        '''
        return self.__material
    
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
        Purpose: print the name with its description and material
        Parameters: self
        Return: f"{self.getName()} is {self.getDescription()}, made out of {self.getMaterial()}"
        Sample call: print(charm)
        '''
        return f"{self.getName()} is {self.getDescription()}, made out of {self.getMaterial()}"
    
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
        Purpose: compare two objects with ==, all attributes have to match, otherwise return False
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
        if self.__material != other.getMaterial():
            return False
        if self.getCondition() != other.getCondition():
            return False
        return True    
    def __ne__(self, other):
        if self.getName() != other.getName():
            return True
        if self.getDescription() != other.getDescription():
            return True
        if self.getRetailPrice() != other.getRetailPrice():
            return True
        if self.__material != other.getMaterial():
            return True
        if self.getCondition() != other.getCondition():
            return True 
        return False

if __name__ == "__main__":
    firstCharm = MyCharm("I ♥ U", "a charm for your significant other", 75.00, Charm.Condition.EXCELLENT, "Plastic")
    secondCharm = MyCharm("Barry", "a charm for Barry", 30.00, Charm.Condition.ACCEPTABLE, "Wood")
    print(firstCharm == secondCharm)
    print(firstCharm != secondCharm)
    print(firstCharm > secondCharm)
    print(firstCharm < secondCharm)
    print(firstCharm >= secondCharm)
    print(firstCharm <= secondCharm)
    print(firstCharm.getMarketValue())
    print(secondCharm.getMarketValue())
    print(firstCharm.getMaterial())
    print(secondCharm.getMaterial())
    print(firstCharm)
    print(secondCharm)