def read_input_file(path: str) -> list[str]:
    """ Read input text file with data """
    with open(path) as file_parce:
        return [data for data in file_parce.read().splitlines() if data]


def parse_file_data() -> dict[str, dict[str, str]]:
    parse_product_items = read_input_file(DATA)
    result = {}
    counter = 0
    for item in parse_product_items:
        counter += 1
        (name, category, section, description, brand,
         item_number, price, rating, age, male, is_sale, discount) = item.split('; ')
        result[f'product №{counter}'] = {
            'name': name,
            'category': category,
            'section': section,
            'description': description,
            'brand': brand,
            'item_number': item_number,
            'price': price,
            'rating': rating,
            'age': age,
            'male': male,
            'is_sale': is_sale,
            'discount': discount
        }
    return result
