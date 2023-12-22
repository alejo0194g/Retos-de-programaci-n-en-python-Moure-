"""/*
 * Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Fecha publicación enunciado: 04/04/22
 * Fecha publicación resolución: 11/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

def Amstrong(numero):
    lista=[]
    exp=0
    valor=0
    
    for q in str(numero):
        if q !="-":
            lista.append(int(q))
    
    exp=len(lista)

    
    for i in lista:
        valor += (i**exp)#Calcula la suma de sus exponentes

    if numero<0 and numero==-1*valor:
        print(str(numero)+ " es un número Amstrong")

    elif numero>=0 and numero==valor:
        print(str(numero)+ " es un número Amstrong")

    else:
        print(str(numero)+ " no es un número Amstrong")
    

Amstrong(372)
Amstrong(0)
Amstrong(371)

