from operator import itemgetter

#Класс "Производитель"
class Manufacturer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#Класс "Деталь"
class Detail:
    def __init__(self, id, name, cost, man_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.man_id = man_id

#Класс "Детали производителя"
class DetMan:
    def __init__(self, man_id, det_id):
        self.man_id = man_id
        self.det_id = det_id

#Производители
manufacturers = [
    Manufacturer(1, 'Производитель №1'),
    Manufacturer(2, 'Производитель №2'),
    Manufacturer(3, 'Иванов'),
    Manufacturer(4, 'Петров'),
    Manufacturer(5, 'Сидоров')
]

#Детали
details = [
    Detail(1, 'Гайка', 19.99, 1),
    Detail(2, 'Шуруп', 49.99, 2),
    Detail(3, 'Гвоздь', 9.99, 3),
    Detail(4, 'Винт', 39.99, 1),
    Detail(5, 'Штуцер', 99.99, 3),
    Detail(6, 'Болт', 59.99, 3)
]

#Детали производителей
detmans = [
    DetMan(1, 1),
    DetMan(1, 2),
    DetMan(2, 3),
    DetMan(3, 3),
    DetMan(3, 5),
    DetMan(4, 1),
    DetMan(5, 3),
    DetMan(5, 4),
    DetMan(5, 6)
]

#Основная функция
def main():
    #один-ко-многим
    one_to_many = [(d.name, d.cost, m.name)
                   for m in manufacturers
                   for d in details
                   if d.man_id == m.id]

    #многие-ко-многим
    many_to_many_temp = [(m.name, dm.man_id, dm.det_id)
                         for m in manufacturers
                         for dm in detmans
                         if m.id == dm.man_id]
    many_to_many = [(d.name, d.cost, man_name)
                    for man_name, man_id, det_id in many_to_many_temp
                    for d in details
                    if d.id == det_id]

    #E1
    print('Задание Е1:')
    res_11 = {}
    for m in manufacturers:
        if 'производитель' in m.name.lower():
            m_d = [item[0]
                   for item in one_to_many
                   if item[2] == m.name]
            res_11[m.name] = m_d
    print(res_11)

    #E2
    print('\nЗадание E2:')
    res_12 = []
    for m in manufacturers:
        m_d = list(filter(lambda i: i[2] == m.name, one_to_many))
        if len(m_d) > 0:
            m_cost = [cost
                      for _,cost,_ in m_d]
            m_cost_avg = sum(m_cost) / len(m_d)
            res_12.append((m.name, round(m_cost_avg, 2)))
    print(sorted(res_12, key = itemgetter(1)))

    #E3
    print('\nЗадание Е3:')
    res_13 = {}
    for d in details:
        if d.name.lower()[0] == 'г':
            d_m = [item[2]
                   for item in many_to_many
                   if d.name == item[0]]
            res_13[d.name] = d_m
    print(res_13)
    print()

if __name__ == '__main__':
    main()
