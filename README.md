# Instalación y Configuración de Odoo 18.0 (Localhost:8070)

Este documento explica el proceso de instalación de **Odoo 18.0** en entorno local.  
Se detalla el entorno usado, problemas encontrados, soluciones aplicadas y tiempo invertido.  

---

## Objetivo del ejercicio
- Configurar un entorno local de Odoo accesible desde el puerto 8070.  
- Documentar el proceso y mostrar un video de funcionamiento.  
- Explicar dificultades enfrentadas y cómo se resolvieron.  

---

## Entorno de trabajo

- **Sistema Operativo:** Windows 11 Pro (64 bits).  
- **Entorno de instalación:** Python `venv` (entorno virtual).  
- **Base de datos:** PostgreSQL 16 (instalada previamente en Windows).  
- **Lenguaje:** Python 3.11.  
- **Editor/IDE usado:** Visual Studio Code.  
- **Repositorio Odoo:** Clonado desde [https://github.com/odoo/odoo](https://github.com/odoo/odoo).  

---

## Pasos de instalación

### 1. Clonar repositorio oficial
```bash
git clone --branch 18.0 --single-branch --depth 1 https://github.com/odoo/odoo.git odoo
cd odoo
```

### 2. Crear entorno virtual
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

> Nota: En algunos casos ciertos paquetes no se instalaron correctamente en Windows. Se resolvió instalando `psycopg2-binary` manualmente:
```bash
python -m pip install --upgrade pip setuptools wheel
pip install psycopg2-binary
```

### 4. Configuración de PostgreSQL
- Crear usuario para Odoo:
```sql
CREATE USER odoo WITH PASSWORD '12345';
ALTER ROLE odoo CREATEDB;
```

### 5. Archivo de configuración `odoo.conf`
Se creó dentro del directorio `odoo/debian/odoo.conf` con el siguiente contenido:

```ini
[options]
; This is the password that allows database operations:
admin_passwd = 1234567890

; Config DB (Modificar)
db_host = localhost
db_port = 5432
db_user = odoo
db_password = 12345
db_name = odoo_db

; Path para los addons (Modificar)
addons_path = C:\Users\albar\Desktop\Project-Odoo\custom_addons,C:\Users\albar\Desktop\Project-Odoo\odoo\addons
default_productivity_apps = True

; Se especifica el puerto dodne correra
xmlrpc_port = 8070

; Se especifica donde se registrara el log  junto al nivel de registro de log (Modificar)
logfile = C:\Users\albar\Desktop\Project-Odoo\logs\odoo.log
log_level = info
```

### 6. Ejecutar Odoo en puerto 8070
```bash
python odoo/odoo-bin -c odoo.conf
```

Luego acceder a: [http://localhost:8070](http://localhost:8070)

---


## Problemas encontrados y soluciones

| Problema | Causa | Solución |
|----------|-------|----------|
| `requirements.txt` con errores al instalar | Dependencias no compatibles con Windows | Instalación manual de librerías problemáticas y cambio de version python 13 a python 11 |
|----------|-------|----------|
| Levantamiento del proyecto con docker | No hay visibilidad total del proyecto por trabajar con imagenes | Levantamiento del proyecto de manera completamente local |
|----------|-------|----------|
| Configuración de PostgreSQL | Usuario por defecto no existía | Crear usuario `odoo` con permisos de creación de BD |
|----------|-------|----------|
| Lentitud al clonar el repositorio | Se estaba clonando todo el proyecto con commits y versiones anteriores | Modificacion del comando git clone para clonar unicamnete la version 18 sin commits, ramas, etc, anteriores. (`git clone --branch 18.0 --single-branch --depth 1 https://github.com/odoo/odoo.git odoo`)|

---

## Tiempo invertido

- **Docker (intento inicial):** 2 horas (descartado para ver código base).  
- **Instalación con venv en Windows:** 3 horas.  
- **Configuración PostgreSQL + Odoo:** 1 hora.  
- **Resolución de errores y pruebas:** 2 horas.  
- **Grabación del video + documentación:** 1 hora.  
**Tiempo total: 9 horas.**

---

## Referencias utilizadas

- [Guía oficial de instalación Odoo (master)](https://www.odoo.com/documentation/master/administration/install.html)  
- [Documentación PostgreSQL](https://www.postgresql.org/docs/)  
- [Python Packaging User Guide](https://packaging.python.org/)  
- [Uso de inteligencia artificial](https://chatgpt.com/)(https://claude.ai/)
---

## Conclusiones

- La instalación en **Windows con venv** es viable, pero requiere resolver varios problemas de dependencias.  
- Para entornos de desarrollo colaborativos, **Docker es más rápido**, aunque menos flexible para explorar el código fuente.  
- Logré configurar Odoo 18.0 corriendo en el puerto **8070**, con acceso local y listo para desarrollo.  
- La experiencia ayudó a reforzar conocimientos en entornos virtuales, PostgreSQL y configuración de servicios en Odoo.  

---

## Notas adicionales (extra)

- Se recomienda para proyectos reales usar **Linux/WSL** o **Docker**, ya que la instalación en Windows puede ser más inestable.
- Implementar variables de entorno (en lugar de credenciales planas en odoo.conf) para mejorar la seguridad de la base de datos.
- Considerar el uso de pgAdmin o herramientas similares para gestionar PostgreSQL de forma más visual.
- Configurar backups automáticos de base de datos y módulos personalizados.
- Organizar los módulos desarrollados en un directorio separado (custom_addons) para mantener claro qué es core de Odoo y qué es código propio.
- Usar Git para versionar tanto la configuración como los módulos personalizados.
- En entornos de prueba/producción, activar y revisar regularmente los logs de PostgreSQL y del sistema operativo.
- Evaluar la integración con herramientas de monitoreo como htop, pg_stat_statements o Prometheus + Grafana, para detectar problemas de rendimiento.
- Documentar todas las dependencias adicionales instaladas en un archivo requirements_extra.txt, de modo que cualquier desarrollador pueda replicar el entorno.
---
