# 📚 Práctica Django – App de Libros

Este proyecto es una práctica técnica desarrollada con **Django**, enfocada en el manejo de una app llamada `libro`. El objetivo es aplicar conceptos fundamentales del framework, como modelos, vistas, templates y rutas, en un entorno funcional y extensible.

---

## 🧩 Características principales

- Registro y visualización de libros
- Estructura modular con apps Django
- Uso de base de datos SQLite
- Templates HTML básicos para renderizado
- Ideal como base para proyectos más complejos

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Django     | Framework web en Python |
| SQLite     | Base de datos ligera |
| HTML       | Plantillas para la interfaz |
| Python     | Lenguaje principal del backend |

---

## 🚀 Instalación y ejecución

- **Clona el repositorio**  
   ```bash
   git clone https://github.com/LordAlphons/practica_django.git
   cd practica_django/site_django
   ```

- Crea un entorno virtual (opcional)
  ```bash
  python -m venv env
  source env/bin/activate  # Linux/macOS
  .\env\Scripts\activate    # Windows
  ```
- Instala dependencias
  ```bash
  pip install -r requirements.txt
  ```
- Ejecuta migraciones
  ```bash
  python manage.py migrate
  ```
- Inicia el servidor
  ```bash
  python manage.py runserver
  ```

- Accede a la app
Abre tu navegador en http://127.0.0.1:8000

---

## 📁 Estructura del proyecto
```
site_django/
├── libro/              # App Django para gestión de libros
│   ├── models.py       # Modelo de datos
│   ├── views.py        # Lógica de vistas
│   ├── urls.py         # Rutas específicas de la app
│   └── templates/      # Plantillas HTML
├── site_django/        # Configuración principal del proyecto
├── manage.py           # Script de administración
└── requirements.txt    # Dependencias del proyecto
```

---

## 🧪 Posibles mejoras
- Paginación y búsqueda de libros
- Estilización con Bootstrap o Tailwind
- Exportación de datos en PDF o CSV
- API REST con Django REST Framework

---

## ✍️ Autor
Alfonso Garrido
Apasionado por DevOps, automatización y excelencia técnica.
🔗 GitHub

---

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
