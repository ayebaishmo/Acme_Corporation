import pytest
from acme import Product
from acme_report import generate_products

def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10

def test_default_product_attributes():
    '''Test default product attributes.'''
    prod = Product('Test Product')
    assert prod.weight == 20
    assert prod.flammability == 0.5

def test_product_methods():
    '''Test stealability() and explode() methods.'''
    prod = Product('Test Product', price=5, weight=15, flammability=2.0)
    assert prod.stealability() == "Not so stealable..."
    assert prod.explode() == "...boom!"

def test_generate_products():
    '''Test generate_products() function returns a list with 30 items.'''
    products = generate_products()
    assert len(products) == 30
