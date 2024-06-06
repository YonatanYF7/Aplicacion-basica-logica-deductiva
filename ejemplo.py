import sympy as sp

# Base de Hechos:
# Interfaz de Usuario:
# Entrada de Datos del Usuario
# Solicitar al usuario ingresar si Koba es un simio o no
koba_simio_input = input("¿Es Koba un simio? (Sí/No): ").strip().lower()
koba_simio = koba_simio_input == 'si' or koba_simio_input == 'sí'  # Convertir la entrada a un valor booleano

# Base de Conocimientos:
# Definir las proposiciones
simio_no_mata_simio = sp.symbols('Simio_no_mata_simio')
simio_si_mata_simio = sp.symbols('Simio_si_mata_simio')
  
# Definir las premisas
premisa1 = sp.Implies(koba_simio, simio_no_mata_simio)  # Si Koba es un simio, entonces simio no mata simio
premisa2 = sp.Implies(sp.Not(koba_simio), simio_si_mata_simio)  # Si Koba no es un simio, entonces simio sí mata simio

# Motor de Inferencia:
# Verificar las premisas
conclusion1 = sp.simplify(premisa1)
conclusion2 = sp.simplify(premisa2)

# Verificar las implicaciones
resultado1 = sp.Implies(conclusion1, simio_no_mata_simio)
resultado2 = sp.Implies(conclusion2, simio_si_mata_simio)

# Interfaz de Usuario:
# Salida de Resultados
# Imprimir la conclusión correspondiente
if koba_simio:
    if resultado1:
        print("Simio no mata simio")
else:
    if resultado2:
        print("Koba mata simio")
