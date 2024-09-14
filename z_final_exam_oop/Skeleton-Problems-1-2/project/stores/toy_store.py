from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    INITUAL_CAPACITY = 100

    def __init__(self,name: str, location: str):
        super().__init__(name,location,self.INITUAL_CAPACITY)

    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        products_in_stock = {}
        for p in self.products:
            if p.model not in products_in_stock.keys():
                products_in_stock[p.model] = {'pcs': 1, 'allprice': p.price}
            else:
                products_in_stock[p.model]['pcs'] += 1
                products_in_stock[p.model]['allprice'] += p.price

        sorted_products = sorted(products_in_stock.keys(), key=lambda x: x.lower())

        result = (f"Store: {self.name}, location: {self.location}, available capacity: {self.INITUAL_CAPACITY}\n"
                  f"Estimated future profit for {len(self.products)} products is {self.get_estimated_profit()}\n"
                  f"**Toys for sale:\n")

        for product, info in sorted_products.items():
            pcs = info[0]
            avg_price = info[1]/pcs
            result += f"{product}: {pcs}pcs, average price: {avg_price:.2f}\n"

        return result