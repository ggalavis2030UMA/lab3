temperaturas = [18, 25, 31, 12, 28, 35, 20]
temperaturas_frias = 0
temperaturas_templadas = 0
temperaturas_calurosas = 0

for temperatura in temperaturas:
    if temperatura < 15:
        categoria = "fria"
        temperaturas_frias += 1
    elif temperatura <= 25:
        categoria = "templada"
        temperaturas_templadas += 1
    else:
        categoria = "calurosa"
        temperaturas_calurosas += 1

    print(f"La temperatura {temperatura} es {categoria}.")

print("=================")
print("Los dias frios son:", temperaturas_frias)
print("Los dias templados son:", temperaturas_templadas)
print("Los dias calurosos son:", temperaturas_calurosas)
print("=================")

