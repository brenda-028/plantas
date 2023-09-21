from data_floricultura import data 

def get_popular():
    result = []
    for element in data:  
        result.append(element["name"]["popular"])
    return result
    

def show_popular():
    array = get_popular()
    for element in array:
        print(f"Nome popular: {element[0]}")


def get_family():
    result = []
    for element in data:
        result.append(element["family"])
    return result

def show_family():
    array = get_family()
    for element in array:
        print(element)

def show_popular_family():
    array_1 = get_popular()
    array_2 = get_family()
    count = 0

    while count < len(array_1):
        print(f"A planta {array_1[count][0]} pertence à família {array_2[count]}")
        count += 1





