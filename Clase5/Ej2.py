from os import startfile, system
class Node:
    def __init__(self, color):
        self.color = color
        self.next = None


class Lista:
    def __init__(self):
        self.first = None
        self.rows = 0
        self.columns = 0
        self.size = 0
        self.nombreP = ""
        self.codigoP = ""

    def insert(self, data):
        nuevo = Node(data)
        if self.first == None:
            self.first = nuevo
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    def crearGraphviz(self):
        if self.rows == 0 or self.columns == 0:
            print('DIMENSIONES INVÁLIDAS:')
            return

        textoDOT = ''' digraph G { \n
        node [shape=plaintext]; \n
        edge [style=invis]; \n

        label = \"nombrePiso =  ''' + self.nombreP + ''' - PATRON = ''' + self.codigoP + '''\"
        \n

        piso [\n label=<<TABLE border = \"1\" cellspacing=\"0\" cellpadding=\"10\">
        '''

        actual = self.first
        for i in range(self.rows):
            textoDOT += "         <tr>"
            for j in range(self.columns):
                if actual.color == "W":
                    textoDOT += f"<td bgcolor=\"white\"></td>"
                elif actual.color == "B":
                    textoDOT += f"<td bgcolor=\"black\"></td>"
                actual = actual.next
            textoDOT += "         </tr>\n"

        textoDOT += "</TABLE>>\n shape=none\n ];"
        textoDOT += "}\n"

        with open("ejemplo2.dot", "w") as dot_file:
            dot_file.write(textoDOT)

        system('dot -Tpdf ejemplo2.dot -o ejemplo2.pdf')
        startfile("ejemplo2.pdf")

if __name__ == '__main__':
    lista = Lista()
    pattern = "WBWBWBWBWBWB"

    for color in pattern:
        # print(color)
        lista.insert(color)
        print('Se agregó el color: ', color, ' a la lista.')

    lista.rows = 4
    lista.columns = 3
    lista.nombreP = "Piso 1"
    lista.codigoP = "A01"

    lista.crearGraphviz()
