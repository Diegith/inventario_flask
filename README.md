# 📦 Sistema de Inventario con Flask

Este proyecto es una aplicación web desarrollada con **Flask** que permite la gestión integral de productos, proveedores y usuarios. Está orientado a pequeñas empresas o almacenes que requieren llevar control de su inventario, emitir alertas por faltantes y administrar perfiles de usuario con distintos roles.

## 🌟 Funcionalidades principales

- **Inicio de sesión seguro** con sesiones y contraseña cifrada
- **Gestión de productos** con cantidad mínima, stock disponible e imágenes
- **Alertas automáticas** por productos bajo inventario o cerca del umbral mínimo
- **Módulo de usuarios** con roles, creación, edición, búsqueda y activación/desactivación
- **Gestión de proveedores** vinculados a productos, con imágenes y CRUD completo
- **Carga de imágenes** para productos y proveedores
- **Filtros dinámicos y búsqueda por atributos**

## 🧰 Tecnologías utilizadas

- Python 3 + Flask
- SQLite (o DB compatible)
- HTML + Jinja2
- Bootstrap (front-end)
- `werkzeug`, `wtforms`, `sensors_plus` (seguridad, formularios, sesiones)
- Subida de imágenes con `secure_filename` y carpeta `/static/uploads`

## 📁 Estructura del proyecto

- `app.py`: Lógica principal, rutas Flask y controladores
- `formularios.py`: Definición de formularios con WTForms
- `db.py`: Funciones auxiliares de consulta e inserción a la base de datos
- `/templates`: Vistas HTML divididas por módulos (`usuarios`, `productos`, `proveedores`)
- `/static`: Archivos de estilos e imágenes subidas
- `img/uploads`: Carpeta donde se almacenan logos e imágenes de productos

## 🚀 ¿Cómo ejecutarlo?

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Diegith/inventario_flask.git
   cd inventario_flask

2. Asegúrate de tener las dependencias instaladas:
```bash
pip install flask werkzeug wtforms

```
3. Ejecuta la aplicación:
```bash
python app.py
Abre tu navegador en http://localhost:8080
```
🔐 Roles de usuario
Admin: acceso total a todos los módulos
Operador o usuario estándar: acceso limitado según implementación

🧪 Notas adicionales
El hash de la contraseña se genera con werkzeug.security
La lógica de alerta en el dashboard verifica si hay productos por debajo del stock mínimo y los resalta

El sistema se puede adaptar fácilmente a MySQL, PostgreSQL u otra base de datos relacional.

📄 Licencia
MIT License – disponible para fines educativos o personales.
