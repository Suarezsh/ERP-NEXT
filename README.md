
<div align="center">
    <a href="https://frappe.io/erpnext">
	<img src="./erpnext/public/images/v16/erpnext.svg" alt="ERPNext Logo" height="80px" width="80xp"/>
    </a>
    <h2>ERPNext</h2>
    <p align="center">
        <p>Powerful, Intuitive and Open-Source ERP</p>
    </p>

[![Learn on Frappe School](https://img.shields.io/badge/Frappe%20School-Learn%20ERPNext-blue?style=flat-square)](https://frappe.school)<br><br>
[![CI](https://github.com/frappe/erpnext/actions/workflows/server-tests-mariadb.yml/badge.svg?event=schedule)](https://github.com/frappe/erpnext/actions/workflows/server-tests-mariadb.yml)
[![docker pulls](https://img.shields.io/docker/pulls/frappe/erpnext-worker.svg)](https://hub.docker.com/r/frappe/erpnext-worker)

</div>

<div align="center">
	<img src="./erpnext/public/images/v16/hero_image.png"/>
</div>

<div align="center">
	<a href="https://erpnext-demo.frappe.cloud/api/method/erpnext_demo.erpnext_demo.auth.login_demo">Live Demo</a>
	-
	<a href="https://frappe.io/erpnext">Website</a>
	-
	<a href="https://docs.frappe.io/erpnext/">Documentation</a>
</div>

## ERPNext

Sistema ERP 100% de código abierto para ayudarte a dirigir tu negocio.

### Motivación

Dirigir un negocio es una tarea compleja: gestionar facturas, realizar el seguimiento del stock, administrar el personal e incluso realizar más actividades ad-hoc. En un mercado donde el software se vende por separado para gestionar cada una de estas tareas, ERPNext hace todo lo anterior y más, de forma gratuita.

### Características Clave

- **Contabilidad**: Todas las herramientas que necesitas para gestionar el flujo de caja en un solo lugar, desde el registro de transacciones hasta el resumen y análisis de informes financieros.
- **Gestión de Pedidos**: Realiza el seguimiento de los niveles de inventario, repón stock y gestiona pedidos de ventas, clientes, proveedores, envíos, entregas y cumplimiento de pedidos.
- **Fabricación**: Simplifica el ciclo de producción, ayuda a realizar el seguimiento del consumo de materiales, muestra la planificación de la capacidad, gestiona la subcontratación ¡y más!
- **Gestión de Activos**: Desde la compra hasta el deterioro, desde la infraestructura de TI hasta el equipamiento. Cubre cada rama de tu organización, todo en un sistema centralizado.
- **Proyectos**: Entrega proyectos tanto internos como externos a tiempo, dentro del presupuesto y con rentabilidad. Realiza el seguimiento de tareas, hojas de horas y problemas por proyecto.

<details open>

<summary>More</summary>
	<img src="https://erpnext.com/files/v16_bom.png"/>
	<img src="https://erpnext.com/files/v16_stock_summary.png"/>
	<img src="https://erpnext.com/files/v16_job_card.png"/>
	<img src="https://erpnext.com/files/v16_tasks.png"/>
</details>

### Under the Hood (Bajo el capó)

- [**Frappe Framework**](https://github.com/frappe/frappe): Un framework de aplicaciones web full-stack escrito en Python y Javascript. El framework proporciona una base sólida para construir aplicaciones web, incluyendo una capa de abstracción de base de datos, autenticación de usuarios y una API REST.

- [**Frappe UI**](https://github.com/frappe/frappe-ui): Una biblioteca de IU basada en Vue, para proporcionar una interfaz de usuario moderna. La biblioteca Frappe UI ofrece una variedad de componentes que se pueden utilizar para construir aplicaciones de una sola página (SPA) sobre el Frappe Framework.

## Production Setup (Configuración de producción)

### Managed Hosting (Alojamiento gestionado)

Puedes probar [Frappe Cloud](https://frappecloud.com), una plataforma de [código abierto](https://github.com/frappe/press) simple, intuitiva y sofisticada para alojar aplicaciones Frappe con total tranquilidad.

Se encarga de la instalación, configuración, actualizaciones, monitoreo, mantenimiento y soporte de tus despliegues de Frappe. Es una plataforma de desarrollo con todas las funciones que permite gestionar y controlar múltiples despliegues de Frappe.

<div>
	<a href="https://erpnext-demo.frappe.cloud/app/home" target="_blank">
		<picture>
			<source media="(prefers-color-scheme: dark)" srcset="https://frappe.io/files/try-on-fc-white.png">
			<img src="https://frappe.io/files/try-on-fc-black.png" alt="Try on Frappe Cloud" height="28" />
		</picture>
	</a>
</div>



### Self-Hosted (Autoalojado)
#### Docker

Requisitos previos: docker, docker-compose, git. Consulta la [Documentación de Docker](https://docs.docker.com) para obtener más detalles sobre la configuración de Docker.

Ejecuta los siguientes comandos:

```
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
docker compose -f pwd.yml up -d
```

Después de un par de minutos, el sitio debería estar accesible en el puerto de tu localhost: 8080. Utiliza las siguientes credenciales de inicio de sesión predeterminadas para acceder al sitio.
- Usuario: Administrator
- Contraseña: admin

Consulta [Frappe Docker](https://github.com/frappe/frappe_docker?tab=readme-ov-file#to-run-on-arm64-architecture-follow-this-instructions) para la configuración de Docker basada en ARM.


## Development Setup (Configuración de desarrollo)
### Manual Install (Instalación manual)

La forma fácil: nuestro script de instalación para bench instalará todas las dependencias (por ejemplo, MariaDB). Consulta https://github.com/frappe/bench para más detalles.

Se crearán nuevas contraseñas para el usuario "Administrator" de ERPNext, el usuario root de MariaDB y el usuario frappe (el script muestra las contraseñas y las guarda en ~/frappe_passwords.txt).


### Local

Para configurar el repositorio localmente, sigue los pasos que se mencionan a continuación:

1. Configura bench siguiendo los [Pasos de instalación](https://frappeframework.com/docs/user/en/installation) e inicia el servidor
   ```
   bench start
   ```

2. En una ventana de terminal separada, ejecuta los siguientes comandos:
   ```
   # Create a new site
   bench new-site erpnext.localhost
   ```

3. Obtén la aplicación ERPNext e instálala
   ```
   # Get the ERPNext app
   bench get-app https://github.com/frappe/erpnext

   # Install the app
   bench --site erpnext.localhost install-app erpnext
   ```

4. Abre la URL `http://erpnext.localhost:8000/app` en tu navegador, deberías ver la aplicación ejecutándose.

## Learning and community (Aprendizaje y comunidad)

1. [Frappe School](https://school.frappe.io) - Aprende Frappe Framework y ERPNext con los diversos cursos de los mantenedores o de la comunidad.
2. [Official documentation](https://docs.erpnext.com/) - Documentación extensa para ERPNext.
3. [Discussion Forum](https://discuss.frappe.io/c/erpnext/6) - Participa con la comunidad de usuarios y proveedores de servicios de ERPNext.
4. [Telegram Group](https://erpnext_public.t.me) - Obtén ayuda instantánea de una enorme comunidad de usuarios.


## Contributing (Contribuir)

1. [Issue Guidelines](https://github.com/frappe/erpnext/wiki/Issue-Guidelines) (Directrices para reportar problemas)
1. [Report Security Vulnerabilities](https://erpnext.com/security) (Reportar vulnerabilidades de seguridad)
1. [Pull Request Requirements](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines) (Requisitos para Pull Requests)
2. [Translations](https://crowdin.com/project/frappe) (Traducciones)


## Logo and Trademark Policy (Política de marcas registradas y logotipos)

Por favor, lee nuestra [Política de marcas registradas y logotipos](TRADEMARK_POLICY.md).

# Ejecutar ERPNext con Docker (Windows)

```bash
# 1. Clonar el repositorio
git clone https://github.com/frappe/frappe_docker.git
cd frappe_docker

# 2. Iniciar los contenedores
docker compose -f pwd.yml up -d

# 3. Verificar que estén en ejecución
docker ps
```

Abrir en el navegador:

```
http://localhost:8080
```

Si Docker no está iniciado, abrir **Docker Desktop** antes de ejecutar los comandos.

<br />
<br />
<div align="center" style="padding-top: 0.75rem;">
	<a href="https://frappe.io" target="_blank">
		<picture>
			<source media="(prefers-color-scheme: dark)" srcset="https://frappe.io/files/Frappe-white.png">
			<img src="https://frappe.io/files/Frappe-black.png" alt="Frappe Technologies" height="28"/>
		</picture>
	</a>
</div>
