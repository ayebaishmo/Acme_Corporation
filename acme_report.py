"""
This module goes ahead and create 
random products
"""
import random

# pylint: disable=E0401
from acme import Product

def generate_products(num_products=30):
    """
    This function create 30 products 
    randomly"""
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

def inventory_report(products):
    """
    This function performs certain 
    calculations on the products"""
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
