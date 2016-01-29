'''
Created on 24 Jan 2016

@author: craig
'''

import csv
from product import Product


class IFixList(dict):

    '''
    The interface for iFix calculator subclasses:
    SalesList,OrdersList,StoreInventory
    SKU items in the list represent total over a given period
    '''

    def addProductsCSV(self, path):
        '''Adds products to an IFixList: SalesList, OrdersList or InventoryList.
        Reads input from a .csv file
        '''
        # read csv
        with open(path, 'rb') as input:
            csvRead = csv.reader(input, delimiter=',')
            headers = csvRead.next()
            # gets column header names from the child object attributes
            # this allows different naming conventions for different List types
            pId = headers.index(self.idName)
            pCount = headers.index(self.idQ)
            pCost = headers.index(self.idCost)
            pPrice = headers.index(self.idPrice)

            for row in csvRead:
                try:
                    productId = (row[pId])
                    productCount = int(float(row[pCount]))
                    productCost = float(row[pCost])
                    productPrice = float(row[pPrice])
                except ValueError:
                    print ("Please ensure no letters are present \
                      in the numeric data")

                if (productId in self):
                    # addStyle" is behavior added to individual Child classes
                    # this allows SalesList to add products differently
                    # to OrdersLists without needing to define
                    # the behavior in each class. This allows for easier
                    # extensibility (behavior changes in one place)
                    self[productId] = self.addStyle.addItem(
                        self[productId], productCount,
                        productCost, productPrice)
                else:
                    newProduct = Product()
                    newProduct = self.addStyle.addItem(
                        newProduct, productCount, productCost, productPrice)
                    self[productId] = newProduct

    def costAll(self, retail=False):
        ''' Determines the total cost of all items in a list:
         (unless retail is set to true)
        for sales List, this determines the total cost of items sold.
        for orders List, this determines the total cost of orders bought,
        for inventory List, this determines the total cost of current stock
        note: this value is rounded to 2 decimal places'''

        total = 0
        for id, prodct in self.iteritems():
            if not retail:
                total += (prodct.totalCost)
            else:
                total += (prodct.retail)
        return round(total, 2)

    def combineList(self, _iFixList, forceCombine=False):
        '''Combines iFixLists. If forceCombine is True,
         items will be created as well as added to exiting stock.
        This is to ensure items cannot be sold unless they are in stock. '''

        for ID, prodct in _iFixList.iteritems():
            if (ID not in self):
                if forceCombine:
                    self[ID] = self.addStyle.addItem(
                        self[ID], prodct.count, prodct.totalCost,
                        prodct.retail, False)
                else:
                    '''This exception prevents sales without stock
                    (as a redundant check)'''
                    raise Exception
            else:
                self[ID] = self.addStyle.addItem(
                    self[ID], prodct.count, prodct.totalCost,
                    prodct.retail, False)
        return True
