# analyticsdevs_project

Portfolio Django project for Gerardo Martínez.

## Descripción

Aplicación Django que contiene:

- `core`: página de inicio y API de chat con Google Gemini.
- `portafolio`: casos de estudio y detalle de proyectos.
- `eventos`: página de inscripción para eventos.
- Configuración de Google Analytics y correo.

## Requisitos

- Python 3.11+ (recomendado)
- `pip`
- `virtualenv` o entornos virtuales de Python

## Instalación local

1. Clona el repositorio o copia el proyecto en tu máquina.

2. Navega a la carpeta del proyecto:

```bash
cd c:\Users\Gera\Desktop\Portafolio-Profesional\analyticsdevs_project
```

3. Crea y activa un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Instala las dependencias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuración de entorno

Copia el archivo de ejemplo y ajusta los valores:

```bash
copy .env.example .env
```

Edita `.env` y agrega los valores correspondientes:

```env
SECRET_KEY=django-insecure-...       # Genera una clave segura para desarrollo / producción
DEBUG=True                           # Usa False en producción
GEMINI_API_KEY=tu_gemini_api_key     # Necesaria para la API de chat en core/views.py
EMAIL_HOST_USER=tu_correo@gmail.com  # Opcional: si quieres enviar emails reales
EMAIL_HOST_PASSWORD=tu_contraseña    # Opcional: contraseña de app o SMTP
GA_MEASUREMENT_ID=G-XXXXXXXXXX       # Opcional: para Google Analytics en plantillas
GA_PROPERTY_ID=123456789             # Opcional
GA_SERVICE_ACCOUNT_PATH=path/to/key.json # Opcional, solo si usas cuenta de servicio
GA_SERVICE_ACCOUNT_JSON="{...}"    # Opcional, alternativa a GA_SERVICE_ACCOUNT_PATH
```

> Si no configuras `EMAIL_HOST_USER` y `EMAIL_HOST_PASSWORD`, Django usará el backend de consola y no fallará.

## Base de datos

Este proyecto usa SQLite por defecto.

1. Aplica migraciones:

```bash
python manage.py migrate
```

2. (Opcional) Crea un superusuario para acceder al admin:

```bash
python manage.py createsuperuser
```

## Archivos estáticos

Durante el desarrollo, Django carga `core/static` automáticamente.

Para producción o antes de desplegar, ejecuta:

```bash
python manage.py collectstatic
```

Los archivos se recopilan en `staticfiles/`.

## Levantar el proyecto

Inicia el servidor de desarrollo con:

```bash
python manage.py runserver
```

Luego abre en el navegador:

- `http://127.0.0.1:8000/` para la página principal
- `http://127.0.0.1:8000/admin/` para el admin de Django

## Rutas importantes

- `/` - Home
- `/api/chat/` - API de chat (POST)
- `/eventos/registro/<slug>/` - Inscripción a evento

## Dependencias principales

- Django 5.2.7
- python-dotenv
- python-decouple==3.8
- google-genai==2.10.0
- Markdown==3.4.4
- whitenoise
- gunicorn
- google-analytics-data (opcional)

## Notas importantes

- La API de chat (`/api/chat/`) requiere `GEMINI_API_KEY` definida en `.env`.
- `GA_MEASUREMENT_ID` y `GA_SERVICE_ACCOUNT_*` son opcionales, pero habilitan Google Analytics.
- Si usas Gmail para correo, configura una contraseña de aplicación o SMTP válido.

## Solución de problemas

- `ModuleNotFoundError: No module named 'django'`: activa el entorno virtual e instala dependencias.
- `KeyError` o falta de `.env`: copia `.env.example` y completa las variables.
- `sqlite3` no encontrado: instala SQLite o usa otra base de datos configurando `DATABASES` en `analyticsdevs_project/settings.py`.

## Mejoras sugeridas

- Añadir `requirements-dev.txt` con herramientas de lint y test.
- Documentar plantillas faltantes para `portafolio/detalle_caso.html`.
- Crear un `.env.example` con variables mínimas.
