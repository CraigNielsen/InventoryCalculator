
import pytest

from ordersList import OrdersList
from salesProductList import SalesProductList
from storeInventory import StoreInventory


class TestOrders:
    #--Orders--

    #_________________________________________________________________________
    #_____________some assertions_____________________________________________

    def test_assertions(self):
        inv = StoreInventory()
        sales = SalesProductList()
        orders = OrdersList()
        with pytest.raises(AssertionError):
            assert inv.addOrders(sales)
        with pytest.raises(AssertionError):
            assert inv.addSales(orders)

#_________________________________________________________________________
#_________________________________________________________________________

    # total orders for SKU item
        '''total cost of orders for SKU'''

    def test_totalOrdersBySKU(self):

        ordered = OrdersList()
        ordered.addProductsCSV(
            "./csvs/stock-purchases_2016-01-16_to_2016-01-22.csv")

        assert ordered['1621'].totalCost == 260
        assert ordered['1621'].count == 4
        # note this is current retail price (at latest order)
        assert ordered['1621'].retail == 399

#_________________________________________________________________________
#_________________________________________________________________________

    # total cost of orders overall
        '''total cost of orders overall'''

    def test_totalOrdersCost(self):

        ordered = OrdersList()
        ordered.addProductsCSV(
            "./csvs/stock-purchases_2016-01-16_to_2016-01-22.csv")

        assert ordered.costAll() == 131987.28

#_________________________________________________________________________
#_________________________________________________________________________
