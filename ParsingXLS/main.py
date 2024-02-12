import json
from datetime import date

import pandas as pd

# Leemos el archivo JSON
def leer_json():
    file = open("employees.json", "r")
    empleados = json.load(file)
    return empleados

empleados =leer_json()

# Flitrado para quitar del array a los empleados que estén en el proyecto GRONK
for item in empleados:
    if item['proyect'] == 'GRONK':
        empleados.remove(item)

# Ceamos los arrays donde van a ir guardados los diferentes datos del JSON y los llenamos con el dato deseado
salaries = []
for item in empleados:

    # Quitamos el símbolo del dolar y la coma con dos replace()
    salariostr = item['salary'].replace("$", "").replace(",", "")

    # Si es mayor de 30 metemos el salario nomal y si es menor le aplicamos la subida del 10%
    if item['age'] > 30:
        salaries.append(f'{salariostr}€')
    else:
        salario = float(salariostr) # Convertimos el String en un Float para poder realizar la operación de subida
        newsalary = round(salario + salario * 0.1, 2) # Hacemos que solo salgan dos decimales con round()
        salaries.append(f'{newsalary}€')

ages = []
for item in empleados:

        ages.append(item['age'])

names = []
for item in empleados:

        names.append(item['name'])

genders = []
for item in empleados:

        genders.append(item['gender'])

proyects = []
for item in empleados:

        proyects.append(item['proyect'])

emails = []
for item in empleados:

        emails.append(item['email'])

df = pd.DataFrame({'Salario': salaries, 'Edad': ages, 'Nombre': names, 'Genero': genders, 'Proyectos': proyects, 'Correos': emails})

df.index.name = 'ID'

# Generar el documento
df.to_excel(f'pagos-empleados-{date.today().month}-{date.today().year}.xlsx')
