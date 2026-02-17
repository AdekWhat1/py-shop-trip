class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product_name, quantity in product_cart.items():
            price_per_item = self.products[product_name]
            total_cost += price_per_item * quantity
        return total_cost

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0

        for product, amount in product_cart.items():
            price_per_item = self.products[product]
            item_total = price_per_item * amount
            total_cost += item_total

            print(f"{amount} {product}s for {item_total:g} dollars")

        print(f"Total cost is {total_cost:g} dollars")
        print("See you again!")
        print()
