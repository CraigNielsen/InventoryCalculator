
from salesProductList import SalesProductList
from product import Product
from salesAddBehaviour import behavior_accumulate_retail


class TestSales:

    #--Sales--

    #_________________________________________________________________________
    #_________________________________________________________________________

    '''total cost of sales for SKU'''

    def test_totalSalesBySKU(self):

        sold = SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_TEST.csv")

        eA = Product()
        eA.setAddStyle(behavior_accumulate_retail())
        eA = eA.addStyle.addItem(eA, -6, 5, 10)  # calculated manually

        assert sold['602'].totalCost == eA.totalCost
        assert sold['602'].count == eA.count
        assert sold['602'].retail == eA.retail

        assert sold['602'].totalCost == -30
        assert sold['602'].count == -6
        assert sold['602'].retail == -60

    def test_totalSalesBySKU2(self):

        sold = SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_2016-01-16_to_2016-01-22.csv")

        assert sold['602'].totalCost == 0
        assert sold['602'].count == -12

        assert sold['6477'].totalCost == -1140
        assert sold['602'].count == -12
#_________________________________________________________________________
#_________________________________________________________________________

    '''total cost of all goods sold ie(All SKUs)'''

    def test_allGoodsSold(self):

        sold = SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_TEST.csv")
        # note cost to the company is negative ie: a profit was made
        assert sold.costAll() == -55  # calculated manually

    def test_allGoodsSold2(self):

        sold = SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_2016-01-16_to_2016-01-22.csv")
        # note cost to the company is negative ie: a profit was made
        assert sold.costAll() == -128717.46  # calculated manually

#_________________________________________________________________________
#_________________________________________________________________________

    ''''total retail for SKU sales'''

    def test_totalRetailForAllBySKU(self):
        # note the nature of a salesAddBehavior totals retail of SKU by default
        sold = SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_TEST.csv")

        assert sold['602'].retail == -60  # calculated manually

    def test_totalRetailForAllBySKU2(self):
        # note the nature of a salesAddBehavior totals retail of SKU by default
        sold = SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_2016-01-16_to_2016-01-22.csv")

        assert sold['602'].retail == 0  # calculated manually
        assert sold['6477'].retail == -3588  # calculated manually
