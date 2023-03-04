"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01(Idata = 'data.csv'):
    """
    Retorne la suma de la segunda columna. Evaluemos el cambio a ver
    Rta/ 214
    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    value = 0
    for i in data:
        value += int(i[1])
    return value

def pregunta_02(Idata = 'data.csv'):
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    col = []
    rpta = []
    let = ['A', 'B', 'C', 'D', 'E']
    for row in data:
        col.append(row[0])
    for j in let:
        rpta.append((j, col.count(j)))
    return rpta

def pregunta_03(Idata = 'data.csv'):
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    contar = list(range(len(data)))
    A = []
    B = []
    C = []
    D = []
    E = []
    for item in contar:
        c = data[item][0]
        if c == 'A':
            A.append(int(data[item][1]))
        elif c == 'B':
            B.append(int(data[item][1]))
        elif c == 'C':
            C.append(int(data[item][1]))
        elif c == 'D':
            D.append(int(data[item][1]))
        else:
            E.append(int(data[item][1]))
    rpta = [
        ("A", sum(A)),
        ("B", sum(B)),
        ("C", sum(C)),
        ("D", sum(D)),
        ("E", sum(E))
    ]
    return rpta

def pregunta_04(Idata = 'data.csv'):
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    Vrpta=[]
    d = []

    for row in data:
        c=row[2]
        d = c.split("-")
        Vrpta.append(str(d[1]))

    rpta=[
        ("01",Vrpta.count("01")),
        ("02",Vrpta.count("02")),
        ("03",Vrpta.count("03")),
        ("04",Vrpta.count("04")),
        ("05",Vrpta.count("05")),
        ("06",Vrpta.count("06")),
        ("07",Vrpta.count("07")),
        ("08",Vrpta.count("08")),
        ("09",Vrpta.count("09")),
        ("10",Vrpta.count("10")),
        ("11",Vrpta.count("11")),
        ("12",Vrpta.count("12"))
    ]

    return rpta

def pregunta_05(Idata = 'data.csv'):
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    contar = list(range(len(data)))
    A = []
    B = []
    C = []
    D = []
    E = []
    for item in contar:
        c = data[item][0]
        if c == 'A':
            A.append(int(data[item][1]))
        elif c == 'B':
            B.append(int(data[item][1]))
        elif c == 'C':
            C.append(int(data[item][1]))
        elif c == 'D':
            D.append(int(data[item][1]))
        else:
            E.append(int(data[item][1]))
    rpta = [
        ("A", max(A), min(A)),
        ("B", max(B), min(B)),
        ("C", max(C), min(C)),
        ("D", max(D), min(D)),
        ("E", max(E), min(E))
    ]

    return rpta

def pregunta_06(Idata = 'data.csv'):
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    e = []
    letter = []
    number = []
    for row in data:
        celda = (row[4])
        d = celda.split(",")
        n = len(d)
        for i in range(n):
            e.append(d[i].split(":"))
    for j in e:
        letter.append(j[0])
        number.append(int(j[1]))

    letras = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    I = []
    J = []

    b = len(letter)
    for u in range(b):
        if letter[u] == letras[0]:
            A.append(number[u])
        elif letter[u]  == letras[1]:
            B.append(number[u])
        elif letter[u] == letras[2]:
            C.append(number[u])
        elif letter[u] == letras[3]:
            D.append(number[u])
        elif letter[u] == letras[4]:
            E.append(number[u])
        elif letter[u] == letras[5]:
            F.append(number[u])
        elif letter[u] == letras[6]:
            G.append(number[u])
        elif letter[u] == letras[6]:
            G.append(number[u])
        elif letter[u] == letras[7]:
            H.append(number[u])
        elif letter[u] == letras[8]:
            I.append(number[u])
        else:
            J.append(number[u])

    rpta= [
        (letras[0], min(A), max(A)),
        (letras[1], min(B), max(B)),
        (letras[2], min(C), max(C)),
        (letras[3], min(D), max(D)),
        (letras[4], min(E), max(E)),
        (letras[5], min(F), max(F)),
        (letras[6], min(G), max(G)),
        (letras[7], min(H), max(H)),
        (letras[8], min(I), max(I)),
        (letras[9], min(J), max(J))
    ]

    return rpta

def pregunta_07(Idata = 'data.csv'):
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    CERO = []
    UNO = []
    DOS = []
    TRES = []
    CUATRO = []
    CINCO = []
    SEIS = []
    SIETE = []
    OCHO = []
    NUEVE = []

    for row in data:
        if row[1] == str(numbers[0]):
            CERO.append(row[0])
        elif row[1] == str(numbers[1]):
            UNO.append(row[0])
        elif row[1] == str(numbers[2]):
            DOS.append(row[0])
        elif row[1] == str(numbers[3]):
            TRES.append(row[0])
        elif row[1] == str(numbers[4]):
            CUATRO.append(row[0])
        elif row[1] == str(numbers[5]):   
            CINCO.append(row[0])
        elif row[1] == str(numbers[6]):
            SEIS.append(row[0])
        elif row[1] == str(numbers[7]):
            SIETE.append(row[0])
        elif row[1] == str(numbers[8]):
            OCHO.append(row[0])
        else:
            NUEVE.append(row[0])

    rpta = [
        (numbers[0], CERO),
        (numbers[1], UNO),
        (numbers[2], DOS),
        (numbers[3], TRES),
        (numbers[4], CUATRO),
        (numbers[5], CINCO),
        (numbers[6], SEIS),
        (numbers[7], SIETE),
        (numbers[8], OCHO),
        (numbers[9], NUEVE)
    ]
    return rpta

def pregunta_08(Idata = 'data.csv'):
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    numbers=[0,1,2,3,4,5,6,7,8,9]
    CERO=[]
    UNO=[]
    DOS=[]
    TRES=[]
    CUATRO=[]
    CINCO=[]
    SEIS=[]
    SIETE=[]
    OCHO=[]
    NUEVE=[]

    for row in data:
        if row[1]==str(numbers[0]):
            CERO.append(row[0])
        elif row[1]==str(numbers[1]):
            UNO.append(row[0])
        elif row[1]==str(numbers[2]):
            DOS.append(row[0])
        elif row[1]==str(numbers[3]):
            TRES.append(row[0])
        elif row[1]==str(numbers[4]):
            CUATRO.append(row[0])
        elif row[1]==str(numbers[5]):
            CINCO.append(row[0])
        elif row[1]==str(numbers[6]):
            SEIS.append(row[0])
        elif row[1]==str(numbers[7]):
            SIETE.append(row[0])
        elif row[1]==str(numbers[8]):
            OCHO.append(row[0])
        else:
            NUEVE.append(row[0])

    rpta= [
        (numbers[0],sorted(set(CERO))),
        (numbers[1],sorted(set(UNO))),
        (numbers[2],sorted(set(DOS))),
        (numbers[3],sorted(set(TRES))),
        (numbers[4],sorted(set(CUATRO))),
        (numbers[5],sorted(set(CINCO))),
        (numbers[6],sorted(set(SEIS))),
        (numbers[7],sorted(set(SIETE))),
        (numbers[8],sorted(set(OCHO))),
        (numbers[9],sorted(set(NUEVE)))
        ]

    return rpta

def pregunta_09(Idata = 'data.csv'):
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    e = []
    letter = []
    for row in data:
        celda = (row[4])
        d = celda.split(",")
        n = len(d)
        for i in range(n):
            e.append(d[i].split(":"))
    for j in e:
        letter.append(j[0])
    rpta = {
        'aaa': letter.count('aaa'),
        'bbb': letter.count('bbb'),
        'ccc': letter.count('ccc'),
        'ddd': letter.count('ddd'),
        'eee': letter.count('eee'),
        'fff': letter.count('fff'),
        'ggg': letter.count('ggg'),
        'hhh': letter.count('hhh'),
        'iii': letter.count('iii'),
        'jjj': letter.count('jjj')
        }
    return rpta

def pregunta_10(Idata = 'data.csv'):
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    letras = []
    coltres = []
    colcuatro = []

    for row in data:
        letras.append(row[0])
        d = row[3].split(",")
        f = row[4].split(",")
        coltres.append(len(d))
        colcuatro.append(len(f))

    rpta = []

    k = range(len(letras))

    for i in k:
        rpta.append((letras[i],coltres[i],colcuatro[i]))

    return rpta

def pregunta_11(Idata = 'data.csv'):
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    pre = []
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []

    for row in data:
        pre = row[3].split(",")
        for j in range(int(len(pre))):
            if pre[j] == "a":
                A.append(int(row[1]))
            elif pre[j] == "b":
                B.append(int(row[1]))
            elif pre[j] == "c":
                C.append(int(row[1]))
            elif pre[j] == "d":
                D.append(int(row[1]))
            elif pre[j] == "e":
                E.append(int(row[1]))
            elif pre[j] == "f":
                F.append(int(row[1]))
            else:
                G.append(int(row[1]))

    rpta = {
        'a': sum(A),
        'b': sum(B),
        'c': sum(C),
        'd': sum(D),
        'e': sum(E),
        'f': sum(F),
        'g': sum(G)
    }


    return rpta

def pregunta_12(Idata = 'data.csv'):
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    open_file = open(Idata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    valuesA = []
    valuesB = []
    valuesC = []
    valuesD = []
    valuesE = []

    for row in data:
        val = row[4].split(",")
        for i in range(len(val)):
            values = val[i].split(":")
            if row[0] == 'A':
                valuesA.append(int(values[1]))
            elif row[0] == 'B':
                valuesB.append(int(values[1]))
            elif row[0] == 'C':
                valuesC.append(int(values[1]))
            elif row[0] == 'D':
                valuesD.append(int(values[1]))
            else:
                valuesE.append(int(values[1]))

    rpta = {
        'A': sum(valuesA),
        'B': sum(valuesB),
        'C': sum(valuesC),
        'D': sum(valuesD),
        'E': sum(valuesE),
    }

    return rpta

