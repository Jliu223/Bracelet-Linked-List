#John Liu
#6/4/24
#Friendship Charm class 


from charm import Charm

class FriendshipCharm(Charm):
    
    def __init__(self, name, description, retailPrice, condition, symbol):
        '''
        Purpose: Initialize Friendship charm attributes and inherit from Charm
        Parameters: name, description, retailPrice, condition, symbol
        Return: none
        Sample Call: charm = FriendshipCharm("Capital C", "A translucent resin cube...", 0.25, Charm.Condition.VERY_GOOD, "C")
        '''
        super().__init__(name, description, retailPrice, condition)
        self.__symbol = symbol
        
    def getMarketValue(self):
        '''
        Purpose: get the market value of its condition
        Parameters: self
        Return: self.getCondition().value / 100.0
        Sample call: charm.getMarketValue()
        '''
        return self.getCondition().value / 100.0
    
    def getSymbol(self):
        '''
        Purpose: return the symbol
        Parameters: self
        Return: self.__symbol
        Sample call: charm.getSymbol()
        '''
        return self.__symbol
    
    def __str__(self):
        '''
        Purpose: returns the symbol
        Parameters: self
        Return: self.__symbol
        Sample call: print(charm)
        '''
        return self.__symbol

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
        Purpose: compare two objects with ==
        Parameters: self, other
        Return: self.getMarketValue() == other.getMarketValue()
        Sample call: print(charm1 == charm2)
        '''
        return self.getMarketValue() == other.getMarketValue()
    
    def __ne__(self, other):
        '''
        Purpose: compare two objects with !=
        Parameters: self, other
        Return: self.getMarketValue() != other.getMarketValue()
        Sample call: print(charm1 != charm2)
        '''
        return self.getMarketValue() != other.getMarketValue()
        