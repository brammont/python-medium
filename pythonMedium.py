text = "Hola a todos, esta es una cadena de texto de prueba."
unique = { c: c.upper() for c in text if c in 'aeiou' }

#Después:

text = "Hola a todos, esta es una cadena de texto de prueba."
unique = { c: text.count(c) for c in text if c in 'aeiou' }

#Mi código final:

def run():
    text = "Hola a todos, esta es una cadena de texto de prueba."
    print(text)
    unique = { c: text.count(c) for c in text if c in 'aeiou' }
    print(f"unique: {unique}")

run()

