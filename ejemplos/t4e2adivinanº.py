def numero_ganador(numero):
    if numero == 4:
        return "¡Acertaste!."
    else:
        return "¡Fallaste!."


numero_introducido = int(input("Elige un numero del 1 al 10: "))

resultado = numero_ganador(numero_introducido)

print("Numero selecionado:", numero_introducido)
print("Resultado:", resultado)