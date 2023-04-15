"""Print out all the melons in our inventory."""


from melons import melons 


def print_melon():
    """Print each melon with corresponding attribute information."""

    for melon in melons:
        print(f"""
            melon: {melon}
            price: {melons[melon][0]}
            seedless: {melons[melon][1]}
            flesh_color: {melons.get('flesh_color', None)}
            rind_color: {melons.get('grind_color', None)}
            average_weight: {melons.get('average_weight', None)}""")

