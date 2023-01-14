
import json


def get_ingredients_for(want_name, want_rate):
    """
    :param want_name: the item you want to make a factory for.
    :param want_rate: desired output rate in items per minute.
    :return: the total raw in materials per minute.
    """

    result = 0
    materials = recipes[want_name]['materials']

    for mat, mat_rate in materials.items():
        want_mat_rate = mat_rate * want_rate / recipes[want_name]['output']
        if mat in basic_materials:
            result += want_mat_rate
        else:
            result += get_ingredients_for(mat, want_mat_rate)
    return result


file_recipes = 'recipes.json'

basic_materials = ['Iron Ore']

if __name__ == "__main__":
    # do stuff
    with open(file_recipes) as fin:
        recipes = json.load(fin)

    # for making 8 rotors per minute, expect result of 90 materials (Iron Ore) per minute
    print(get_ingredients_for('Rotor', 8))
