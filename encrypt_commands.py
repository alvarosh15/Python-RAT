def progressive_caesar_encrypt(text):
    """
    Cifra el texto usando un método de cifrado César progresivo.
    
    En lugar de usar un desplazamiento fijo como en el cifrado César clásico, esta función aplica un desplazamiento que 
    incrementa con cada letra del texto. La primera letra se desplaza 1 posición en el alfabeto, la segunda se desplaza 
    2 posiciones, la tercera 3 posiciones, y así sucesivamente. El desplazamiento se reinicia en el alfabeto cuando llega 
    al final (cifrado modular). Solo se cifran los caracteres alfabéticos.

    Args:
        text (str): El texto a cifrar.
        
    Returns:
        str: El texto cifrado con desplazamientos progresivos.
    """
    result = ''
    shift = 1 

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            shift += 1 
        else:
            result += char

    return result

def main():
    print("Introduce un texto para cifrar. Escribe 'exitt' para salir.")
    
    while True:
        text = input("Texto: ")
        
        if text.lower() == 'exitt':
            print("Saliendo del programa.")
            break
        
        # Cifra el texto usando el método progresivo de César
        encrypted_text = progressive_caesar_encrypt(text)
        
        print(f"Texto cifrado: {encrypted_text}")

if __name__ == "__main__":
    main()