from db import Db


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
                size = 5
            elif counter < 5:
                size = 4
            elif counter < 13:
                size = 3
            elif counter < 27:
                size = 2
            else:
                size = 1
            color = avg_color
            text_boxes.append(TextBox(text, size, color))
            counter +=1


        for i in text_boxes:
            print(i.text, i.size, i. color)
        return text_boxes


    @staticmethod
    def normalize_color(var):
        temp = []
        if var == None:
            var = "#000"
        for i in var[1:]:
            temp.append(int(i.translate({ord("a"): "10", ord("b"): "11", ord("c"): "12",
                                         ord('d'): "13", ord('e'): "14", ord('f'): "15"})) * 16)
        return temp



TextBox.client()