from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):

    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)

    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):

        products_by_model = {}

        for product in self.products:

            if product.model not in products_by_model:
                products_by_model[product.model] = {"count": 0, "total_price": 0.0}

            products_by_model[product.model]["count"] += 1
            products_by_model[product.model]["total_price"] += product.price

        sorted_models = sorted(products_by_model.keys())

        model_info = [
            f"{model}: {products_by_model[model]['count']}pcs, average price: {products_by_model[model]['total_price'] / products_by_model[model]['count']:.2f}"
            for model in sorted_models
        ]

        return (
                f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{self.get_estimated_profit()}\n"
                f"**Furniture for sale:\n" +
                "\n".join(model_info))
