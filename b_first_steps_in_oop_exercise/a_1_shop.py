class Shop:
    def __init__(self,name:str,items:list):
        self.name = name
        self.items = items

    def get_items_count(self) -> str:
        return len(self.items)

# Test_code
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])

print(shop.get_items_count())