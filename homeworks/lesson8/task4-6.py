"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class StockItem:

    def __init__(self, item_id: int, name: str, size: int):
        self.__id = item_id
        self.__name = name
        self.__size = size

    @property
    def id(self) -> int:
        return self.__id

    @property
    def size(self) -> int:
        return self.__size

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self):
        return f'{self.__id}: {self.__name}'


class StockItemRep:
    def __init__(self):
        self.__stock_items = {}
        self.__next_id = 1

    def __get_next_id(self) -> int:
        self.__next_id += 1
        return self.__next_id - 1

    def __getitem__(self, item_id):
        return self.__stock_items[item_id]

    def create_batch(self, item_cls, quantity: int, **kwargs):
        """ Возвращает генератор StockItem для заданных параметров"""

        starting_id = self.__next_id
        for _ in range(quantity):
            next_id = self.__get_next_id()
            item = item_cls(next_id, **kwargs)
            self.__stock_items[next_id] = item
            yield item


class Printer(StockItem):

    def __init__(self, item_id: int, name: str, size: int, cartridge_type: str):
        self.__cartridge_type = cartridge_type
        super().__init__(item_id, name, size)

    @property
    def cartridge_type(self):
        return self.__cartridge_type


class Scanner(StockItem):

    def __init__(self, item_id: int, name: str, size: int, resolution: str):
        self.__resolution = resolution
        super().__init__(item_id, name, size)

    @property
    def resolution(self):
        return self.__resolution


class Photocopier(StockItem):
    def __init__(self, item_id: int, name: str, size: int, speed: int):
        self.__speed = speed
        super().__init__(item_id, name, size)

    @property
    def resolution(self):
        return self.__speed


class NotEnoughSpace(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ItemAlreadyExists(ValueError):
    def __init__(self, msg):
        super().__init__(msg)


class ItemDoesntExist(ValueError):
    def __init__(self, msg):
        super().__init__(msg)


class Warehouse:
    def __init__(self, stock_items_rep: StockItemRep, name: str, num_lines: int, num_levels: int, num_slots: int):
        self.__name = name
        self.__stock_items_rep = stock_items_rep

        # склад организован как набор линий (стеллажей), в кажой линии один или несколько уровней (полок),
        # на каждом уровне одинаковое количество мест для размещения товара (ячеек)
        try:
            self.__max_lines = int(num_lines)
            self.__max_levels = int(num_levels)
            self.__max_slots = int(num_slots)
        except ValueError:
            raise ValueError('Размерности склада должны быть целыми числами')

        self.__empty_mark = 'Empty'
        self.__max_str_len = len(self.__empty_mark)

        # изначально все место на складе заполняется "пустотой" (self.__empty_mark)
        self.__location = [[[self.__empty_mark for _ in range(self.__max_slots)] for level in range(self.__max_levels)]
                           for line in range(self.__max_lines)]

        # Структура записи для учета товара:
        # {stock_item.id: [(line, level, slot), department]}
        self.__on_hand_items = {}

    def __reserve_location(self, stock_item_size: int) -> list:
        """
        Выделяет место на складе для товара согласно его размеру
        Возвращает список из координат [линия, уровень, ячейка]
        """

        if stock_item_size > self.__max_slots:
            raise NotEnoughSpace(f'На складе нет таких полок, чтобы вместить товар размером {stock_item_size}')

        line_idx = 0
        # обходим __location в поисках такого количества свободных ячеек подряд, чтобы вместить size товара
        for line in self.__location:
            level_idx = 0
            for level in line:
                slot_idx = 0
                free_slot = 0
                for slot in level:
                    if slot == self.__empty_mark:
                        free_slot += 1
                    else:
                        free_slot = 0
                    if free_slot >= stock_item_size:
                        return [line_idx + 1, level_idx + 1, slot_idx + 2 - stock_item_size]
                    slot_idx += 1
                level_idx += 1
            line_idx += 1
        raise NotEnoughSpace('На складе нет места')

    def receive_inventory(self, stock_item_cls, quantity: int, **kwargs) -> list:
        """ Выполняет прием товара(ов) на склад и возвращает список из id добавленных товаров"""

        try:
            quantity = int(quantity)
        except ValueError:
            raise ValueError('Количество товара должно быть целым числом')

        result = []
        for item in self.__stock_items_rep.create_batch(stock_item_cls, quantity, **kwargs):

            location = tuple(self.__reserve_location(item.size))
            on_hand_data = self.__on_hand_items.get(item.id)
            if on_hand_data:
                raise ItemAlreadyExists('Такой товар уже заргестрирован на складе')
            else:
                self.__on_hand_items[item.id] = [location, '']
                result.append(item.id)
                line, level, slot = location
                used_space = 0
                while used_space < item.size:
                    if len(str(item)) > self.__max_str_len:
                        self.__max_str_len = len(str(item))
                    self.__location[line - 1][level - 1][slot - 1 + used_space] = str(item)
                    used_space += 1
        return result

    def assign_department(self, department: str, stock_item_ids: list) -> None:
        for item_id in stock_item_ids:
            item = self.__on_hand_items.get(item_id)
            if item:
                item[1] = department
            else:
                raise ItemDoesntExist(f'На складе нет товара c таким id: {item_id}')

    def get_dep_analytics(self) -> dict:
        """
        Возворащает список с аналитикой по следующему шаблону:
        {department: {stock item class name: quantity}}
        """
        analytics = {}
        for item_id, data in self.__on_hand_items.items():
            department = data[1]
            dep_data = analytics.get(department)
            quantity = 0
            item_class = self.__stock_items_rep[item_id].__class__.__name__
            if dep_data:
                quantity = dep_data.get(item_class)
                if quantity is None:
                    quantity = 0
            else:
                dep_data = {}
            dep_data[item_class] = quantity + 1
            analytics[department] = dep_data
        return analytics

    def __str__(self):
        # Товары на складе
        result = f'Склад {self.__name}:'
        for line_num, line in enumerate(self.__location):
            result += f'\n\tЛиния {line_num + 1}'
            for level_num, level in enumerate(line):
                result += f'\n\t\tПолка {level_num + 1}\t|'
                for slot_num, slot in enumerate(level):
                    result += f'{slot.center(self.__max_str_len)}|'
                result += '\n'

        # Аналитика
        result += f'\nАнанлитика:\n'
        final_dep = ''
        analytics = self.get_dep_analytics()
        for department in analytics.keys():
            last_item = len(department) == 0
            if last_item:
                final_dep += f'\tНе привязано к подразделению:'
            else:
                result += f'\tНа балансе подразделения {department}:'
            for item_class, quantity in analytics[department].items():
                line = f'\n\t\t{item_class}: {quantity}шт'
                if last_item:
                    final_dep += line
                else:
                    result += line
            if not last_item:
                result += '\n'
        return result + final_dep


# main
if __name__ == '__main__':
    wh = Warehouse(StockItemRep(), 'Wh1', 2, 3, 5)
    printers = wh.receive_inventory(Printer, 4, name='Epson', size=1, cartridge_type='Ink')
    scanners = wh.receive_inventory(Scanner, 3, name='Canon', size=2, resolution='2400x2400')
    copiers = wh.receive_inventory(Photocopier, 2, name='Xerox', size=3, speed='70')
    wh.assign_department('R & D', printers[:2])
    wh.assign_department('Sales', printers[3:])
    wh.assign_department('R & D', copiers[:1])
    wh.assign_department('Sales', scanners[:1])
    wh.assign_department('R & D', scanners[1:])

    print(wh)
