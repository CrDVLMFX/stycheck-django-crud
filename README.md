# Stycheck — Módulo Servicios (Django)

Evidencia **GA7-220501096-AA2-EV01** — Codificación de módulos del software
según requerimientos del proyecto. Módulo elegido: **Catálogo de Servicios**
(RF08, RF09 de Stycheck).

## 1. Requisitos previos
- Python 3.x instalado
- Laragon (trae MySQL 8 integrado) — inícialo antes de correr el proyecto
- Visual Studio Code
- Git

## 2. Crear la base de datos
1. Abre Laragon → inicia el servidor MySQL
2. Entra a HeidiSQL (o el gestor que uses) y crea una base de datos vacía llamada `stycheck`

## 3. Preparar el entorno virtual
Desde la carpeta `stycheck_django`:

```
python -m venv .venv
.venv\Scripts\activate
```

## 4. Instalar dependencias

```
pip install -r requirements.txt
```

Si `mysqlclient` da error al instalar en Windows, prueba en su lugar:

```
pip install django mysqlclient
```

y si sigue fallando, revisa que tengas Visual C++ Build Tools instalado,
o usa `pip install pymysql` como alternativa (requiere dos líneas extra
en `stycheck/__init__.py`, pregúntame si necesitas ese cambio).

## 5. Migrar la base de datos

```
python manage.py makemigrations
python manage.py migrate
```

Esto crea la tabla `servicios` en la base de datos `stycheck`.

## 6. (Opcional) Crear un superusuario para el panel admin

```
python manage.py createsuperuser
```

## 7. Levantar el servidor

```
python manage.py runserver
```

Abre en el navegador:
- Catálogo de servicios: http://127.0.0.1:8000/servicios/
- Panel de administración: http://127.0.0.1:8000/admin/

## 8. Plan de pruebas sugerido (para el 10% de versionamiento/pruebas)

| # | Caso de prueba | Pasos | Resultado esperado |
|---|---|---|---|
| 1 | Crear servicio con datos válidos | Llenar formulario completo y guardar | El servicio se guarda y aparece en la lista |
| 2 | Crear servicio sin nombre | Dejar "Nombre" vacío y guardar | Muestra error, no guarda |
| 3 | Precio negativo o cero | Ingresar precio 0 o -5 | Muestra "El precio debe ser mayor a cero" |
| 4 | Duración cero | Ingresar duración 0 | Muestra "La duración debe ser mayor a cero minutos" |
| 5 | Editar servicio existente | Cambiar precio y categoría, guardar | Se actualiza y refleja el cambio en la lista |
| 6 | Eliminar servicio | Clic en "Eliminar", confirmar en el diálogo | El servicio desaparece de la lista |
| 7 | Filtrar por categoría | Seleccionar una categoría en el combo | Solo muestra servicios de esa categoría |
| 8 | Paginación | Crear más de 10 servicios | Aparecen los enlaces "Anterior/Siguiente" |

## 9. Versionamiento con Git

```
git init
git add .
git commit -m "Módulo Servicios: modelo, formularios, vistas y plantillas"
git branch -M main
git remote add origin https://github.com/<tu-usuario>/stycheck-django.git
git push -u origin main
```

Recuerda: **no subir la carpeta `.venv`** (ya está excluida en `.gitignore`).

## Estructura del proyecto

```
stycheck_django/
├── manage.py
├── requirements.txt
├── .gitignore
├── stycheck/            ← configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── servicios/           ← la app (el módulo de la evidencia)
    ├── models.py        ← modelo Servicio
    ├── forms.py         ← ServicioForm (validaciones)
    ├── views.py         ← listar / crear / editar / eliminar
    ├── urls.py          ← rutas del módulo
    ├── admin.py
    └── templates/servicios/
        ├── base.html
        ├── lista.html
        └── formulario.html
```
