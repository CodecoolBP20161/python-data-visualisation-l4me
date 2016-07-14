from db import Db
from datetime import datetime


class TextBox():
    def __init__(self, text, size, color):
        self.text = text
        self.size = size
        self.color = color

    @staticmethod
    def client():
        data = Db.execute_query("SELECT company_name, main_color FROM project")
        lista = [i[0] for i in data]
        lista_color = [TextBox.normalize_color(i[1]) for i in data]
        clients = dict(zip(lista, [0] * len(lista)))
        for i in lista:
            clients[i] += 1
        clients_list = list(sorted(clients, key = clients.get, reverse = True))
        ultimate =  [[x, lista_color[i]] for i, x in enumerate(lista)]

        counter = 0
        text_boxes = []
        for i in clients_list:
            avg_color = [0,0,0]
            for j in ultimate:
                if i == j[0]:
                    avg_color[0] += j[1][0]
                    avg_color[1] += j[1][1]
                    avg_color[2] += j[1][2]
            avg_color[0]//=clients[i]
            avg_color[1]//=clients[i]
            avg_color[2]//=clients[i]
            text = i
            if counter < 1:
                size = 4
            elif counter < 5:
                size = 3
            elif counter < 13:
                size = 2
            elif counter < 27:
                size = 1
            else:
                size = 0
            color = tuple(avg_color)
            text_boxes.append(TextBox(text, size, color))
            counter +=1

       # print(clients)
        #for i in text_boxes:
         #   print(i.text, i.size, i. color)
        return text_boxes

    @staticmethod
    def project():
        data = Db.execute_query("SELECT name, budget_value, main_color, CASE WHEN budget_currency ='EUR' THEN '315' WHEN budget_currency = 'USD' THEN '260' WHEN budget_currency = 'GBP' THEN '400' ELSE budget_currency END FROM project")
        project_lista = [i[0] for i in data if i[0] != None]
        lista_color = [TextBox.normalize_color(i[2]) for i in data if i[0] != None]
        currency = [(i[3]) for i in data if i[0] != None]
        budget = [i[1] for i in data if i[0] != None]

        currency = map(int, currency)
        budget = map(float, budget)
        exchanged_budget = [a*b for a,b in zip(budget, currency)]

        ultimate = [[x, lista_color[i]] for i, x in enumerate(project_lista)]
        a_ultimate = [[x[0],x[1], exchanged_budget[i]] for i,x in enumerate(ultimate)]
        a_ultimate= list(sorted(a_ultimate, key = lambda x: x[2], reverse = True))


        text_boxes = []
        counter = 0
        for i in a_ultimate:
            text = i[0]
            color = tuple(i[1])
            if counter < 1:
                size = 4
            elif counter < 5:
                size = 3
            elif counter < 17:
                size = 2
            elif counter < 42:
                size = 1
            else:
                size = 0
            text_boxes.append(TextBox(text,size,color))
            counter +=1

        return text_boxes
       # for i in text_boxes:
        #    print(i.text, i.size, i.color)

    '''
    @staticmethod
    def date():
        data = Db.execute_query("SELECT name, duedate, main_color FROM project WHERE name != 'None'")
        name = [x[0] for x in data if x[0] != None]
        date = [datetime.datetime(x[1]) for x in data if x[0] != None]
        color = [TextBox.normalize_color([2]) for x in data if x[0] != None]
        print(name)
        print(date)
        print(color)
    '''




    @staticmethod
    def normalize_color(var):
        temp = []
        if var == None:
            var = "#000"
        for i in var[1:]:
            temp.append(int(i.translate({ord("a"): "10", ord("b"): "11", ord("c"): "12",
                                         ord('d'): "13", ord('e'): "14", ord('f'): "15"})) * 16)
        return temp




TextBox.project()
TextBox.client()
#TextBox.date()