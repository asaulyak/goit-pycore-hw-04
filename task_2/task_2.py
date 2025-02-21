def get_cats_info(path):
    cats = []

    try:
        with open(path) as file:
            while True:
                line = file.readline()

                if not line:
                    break

                cat = parse_cat_info(line)

                if cat:
                    cats.append(cat)
    except Exception as e:
        print(e)

    return cats

def parse_cat_info(cat_info):
    try:
        cat_id, name, age = cat_info.strip().split(',')

        if not cat_id or not name or not age:
            print("Invalid cat info on line ", cat_info)

            return None

        return {'id': cat_id, 'name': name, 'age': int(age)}
    except Exception as e:
        print(e)
        return None
