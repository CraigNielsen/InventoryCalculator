'''
Created on 24 Jan 2016

@author: craig
'''

from iFixList import IFixList
from ordersList import OrdersList
from salesProductList import SalesProductList
from addBehavior import AddBehavior


class StoreInventory(IFixList, AddBehavior):

    '''
    -This class represents an IFixStore Inventory
    -Orders can be passed to the Inventory
    -Sales can be passed to the inventory
    '''

    def __init__(self):

        self.idName = "ProductId"
        self.idQ = "InventoryCount"
        self.idCost = "Cost"
        self.idPrice = "Price"
        self.addStyle = AddBehavior()

    def addOrders(self, _ordersList):
        assert type(_ordersList) == OrdersList  # assert type
        self.combineList(_ordersList, True)  # add order items
        return True

    def addSales(self, _salesProductList):
        assert type(_salesProductList) == SalesProductList  # assert type
        self.combineList(_salesProductList)  # add sales items
        return True

    # to accommodate accumulative retail price
    def setAddStyle(self, _addBehavior):
        self.addStyle = _addBehavior

    def getWeightedUnitCost(self, SKU):
        return self[SKU].totalCost/self[SKU].count
