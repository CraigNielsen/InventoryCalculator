'''
Created on 25 Jan 2016

@author: craig
'''


class AddBehavior(object):

    '''
    -"default" behavior for adding Products
    -total cost is incremented but retail price is updated
    -this allows for feedback on current unit retail cost (Latest) for an item
    '''

# default add behavior
    def addItem(self, prodct, count, cost, retail, accumulateCost=True):
        # accumulate costs is only for creating individual lists,
        # when combining lists, no accumulation should be used
        # (because cost is already accumulated )

        prodct.count += count
        if accumulateCost:
            prodct.totalCost += cost * count
        else:
            prodct.totalCost += cost
        prodct.retail = retail  # retail is not weighted only updated

        return prodct
