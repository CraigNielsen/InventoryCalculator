'''
Created on 24 Jan 2016

@author: craig
'''
from iFixList import IFixList
from addBehavior import AddBehavior


class OrdersList(IFixList, AddBehavior):

    '''
    classdocs
    '''

    def __init__(self):

        self.idName = "ProductId"
        self.idQ = "Quantity"
        self.idCost = "UnitCost"
        self.idPrice = "UnitPrice"
        self.addStyle = AddBehavior()
