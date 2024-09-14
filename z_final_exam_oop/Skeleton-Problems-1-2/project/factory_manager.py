from project.stores.toy_store import ToyStore
from project.stores.furniture_store import FurnitureStore
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    VALID_PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCT_TYPES:
            raise Exception("Invalid product type!")
        product = self.VALID_PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")
        store = self.VALID_STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        products_to_be_sold = [p for p in products if p.sub_type == store.store_type()[:-5]]
        if products_to_be_sold:
            for product in products_to_be_sold:
                self.products.remove(product)
                store.products.append(product)
                store.capacity -= 1

            total_price = sum(p.price for p in products_to_be_sold)
            self.income += total_price
            return f"Store {store.name} successfully purchased {len(products_to_be_sold)} items."
        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discounted_count = 0
        for product in self.products:
            if product.model == product_model:
                original_price = product.price
                product.discount()
                if product.price != original_price:
                    discounted_count += 1

        return f"Discount applied to {discounted_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        factory_products_count = len([p for p in self.products])
        products_sum_price = sum([p.price for p in self.products])
        product_breakdown = {}
        for product in self.products:
            if product.model not in product_breakdown:
                product_breakdown[product.model] = 0
            product_breakdown[product.model] += 1

        sorted_models = sorted(product_breakdown.keys())
        products_info = "\n".join([f"{model}: {product_breakdown[model]}" for model in sorted_models])
        sorted_stores = sorted([store.name for store in self.stores])
        stores_info = "\n".join(sorted_stores)

        return (f"Factory: {self.name}\n"
                f"Income: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {factory_products_count}. Total net price: {products_sum_price:.2f}\n"
                f"{products_info}\n"
                f"***Partner Stores: {len(self.stores)}***\n"
                f"{stores_info}")
