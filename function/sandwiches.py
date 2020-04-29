def sandwiches(*ingredients):
    print('Então você quer em seu sanduíche:')

    for ingredient in ingredients:
        print(ingredient.title())

sandwiches('queijo', 'alface', 'tomate')
sandwiches('queijo', 'alface', 'tomate', 'palmito', 'azeitona')
sandwiches('queijo', 'alface', 'palmito', 'azeitona', 'maionese')