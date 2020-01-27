"""
This script produces the 'ACME OFFICIAL INVENTORY REPORT'

"""
from random import randint, sample, uniform
from acme import Product

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_prod=30):
    """ Randomly generates product names """
    products = []
    for num in range(num_prod):
        product = sample(adjectives,1)[0] + " " + sample(nouns,1)[0]
        products.append(product)
    return products

def inventory_report(products):
    """
    Randomly generates inventory list of acme.Product() class obecjts nd then
    prints inventory report

    """
    inventory = []
    for product in products:
        price = randint(5,100)
        weight = randint(5,100)
        flammability  = uniform(0.0,2.5)
        prod = Product(product,
                       price=price,
                       weight=weight,
                       flammability=flammability
                        )
        inventory.append(prod)
    prices = []
    weights = []
    flam_rates = []
    for item in inventory:
        prices.append(item.price)
        weights.append(item.weight)
        flam_rates.append(item.flammability)
    
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(set(products)))
    print('Average price: ', sum(prices)/len(prices))
    print('Average weight: ', sum(weights)/len(weights))
    print('Average flammability: ', sum(flam_rates)/len(flam_rates))

if __name__ == '__main__':
    inventory_report(generate_products())