import csv


class Product(object):

    def __init__(self, _count=0, _totalCost=0, _retail=0):
        self.count = _count
        self.sales = 0
        self.totalCost = _totalCost
        self.retail = _retail

    def w_unit_cost(self):
        return self.totalCost / self.count


class Product_List(dict):

    def add_products_csv(self, path, Id_column_name, count_column_name, cost_column_name, price_column_name):
        with open(path, 'r') as input:
            csvRead = csv.reader(input, delimiter=',')
            headers = csvRead.next()
            pId = headers.index(Id_column_name)
            pCount = headers.index(count_column_name)
            pCost = headers.index(cost_column_name)
            pPrice = headers.index(price_column_name)

            for row in csvRead:
                productId = (row[pId])
                productCount = int(float(row[pCount]))
                productCost = float(row[pCost])
                productPrice = float(row[pPrice])
                if (productId in self):
                    self[productId].count += productCount
                    self[productId].totalCost += (productCost * productCount)
                    self[productId].retail += productPrice
                else:
                    self[productId] = Product(
                        productCount, productCost*productCount, productPrice)

    def add_list(self, transaction_list):
        for key, product in transaction_list.iteritems():
            if (product.count > 0):  # is a purchase list
                self[key].count += product.count
                self[key].totalCost += product.totalCost
            else:  # is a sales item
                self[key].sales += product.count

    def totalCost(self):
        total = 0
        for key, product in self.iteritems():
            total += product.totalCost
        return total
