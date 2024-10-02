libro1 = {
    "titulo": "Django 3 Web Development Cookbook Fourth Edition",
    "autor": "Aidas Bendoraitis",
    "valoracion": 3250
}
 
libro2 = {
    "titulo": "Two Scoops of Django 3.x",
    "autor": "Daniel Feldroy",
    "valoracion": 1570
}
 
libro3 = {
    "titulo": "El libro de Django",
    "autor": "Adrian Holovaty",
    "valoracion": None  # No tiene valoración
}
 
libro4 = {
    "titulo": "Python Web Development with Django",
    "autor": "Jeff Forcier",
    "valoracion": None  # No tiene valoración
}
 
libro5 = {
    "titulo": "Django for Professionals",
    "autor": "William S. Vincent",
    "valoracion": 2100
}
 
libro6 = {
    "titulo": "Django for APIs",
    "autor": "William S. Vincent",
    "valoracion": 2540
}

libros = [ libro1, libro2, libro3, libro4, libro5, libro6 ]

def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas y eliminamos caracteres que no son letras o números
    palabra_limpia = ''.join(c for c in palabra.lower() if c.isalnum())
    
    # Verificamos si la palabra es igual a su versión invertida
    return palabra_limpia == palabra_limpia[::-1]