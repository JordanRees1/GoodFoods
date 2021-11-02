import re

list = '1 tbsp sesame oil', '1 red onion', '1 garlic clove', 'thumb-sized piece ginger', '1 red chilli', '1½ tsp ground turmeric', '1½ tsp ground cumin', '2 sweet potatoes (about 400g/14oz)', '250g red split lentils', '600ml vegetable stock', '80g bag of spinach', '4 spring onions', '½ small pack of Thai basil'



ingredient_dict = {}
for item in list:
    amount = re.search("([\d]+)", item)
    if not item in ingredient_dict:
        if amount:
            ingredient_dict[item] = amount.group(0)
        else:
            ingredient_dict[item] = 1
    else:
        if amount:
            ingredient_dict[item] += amount.group(0)
        else:
            ingredient_dict[item] += 1
