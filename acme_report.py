import random

from acme import Product
def generate_products(num_products=30):
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    product_list = []
    for _ in range(num_products):
        name = ' '.join([random.choice(adjectives), random.choice(nouns)])
        price = random.randrange(5, 101)
        weight = random.randrange(5, 101)
        flammability = random.randrange(0, 3)
        product = Product(name, price, weight, flammability)
        product_list.append(product)
    return product_list

# products = generate_products(30)
# for product in products:
#     print(f"Name: {product.name}, Price: {product.price}, Weight: {product.weight}, Flammability: {product.flammability}, Identifier: {product.identifier}")


def inventory_report(products):
    num_unique_products = len(set(products))
    total_price = sum(product.price for product in products)
    total_weight = sum(product.weight for product in products)
    total_flammability = sum(product.flammability for product in products)
    average_price = total_price / len(products)
    average_weight = total_weight / len(products)
    average_flammability = total_flammability / len(products)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product count: {num_unique_products}")
    print(f"Average price: {average_price}")
    print(f"Average weight: {average_weight}")
    print(f"Average flammability: {average_flammability}")

    return (num_unique_products, average_price, average_weight, average_flammability)

# if __name__ == '__main__':
#     print(inventory_report(generate_products()))