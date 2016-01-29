'''
Created on 25 Jan 2016

@author: craig
'''
from addBehavior import AddBehavior


class behavior_accumulate_retail(AddBehavior):

    '''(also thought of as accumulative retail behavior)
    -Interface for specific add behavior
    -The retail amount is incremented to a total for all sales
    -Objects implementing this do not require feedback on retail price per item
    -This behavior can be applied to any number of IFixList children
    '''

    def addItem(self, prodct, count, cost, retail, accumulateCost=True):
        #   accumulate costs is only for creating individual lists,
        #   when combining lists, no accumulation should be used
        #   (because cost is already accumulated )

        prodct.count += count
        if accumulateCost:
            prodct.totalCost += cost * count
        else:
            prodct.totalCost += cost
        prodct.retail += (retail*count)

        return prodct
