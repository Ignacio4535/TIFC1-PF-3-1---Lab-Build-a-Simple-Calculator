
#suma de los numeros 

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

Resultado_suma = num1 + num2

print("El resultado de la suma es:", Resultado_suma)


#Opcionales
# while True:

#     print("\n=== CALCULADORA ===")
#     print("1. Para restar")
#     print("2. Para multiplicacion")
#     print("3. Para dividir")
#     print("4. Sobras")
#     print("5. Suma de tres numeros")
#     print("6. Operaciones mixtas")
#     print("7. Salir")

#     opcion = input("Seleccione una opcion: ")

#     # Para que resté
#     if opcion == "1":

#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))

#         resultado = num1 - num2

#         print("El resultado de su resta es:", resultado)

#     # Para multiplicar
#     elif opcion == "2":

#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))

#         resultado = num1 * num2

#         print("El resultado de su multiplicacion es", resultado)

#     # Para dividir
#     elif opcion == "3":

#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))

#         if num2 != 0:
#             resultado = num1 / num2
#             print("El resultado de su divicion es:", resultado)
        
#     # Cuanto sobra
#     elif opcion == "4":

#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))

#         if num2 != 0:
#             resultado = num1 % num2
#             print("Sobran:", resultado)
       
#     # SUMA DE TRES NUMEROS
#     elif opcion == "5":

#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))
#         num3 = float(input("Ingrese el tercer numero: "))

#         resultado = num1 + num2 + num3

#         print("Resultado de la suma:", resultado)

#     # Mixtas 
#     elif opcion == "6":
#         print("Esta operacion va a sumar el primer numero con el segundo y dividir con el tercero")

#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))
#         num3 = float(input("Ingrese el tercer numero: "))

#         resultado = num1 + num2 % num3

#         print("Su resultado de la operacion mixta:", resultado)

#     # SALIR
#     elif opcion == "7":

#         print("Ahi estan sus resultados muchas gracias por usarme como calculadora")
#         break
