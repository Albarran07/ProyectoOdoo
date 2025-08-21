# README – Tutorial Crear Módulos en Odoo

## 1. Resumen del proyecto

Este repositorio contiene un módulo de ejemplo para **Odoo 18** llamado `Tutorial_Crear_Modulos`.
El objetivo principal es demostrar el entendimiento del **Odoo Server Framework**, la creación de módulos desde cero y la aplicación de buenas prácticas en el desarrollo de módulos.

El módulo permite:

- Crear, listar y editar elementos de tipo `tutorial.modulo`.
- Visualizar los datos en **vista lista** y **formulario**.
- Manejar seguridad básica con permisos de lectura, escritura, creación y eliminación.

El módulo se desarrolló siguiendo un **proceso incremental**:

1. Módulo sin dependencias.
2. Módulo con control de accesos (`ir.model.access.csv`).
3. Uso de vistas XML adaptadas a la versión 18 de Odoo.
4. Menús y acciones para acceder a los registros desde la interfaz de usuario.

---

## 2. Estructura del módulo

```
Tutorial_Crear_Modulos/
│
├─ __init__.py
├─ __manifest__.py
├─ models/
│   ├─ __init__.py
│   └─ tutorial_modelo.py
├─ views/
│   └─ tutorial_modelo_views.xml
├─ security/
│   └─ ir.model.access.csv
└─ __pycache__/
```

- `__manifest__.py` → Define el módulo y sus metadatos.
- `models/tutorial_modelo.py` → Contiene la definición del modelo `tutorial.modulo`.
- `views/tutorial_modelo_views.xml` → Vistas del módulo (lista y formulario), acciones y menús.
- `security/ir.model.access.csv` → Permisos de acceso al modelo para usuarios.

---

## 3. Instalación y prueba del módulo

### Requisitos

- Odoo 18 instalado y funcionando.
- Python 3.11.
- PostgreSQL configurado con una base de datos disponible.
- Modificar el `odoo.conf` con los datos correspondientes a su local (addons_path, configuracion de la BD, etc.)

### Pasos para probar

1. Copiar la carpeta `Tutorial_Crear_Modulos` dentro del directorio de `custom_addons` de tu instancia de Odoo.
2. Asegurarse de incluir `custom_addons` en el `addons_path` del archivo de configuración (`odoo.conf`):

```ini
addons_path = C:\Users\albar\Desktop\Project-Odoo\custom_addons
```

3. Reiniciar el servidor de Odoo:

```bash
python odoo-bin -c odoo.conf
```

4. Actualizar la lista de módulos desde **Apps → Actualizar lista de módulos** (Esto se puede hacer desde consola o desde la intefaz con le modo desarrollador activado).
5. Buscar `Tutorial Módulo` e instalarlo.
6. Acceder al menú:

```
Tutorial Módulo → Items
```

7. Crear, editar y eliminar registros para verificar que las vistas y permisos funcionan correctamente.

---

## 4. Qué se completó

- Módulo funcional `Tutorial_Crear_Modulos` sin dependencias externas.
- Modelo `tutorial.modulo` con campos:
  - `name` (Char)
  - `descripcion` (Text)
- Vistas:
  - Lista (`list`)
  - Formulario (`form`)
- Menús y acciones para interactuar con el modelo.
- Control de acceso básico usando `ir.model.access.csv`.
- Ajuste de sintaxis XML para Odoo 18.
- Documentación del proceso paso a paso.

---

## 5. Aprendizajes principales

1. Diferencias entre versiones de Odoo y cómo afectan la sintaxis XML.
2. Cómo crear modelos, vistas y menús desde cero.
3. Uso de `ir.model.access.csv` para controlar permisos de acceso a modelos.
4. Visualizacion de errores comunes durante la instalación de módulos desde docuemnto log o desde la intefaz con el modo desarrollador activado .
5. Organización de directorios y buenas prácticas en desarrollo de módulos.

---

## 6. Problemas encontrados y soluciones

| Problema | Causa | Solución |
|----------|-------|---------|
| Error `Wrong value for ir.ui.view.type: 'tree'` | Sintaxis XML de Odoo 17 no compatible con Odoo 18 | Cambiar `<tree>` a `<list>` y `<field name="type">list</field>` |
| Módulo no visible en menú | No se definió `security` ni permisos | Crear carpeta `security` con `ir.model.access.csv` y asignar permisos a `base.group_user` |
| Instalación parcial o fallida | Módulo instalado parcialmente | Desinstalar desde Apps o eliminar el registro en `ir_module_module` en modo debug |
| Registro duplicado de menú o vista | Actualizaciones previas de XML sin limpiar | Reiniciar servidor y actualizar lista de módulos |

---

## 7. Qué haría diferente con más tiempo

- Implementar más **campos de prueba** en el modelo para mostrar relaciones (`Many2one`, `One2many`).
- Crear **vistas Kanban y calendario** para enriquecer la interfaz.
- Añadir **reportes PDF** usando `QWeb` y `wkhtmltopdf`.
- Crear **pruebas automatizadas** para el módulo usando Odoo `unittest`.
- Mejorar documentación interna en Python y XML con comentarios explicativos.

---

## 8. Buenas prácticas aplicadas

- Modularización: separar `models`, `views` y `security`.
- Uso de convenciones de nombres claras para modelos y vistas.
- Uso correcto de IDs y referencias entre XML y acciones.
- Manejo de errores y limpieza de registros en la base de datos.
- README detallado para explicar el proceso de desarrollo.

---

## 9. Recursos de referencia

- [Documentación oficial de Odoo 18](https://www.odoo.com/documentation/18.0/)
- [Odoo Server Framework 101](https://www.odoo.com/documentation/18.0/developer/framework.html)
- [Uso de inteligencia artificial](https://chatgpt.com/)(https://claude.ai/)

---

