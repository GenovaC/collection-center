# Centro de Acopio

Sistema web para la gestión de inventario de donaciones en centros de acopio. Permite registrar, clasificar y administrar ítems donados, además de exportar reportes en Excel y PDF.

---

## 🛠️ Stack tecnológico

* Python 3
* Flask
* SQLAlchemy
* Flask-Migrate
* PostgreSQL
* HTML + Jinja2
* CSS personalizado
* JavaScript vanilla

---

## 📦 Instalación

### 1. Clonar repositorio

```bash id="c1cl01"
git clone https://github.com/GenovaC/collection-center.git
cd collection-center
```

---

### 2. Crear entorno virtual

```bash id="c1cl02"
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Instalar dependencias

```bash id="c1cl03"
pip install -r requirements.txt
```

---

### 4. Configurar variables de entorno

Crear archivo `.env`:

```env id="c1cl04"
SECRET_KEY=tu_clave_secreta

DATABASE_URL=postgresql://usuario:password@localhost:5432/centro_acopio
```

---

### 5. Inicializar base de datos

```bash id="c1cl05"
flask db init
flask db migrate -m "init"
flask db upgrade
```

---

### 6. Ejecutar proyecto

```bash id="c1cl06"
flask run
```

---

## 🐘 Configuración PostgreSQL

Asegúrate de tener PostgreSQL instalado y una base creada:

```sql id="c1cl07"
CREATE DATABASE collection_center;
```

Si usas usuario distinto al `postgres`, ajusta la URL en `.env`.

---

## 📊 Modelo de prioridad

Las prioridades se almacenan como strings en la base de datos:

| Valor  | Significado |
| ------ | ----------- |
| critic | Crítica     |
| high   | Alta        |
| mid    | Media       |
| low    | Baja        |

La interfaz traduce automáticamente estos valores y los muestra con colores.

---

## 📁 Estructura del proyecto

```text id="c1cl08"
app/
 ├── models/
 ├── routes/
 ├── templates/
 ├── static/
 ├── services/
 ├── __init__.py
migrations/
requirements.txt
run.py
```

---

## 🔄 Flujo de trabajo

```bash id="c1cl09"
git add .
git commit -m "Descripción del cambio"
git push
```

---

## 👥 Recomendaciones de colaboración

* Trabajar en ramas por feature
* Evitar commits directos a `main`
* Usar mensajes de commit claros
* Revisar cambios antes de merge

---

## 📌 Próximas mejoras

* Filtros avanzados por categoría y prioridad
* Paginación del inventario
* Dashboard con métricas
* Sistema de usuarios (roles)
* Historial de movimientos

---

## 📄 Licencia

Proyecto interno – Centro de Acopio - El Sistema - Música para todos
