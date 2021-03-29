from lxml import etree

# print(etree)

with open("food.xml", "r") as f:
    tree = etree.parse(f)
# The price of all foods (as a list)
    price = tree.xpath('/breakfast_menu/food/price/text()')
    print(price)

# The sum of all the calories

    calories = tree.xpath('/breakfast_menu/food/calories/text()')

    total = 0
    for x in calories:
        x = int(x)
        total = total + x
    print(str(total) + " calories")

# The description of the food with the id: 3

    description = tree.xpath('/breakfast_menu/food/description/text()')
    print(description[2])

# The price of "French Toast"

    french_toast = tree.xpath('/breakfast_menu/food/price/text()')
    print(french_toast[3])

# The concatenated descriptions of all the "savoury" foods

    savoury_food = tree.xpath("//food[@type='savoury']/description/text()")
    print(savoury_food)

    for string in savoury_food:
        string = str(string)
        print(string)

# The count of ingredients of the food with id: 2

    count = tree.xpath("//food[@id='2']/ingredients/ingredient/type/text()")
    print(count)

    x = len(count)
    print(x)

# The second ingredient of "Homestyle Breakfast"

    find_text = tree.xpath('food[name="Homestyle Breakfast"]/ingredients/ingredient[2]/type')
    print(find_text[0].text)

# The count of foods that has "milk" in the ingredients

    find_milk = tree.xpath('food/ingredients/ingredient[type="milk"]')
    print(len(find_milk))

# The count of ingredients of all "sweet" foods

    find_sweetFood = tree.xpath('food[@type="sweet"]/ingredients/ingredient')
    print(len(find_sweetFood))








