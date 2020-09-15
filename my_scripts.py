from itertools import count, cycle


def int_numbers(start, stop, step):
    """
    Итератор, генерирующий целые числа, начиная с указанного
    :param start: 7
    :param stop: 15
    :param step: 2
    :return: 7, 9, 11, 13, 15
    """
    result = []
    for el in count(start, step):
        if el > stop:
            break
        else:
            result.append(el)
    return result


def round_list(you_list, max_count):
    """
    Итератор, повторяющий элементы некоторого списка, определенного заранее
    :param you_list: ['bus', 'plane', 'car']
    :param max_count: 3
    :return: 'bus', 'plane', 'car', 'bus', 'plane', 'car', 'bus', 'plane', 'car'
    """
    result = []
    i = 1
    for el in cycle(you_list):
        if i > max_count:
            break
        else:
            result.append(el)
            i += 1
    return result


if __name__ == '__main__':
    print(int_numbers(15, 255, 6))
    print(round_list(['монитор', 'телевизор', 'телефон'], 8))
