'''
Created on 24 Jan 2016

@author: Craig
'''
from addBehavior import AddBehavior


class Product(object):

    '''
    Object representing the basic product
    '''

    def __init__(self):
        self.count = 0
        self.totalCost = 0
        self.retail = 0
        self.addStyle = AddBehavior()

    # setting the behavior for addition, mostly used for quick product
    # creation in testing
    def setAddStyle(self, _addBehavior):
        self.addStyle = _addBehavior
