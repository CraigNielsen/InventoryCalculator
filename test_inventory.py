
import pytest

from ordersList import OrdersList
from salesProductList import SalesProductList
from storeInventory import StoreInventory
from salesAddBehaviour import behavior_accumulate_retail


class TestInventory:

    #_________________________________________________________________________
    #_________________________________________________________________________

        #--Stock--
        # total quantity of SKU item in stock

    def test_stockException(self):
        # can define custom exception at a later stage if desired
        inv = StoreInventory()
        inv.addProductsCSV("./csvs/emptyStock.csv")
        sales = SalesProductList()
        sales.addProductsCSV("./csvs/stock-sales_TEST.csv")
        with pytest.raises(Exception):
            inv.addSales(sales)
#_________________________________________________________________________
#_________________________________________________________________________

    def test_stockTotalCostandRetail(self):
        inv = StoreInventory()
        # to calculate the accumulative  retail available, set addBehavior to
        # salesAddBehaviour (this behavior may be renamed to
        # accumulativeRetailBehaviour)
        inv.setAddStyle(behavior_accumulate_retail())
        inv.addProductsCSV("./csvs/ifix-stock_2016-01-22.csv")
        assert inv.costAll() == 588989.66
        assert inv.costAll(retail=True) == 3244457

#_________________________________________________________________________
#_________________________________________________________________________

    def test_weightedUnitPrice(self):

        inv = StoreInventory()
        # to calculate the accumulative  retail available, set addBehavior to
        # salesAddBehaviour (this behavior may be renamed to
        # accumulativeRetailBehaviour)
        inv.setAddStyle(behavior_accumulate_retail())
        inv.addProductsCSV("./csvs/trendTest/ifix-stock_trendTest.csv")

        orders = OrdersList()
        orders.addProductsCSV("./csvs/trendTest/stock-purchases_trendTest.csv")

        sales = SalesProductList()
        sales.addProductsCSV("./csvs/trendTest/stock-sales_trendTest.csv")

        inv.addOrders(orders)
        wUnitCost = inv.getWeightedUnitCost("6691")

        # rounding is required at the last moment so errors do not accumulate

        assert round(wUnitCost, 2) == 89.61
        assert round(sales['6691'].count * wUnitCost, 2) == -358.43
        inv.addSales(sales)
        assert round(inv["6691"].count * wUnitCost, 2) == 806.47
