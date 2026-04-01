import simplejson as json
import time

# Abrir y cargar el JSON
with open('myfile.json', 'r') as file:
    variable_json = json.load(file)

# Imprimir el contenido
print("Contenido de la variable:", variable_json)

# Mostrar token y calcular tiempo
token = variable_json['token']
expiracion = variable_json['expires_at']
tiempo_actual = time.time()
tiempo_restante = expiracion - tiempo_actual

print("Token:", token)
print("Tiempo restante (segundos):", int(tiempo_restante))
