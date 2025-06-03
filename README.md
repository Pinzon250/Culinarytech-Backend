# Documentation for Culinarytech project

                    Como ejecutar el proyecto

    • Instalar archivos desde el repositorio (.zip)
    • Tener python 3.13 Instalado
          Se puede instalar desde la Microsoft Store

    Ejecutar Backend:
        • Desde la consola acceder al archivo (Powershell recomendado):
            1. cd (Ruta donde esta guardado)
            Ej: cd C:\Users\Usuario\Desktop\Culinarytech
            2. code . (Abrir en VSC)
        • Crear y activar entorno virtual:
            Acceder a la ruta del backend para crear entorno virtual:
            Ej: cd C:...\Culinarytech\backend
            Crear: python -m venv (nombre de su entorno virtual)
            Ej: python -m venv env
            Activar:  .\(nombre del entorno virtual)\Scripts\Activate.ps1
        • Instalar dependencias necesarias
            1. pip install -r requirements.txt
        • Ejecutar backend:
            1. uvicorn app.main:app --reload

        -----------------------------------------------------------------------

    Ejecutar Frontend:
        • Instalar node.js:
            1. https://nodejs.org/en
        • Desde la consola acceder al archivo
            1. cd C:...\Culinarytech\frontend
        • Colocar npm install para instalar las dependencias del proyecto
        • Colocar npm run dev para correr el frontend del proyecto
