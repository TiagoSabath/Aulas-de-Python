segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_seg = int(segundos_str)

horas = total_seg // 3600
segs_restantes = total_seg % 3600
minutos = segs_restantes // 60 
segs_restantes_final = segs_restantes % 60

print(horas, "Horas, ", minutos, "minutos e,",segs_restantes_final, "segundos.")