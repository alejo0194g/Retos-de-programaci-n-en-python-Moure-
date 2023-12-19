"""/*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

class Tradutor:
    def __init__(self, texto):
        self.texto=texto
        self.morse={
            'A':'.-', 'B':'-...', 'C':'-.-.', 
            'CH':'----', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.', 
            'Ñ':'--.--', 'O':'---', 'P':'.--.', 
            'Q':'--.-', 'R':'.-.', 'S':'...', 
            'T':'-', 'U':'..-', 'V':'...-',
            'W':'.--', 'X':'-..-', 'Y':'-.--', 
            'Z':'--..',
            '0':'-----', '1':'.----', '2':'..---', 
            '3':'...--', '4':'....-', '5':'.....', 
            '6':'-....', '7':'--...', '8':'---..', 
            '9':'----.', 
            '.':'.-.-.-', ',':'-.-.--', '?':'..--..', 
            '"':'.-..-.', '!':'--..--', ' ':' '}
        
    
    def natural_morse(self):
        string=""
        letra=""
        palabra=""
        
        for q in self.texto:
            letra += q
            cont=0
            if q ==" ":
                cont+=1
                string += list(self.morse.keys())[list(self.morse.values()).index(letra.rstrip())]
                letra="" 
            
        string += list(self.morse.keys())[list(self.morse.values()).index(letra)]
            

        return string

    def morse_natural(self):
        string=""
        for q in self.texto:
            if q ==" ":
                string += self.morse[q]+"  "
            else:
                string += self.morse[q]+" "

        return string

texto_morse=Tradutor("ALEJANDRO DUQUE")
print(texto_morse.morse_natural())
texto_natural=Tradutor(".- .-.. . .--- .- -. -.. .-. ---")
print(texto_natural.natural_morse())
