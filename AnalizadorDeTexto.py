texto = input("Ingresa un texto, el que quieras: ")
letras = []

texto = texto.lower()

letras.append(input ("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra ").lower())
letras.append(input ("Ingresa la tercera letra: ").lower())

print("\n")

print("Cantidad de letras: ")

cant_de_letras1 = texto.count(letras[0])
cant_de_letras2 = texto.count(letras[1])
cant_de_letras3 = texto.count(letras[2])

print(f"Primer letra({letras[0]}): {cant_de_letras1}\n Segunda letra({letras[1]}): {cant_de_letras2}\n Tercer letra({letras[2]}): {cant_de_letras3}")

print("\n")
print("Cantidad de palabras: ")
cant_de_palabras = texto.split()

print(f"Se encontraron: {len(cant_de_palabras)} en tu texto")

print("\n")

print("Letras de inicio y del final")
letra_inicio = texto[0]
letra_final = texto[-1]

print(f"La letra inicial es: '{letra_inicio}'\n La letra final es'{letra_final}'")

print("\n")

print("Texto invertido")

cant_de_palabras.reverse()
texto_invertido = " ".join(cant_de_palabras)

print(f"Tu texto dado vuelta es: {texto_invertido}")

print("\n")

print("Esta la palabra python?")

buscar_python = "python" in texto

dic = {True : "si esta", False : "no esta"}

print(f"La palabra python, {dic[buscar_python]}")