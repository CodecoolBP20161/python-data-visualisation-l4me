from db import Db
import random


class TextBox():
    def __init__(self, text, size, color):
        self.text = text
        self.size = size
        self.color = color

    @classmethod
    def client(cls):
        data = [[i[0], cls.normalize_color(i[1])]
                for i in Db.execute_query("SELECT company_name, main_color FROM project")]
        clients_list = sorted([[i, len([j for j in data if j[0] == i])] for i in set([i[0] for i in data])],
                              key=lambda i: i[1], reverse=True)

        text_boxes = []
        for i, k in enumerate(clients_list):
            color = [sum([i[1][j] // k[1] for i in data if i[0] == k[0]]) for j in range(3)]
            text_boxes.append(cls(k[0], cls.size_calculate(i, 1), tuple(color)))

        return text_boxes

    @classmethod
    def project(cls):
        data = sorted([[i[0], float(i[1])*cls.currency_exchange(i[3]), cls.normalize_color(i[2])]
                      for i in Db.execute_query("SELECT name, budget_value, main_color, budget_currency FROM project")
                      if i[0] is not None], key=lambda i: i[1], reverse=True)

        return [cls(k[0], cls.size_calculate(i), tuple(k[2])) for i, k in enumerate(data)]

    @classmethod
    def date(cls):
        data = [[i[0], cls.normalize_color(i[1])] for i in
                Db.execute_query("SELECT name, main_color FROM project WHERE name != 'None' ORDER BY duedate DESC")]

        return [cls(k[0], cls.size_calculate(i), tuple(k[1])) for i, k in enumerate(data)]

    @classmethod
    def len_name(cls):
        data = sorted([[i[0], cls.normalize_color(i[1])] for i in
                      Db.execute_query('''SELECT name,  main_color FROM project
                      WHERE name !='None' ORDER BY LENGTH(name) DESC''')], key=lambda i: len(i[0]), reverse=True)

        return [cls(k[0], cls.size_calculate(i), tuple(k[1])) for i, k in enumerate(data)]

    @classmethod
    def easteregg(cls, extra):
        data = sorted([[i[0], cls.currency_coloring(i[2]), float(i[1])*cls.currency_exchange(i[2]), i[2]] for i in
                      Db.execute_query('''SELECT name, budget_value, budget_currency
                      FROM project WHERE name !='None' ''')], key=lambda i: i[2], reverse=True)

        if extra:
            data = [["BREXIT", (0, 0, 0)] if i[3] == "GBP" else [i[0], i[1]] for i in data]

        return [cls(k[0], cls.size_calculate(i), tuple(k[1])) for i, k in enumerate(data)]

    @staticmethod
    def size_calculate(index, version=0):
        size = 4
        for i in [[1, 1], [5, 5], [17, 13], [42, 27]]:
            size = size-1 if index >= i[version] else size
        return size

    @staticmethod
    def normalize_color(var):
        temp = []
        if var is None:
            var = "#000"
        for i in var[1:]:
            temp.append(int(i.translate({ord("a"): "10", ord("b"): "11", ord("c"): "12",
                                         ord('d'): "13", ord('e'): "14", ord('f'): "15"})) * 16)
        return temp

    @staticmethod
    def currency_exchange(curr):
        return {"EUR": 315, "USD": 260, "GBP": 400}[curr]

    @staticmethod
    def currency_coloring(curr):
        options = random.choice([50, 100, 150, 200, 250])
        return {"EUR": (0, 0, options), "USD": (0, options, 0), "GBP": (options, 0, 0)}[curr]
