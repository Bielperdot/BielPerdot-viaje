km= 225000000

for velocidades in range(10000, 50001, 10000):
    tiempo_horas = km / velocidades 
    tiempo_días = tiempo_horas / 24
    print("Para llegar a Marte a ", velocidades,"km/h" " se tardaría:",tiempo_días,"días")
