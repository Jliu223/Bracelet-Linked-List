#John Liu, jl4582
#6/4/24
#Bracelet class that inherits from LinkedList


from linked_list import LinkedList
from charm import Charm 

class Bracelet(LinkedList):
    
    def __init__(self, marketValue):
        '''
        Purpose: initialize Bracelet with an additional attribute, marketValue, inherit from LinkedList
        Parameters: self, marketValue
        Return: none
        Sample call: bracelet = Bracelet(90)
        '''
        super().__init__()
        self.__marketValue = marketValue
    
    def append(self, data):
        '''
        Purpose: append to the linked list
        Parameters: self, data
        Return: none
        Sample call: bracelet.append(20)
        '''
        if isinstance(data, Charm): #check if data is instance of Charm
            if self.isClosed(): #if closed, open, append, then close
                self.open()  
                super().append(data)
                self.close()
            else: #open case 
                super().append(data)
    
    def appraise(self):
        '''
        Purpose: appraise the marketValue for each Charm in the linked list
        Parameters: self
        Return: round(totalValue, 2), totalValue is the total market values of all of the charms
        Sample call: bracelet.appraise()
        '''
        totalValue = self.__marketValue
        currentNode = super().getHead()
        if self.isClosed(): #closed case 
            while currentNode.getNext() != super().getHead():
                totalValue += currentNode.getData().getMarketValue()
                currentNode = currentNode.getNext()
            
        else: #open case
            while currentNode is not None:
                totalValue += currentNode.getData().getMarketValue()
                currentNode = currentNode.getNext()
        
        return round(totalValue, 2)
    
    def close(self):
        '''
        Purpose: close the linked list, by setting the last node's next to the head
        Parameters: self
        Return: none
        Sample call: bracelet.close()
        '''
        if super().isEmpty():
            return
        currentNode = super().getHead()
        while currentNode.getNext() is not None and currentNode.getNext() != super().getHead():
            currentNode = currentNode.getNext()
        currentNode.setNext(super().getHead()) #set the next to the head to indicate a closed bracelet 
        
    def open(self):
        '''
        Purpose: close the linked list, by setting the last node's next to None
        Parameters: self
        Return: none
        Sample call: bracelet.open()
        '''
        if super().isEmpty():
            return
        currentNode = super().getHead()
        while currentNode.getNext() is not None:
            currentNode = currentNode.getNext()
            if currentNode.getNext() == super().getHead():
                currentNode.setNext(None) #set next to None instead of the head to open the bracelet 
                return
            
           
            
    def isClosed(self):
        '''
        Purpose: checks if the linked list is closed
        Parameters: self
        Return: True or False 
        Sample call: if self.isClosed():
        '''
        if super().isEmpty():
            return False
        currentNode = super().getHead()
        while currentNode.getNext() is not None:
            currentNode = currentNode.getNext()
            if currentNode.getNext() == super().getHead(): #when next equals the head, indicates a closed Bracelet, return True
                return True
            if currentNode.getNext() == None: #indicates an open bracelet, return False 
                return False
           
        
    def isOpen(self):
        '''
        Purpose: checks if the linked list is open
        Parameters: self
        Return: True or False 
        Sample call: if self.isOpen():
        '''
        if super().isEmpty():
            return True
        currentNode = super().getHead()
        while currentNode.getNext() is not None:
            currentNode = currentNode.getNext()
            if currentNode.getNext() == super().getHead(): #opposite of isOpen()
                return False
            if currentNode.getNext() == None:
                return True
            
        

    def remove(self, item):
        '''
        Purpose: removes the item and if it is closed, it opens the bracelet, removes the item, then closes again
        Parameters: self, item
        Return: removedItem
        Sample call: bracelet.remove(20)
        '''
        if self.isClosed(): #if the bracelet is closed, open it, remove the item, then close the bracelet 
            self.open()
        
        removedItem = super().remove(item)
        self.close()
        
        return removedItem
        
        
    def search(self, item):
        currentNode = super().getHead()
        found = False
        if self.isClosed():
            while currentNode != item and not found and currentNode.getData() != super().getHead(): 
                if currentNode.getData() == item:
                    found = True
                else:
                    currentNode = currentNode.getNext()

        else:
            while currentNode is not None and not found:
                if currentNode.getData() == item:
                    found = True
                else:
                    currentNode = currentNode.getNext()
        return found 
        #keep searching until the item's next is None or the head 
    def __getitem__(self):
        pass
    
    def __str__(self):
        pass
    
    def __len__(self):
        if super().getHead() == None:  # if list is empty return 0
            return 0
        
        current = super().getHead()   #list is not empty and has at least 1 Node
        counter = 1
        
        while current.getNext() != None: # check if theres's another item after the current node
            counter += 1
            current = current.getNext()
        return counter
    
    
