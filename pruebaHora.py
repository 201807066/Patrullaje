from datetime import datetime, timedelta

# Definir las horas de inicio y fin
inicio = datetime.strptime('23:59', '%H:%M')  # Hora de inicio: 10:30
fin = datetime.strptime('00:01', '%H:%M')  # Hora de fin: 15:45

# Restar las horas
diferencia = fin - inicio

# Obtener la diferencia en horas y minutos
diferencia_horas = diferencia.seconds // 3600

diferencia_minutos = (diferencia.seconds // 60) % 60
print(len(str(diferencia_minutos)))



print("La diferencia de horas es:", diferencia_horas)
print("La diferencia de minutos es:", diferencia_minutos)