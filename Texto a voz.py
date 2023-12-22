"""
    Convertir texto a voz (TTS) con
    Python usando gTTS
    Ejemplo 1: Escribir hola mundo en un archivo, en idioma español
    @author parzibyte
"""
from gtts import gTTS
tts = gTTS('Hola mundo, este codigo convierte texto a voz', lang='es-us')
tts.save("1_hola_mundo.mp3")