🤖 Telegram Data Bot - Procesador Dinámico de Archivos .CSV
Este proyecto consiste en un Chatbot de Telegram diseñado para recibir, leer y analizar estructuras de datos variables. Desarrollado como parte del Módulo 5: Aprendizaje Automático en el Técnico en IA de INFOTEP, con un enfoque en la manipulación técnica de archivos y lógica de programación.
🚀 Funcionalidades Principales
•	Procesamiento de Archivos CSV: El bot es capaz de recibir archivos .csv enviados por el usuario a través del chat.
•	Adaptabilidad de Columnas: Implementa lógica dinámica para interpretar diferentes nombres de encabezados (ej. "Venta", "Total", "Ingresos") sin necesidad de reconfigurar el código.
•	Análisis Automático: Calcula totales, promedios e identifica valores máximos/mínimos según el archivo proporcionado.
•	Gestión de Sesiones: Mantiene una interacción fluida con el usuario mediante la API de Telegram.
•	Entorno Aislado: Configurado mediante venv para asegurar que las dependencias no entren en conflicto con otros proyectos.
🛠️ Stack Tecnológico
•	Lenguaje: Python 3.11.9
•	Interfaz de Bot: python-telegram-bot (Librería principal para la comunicación con Telegram).
•	Manipulación de Datos: pandas / csv (Para el parsing y análisis de los archivos).
•	Entorno: Visual Studio Code / PowerShell.
📂 Estructura del Proyecto
⚙️ Instalación y Ejecución
1.	Navegar a la carpeta del proyecto:
2.	Activar el entorno virtual:
3.	Instalar librerías necesarias: Si experimentas errores con el launcher de pip, utiliza:
4.	Ejecutar el Bot:
📊 Casos de Uso Testeados
El sistema ha sido validado con los siguientes tipos de datos:
•	Ventas por Empleado: Validación de strings y montos básicos.
•	Ventas por Producto: Prueba de flexibilidad en nombres de columnas.
•	Rendimiento de Sucursales: Manejo de valores numéricos de gran escala.
•	Tráfico Web: Análisis de variabilidad de datos por días.
________________________________________
Autor: Nelson Miñoso estudiante del Técnico en IA - TEOREMA (INFOTEP) 
Módulo: Aprendizaje Automático (Fase de Procesamiento de Datos)
