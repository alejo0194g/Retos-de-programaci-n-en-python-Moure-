"""/*
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

from datetime import datetime

def Calculador_Fecha(fecha1,fecha2):
    try:
        fecha1=str(fecha1).replace("/","-")
        fecha1=datetime.strptime(fecha1,"%d-%m-%Y")

        fecha2=str(fecha2).replace("/","-")
        fecha2=datetime.strptime(fecha2,"%d-%m-%Y")
        
        delta=abs(fecha1-fecha2)
        #print(fecha1,fecha2)
        print(f"Se tienen {delta.days} dias")
    except ValueError:
        print("Fecha incorrecta, ingresar en el siguiente formato: dd/mm/yy")

Calculador_Fecha("19/12/2023","18/10/2023")
Calculador_Fecha("18/10/2023","19/12/2023")