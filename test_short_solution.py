from iFIxShortSolution import Product_List


class TestSales:
    
        
    def test_short_solution(self):
        
        inv=Product_List()
        inv.add_products_csv("./csvs/trendTest/ifix-stock_trendTest.csv", "ProductId", "InventoryCount", "Cost", "Price")
        
        sales=Product_List()
        sales.add_products_csv("./csvs/trendTest/stock-sales_trendTest.csv", "ProductId", "Quantity", "UnitCost", "UnitPrice")
        
        orders=Product_List()
        orders.add_products_csv("./csvs/trendTest/stock-purchases_trendTest.csv", "ProductId", "Quantity", "UnitCost", "UnitPrice")
           
        
        assert inv["6691"].count == 10 
        assert orders["6691"].count == 3
        assert sales["6691"].count == -4
        
        assert inv["6691"].w_unit_cost() == 85.9
        
        inv.add_list(sales) 
#        On-hand quantities of stock on the system at the end of the period.
        assert inv['6691'].count == 10
        assert inv['6691'].sales == -4
        
        assert inv["6691"].w_unit_cost() == 85.9
        
        inv.add_list(orders)     
        assert inv['6691'].count == 13
        assert inv['6691'].sales == -4
        
        #Total Cost of Goods Sold by SKU
        assert inv['6691'].totalCost == 1164.9
       
        # Total Cost of Goods Sold for the given period
        assert inv.totalCost()==1164.9
        
        #weighted unit cost for SKU at a point in time
        assert round(inv["6691"].w_unit_cost(),2) == 89.61
    
        