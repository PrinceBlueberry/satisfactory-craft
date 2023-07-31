
import json
import collections


def get_ingredients_for(want_name, want_rate):
    """
    :param want_name: the item you want to make a factory for.
    :param want_rate: desired output rate in items per minute.
    :return: the total raw in materials per minute.
    """
    raw_materials = collections.Counter()

    materials = recipes[want_name]['materials']
    for mat, mat_rate in materials.items():
        want_mat_rate = mat_rate * want_rate / recipes[want_name]['output']
        if mat in basic_materials:
            raw_materials[mat] += want_mat_rate
        else:
            raw_materials += get_ingredients_for(mat, want_mat_rate)
    return raw_materials


def get_buildings_for(want_name, want_rate):
    """
    :param want_name: the item you want to make a factory for.
    :param want_rate: desired output rate in items per minute.
    :return: the buildings that need to be built.
    """

    building_and_recipe = f"{recipes[want_name]['building']}: {want_name}"
    buildings_required = want_rate / recipes[want_name]['output']
    buildings = collections.Counter({building_and_recipe: buildings_required})

    materials = recipes[want_name]['materials']
    for mat, mat_rate in materials.items():
        if mat not in basic_materials:
            want_mat_rate = mat_rate * want_rate / recipes[want_name]['output']
            buildings += get_buildings_for(mat, want_mat_rate)
    return buildings


file_recipes = 'recipes.json'

basic_materials = ['Iron Ore', 'Copper Ore']
basic_materials = ['Iron Ore', 'Copper Ore', 'Limestone', 'Coal']
basic_machines = ['Miner']

if __name__ == "__main__":
    with open(file_recipes) as fin:
        recipes = json.load(fin)

    want = 'Heavy Modular Frame'
    rate = 2
    # for making 8 rotors per minute, expect result of 90 materials (Iron Ore) per minute
    # for making 8 rotors per minute, expect result of ......?

    print(f'In order to make "{want}" at a rate of {rate} per minute, you need: ')
    print('Materials (items per minute): ')
    print(get_ingredients_for(want, rate))
    print('Buildings: ')
    print(get_buildings_for(want, rate))
