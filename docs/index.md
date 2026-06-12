# 🚀 ERP NEXT

Sistema ERP empresarial de código abierto implementado mediante **ERPNext** y **Frappe Framework**, diseñado para integrar y optimizar los procesos administrativos, financieros, comerciales y operativos de una organización.

---

## 📋 Tabla de Contenidos

* [Descripción del Proyecto](#-descripción-del-proyecto)
* [Objetivos](#-objetivos)
* [Integrantes y Roles](#-integrantes-y-roles)
* [Tecnologías Utilizadas](#-tecnologías-utilizadas)
* [Arquitectura del Sistema](#-arquitectura-del-sistema)
* [Funcionalidades](#-funcionalidades)
* [Módulos ERP](#-módulos-erp)
* [Metodología Scrum](#-metodología-scrum)
* [Estructura del Proyecto](#-estructura-del-proyecto)
* [Instalación](#-instalación)
* [Ejecución](#-ejecución)
* [Beneficios](#-beneficios)
* [Mejoras Futuras](#-mejoras-futuras)
* [Enlaces de Referencia](#-enlaces-de-referencia)

---

# 📖 Descripción del Proyecto

ERP NEXT es una solución de planificación de recursos empresariales (ERP) basada en software libre que permite gestionar de forma centralizada los procesos más importantes de una empresa.

El sistema integra módulos para la gestión de:

* Clientes
* Ventas
* Compras
* Inventarios
* Finanzas
* Recursos Humanos
* Proyectos
* Producción
* Reportes Gerenciales

Su objetivo principal es mejorar la eficiencia operativa, reducir errores manuales y proporcionar información en tiempo real para una mejor toma de decisiones.

---

# 🎯 Objetivos

## Objetivo General

Implementar una plataforma ERP basada en ERPNext para optimizar la gestión empresarial mediante la integración de procesos organizacionales.

## Objetivos Específicos

* Centralizar la información empresarial.
* Automatizar procesos administrativos.
* Optimizar la gestión de ventas y compras.
* Mejorar el control de inventarios.
* Facilitar la gestión financiera.
* Incrementar la productividad organizacional.
* Implementar metodologías ágiles para el desarrollo.

---

# 👥 Integrantes y Roles

| Integrante                         | Rol                |
| ---------------------------------- | ------------------ |
| Fernandez Lastarria, Valerio Piero | Scrum Master 1     |
| Suarez Huamani, Marco Antonio      | Scrum Master 2     |
| Condori Catunta, Joselin Sharon    | Backend Developer  |
| Rojas Condori, Fabiana Paola       | Frontend Developer |
| Velazque Quispe, Flor De Liz       | QA & Testing       |

---

# 🛠 Tecnologías Utilizadas

## Backend

* Python
* Frappe Framework v16
* ERPNext v16

## Frontend

* Vue.js
* JavaScript
* HTML5
* CSS3

## Base de Datos

* MariaDB

## DevOps

* Docker
* Docker Compose
* GitHub Actions

## Gestión Ágil

* Scrum
* GitHub Projects
* GitHub Issues

---

# 🏗 Arquitectura del Sistema

```text
Usuario
   │
   ▼
Frontend (Vue.js)
   │
   ▼
Frappe Framework
   │
   ▼
ERPNext
   │
   ▼
MariaDB
```

Características:

* Arquitectura modular.
* Alta escalabilidad.
* Fácil mantenimiento.
* Seguridad integrada.
* Integración con APIs externas.

---

# ⚙ Funcionalidades

## 📊 Gestión de Clientes (CRM)

* Registro de clientes.
* Historial comercial.
* Seguimiento de oportunidades.
* Gestión de contactos.

## 💰 Gestión de Ventas

* Cotizaciones.
* Órdenes de venta.
* Facturación.
* Reportes comerciales.

## 🛒 Gestión de Compras

* Solicitudes de compra.
* Órdenes de compra.
* Gestión de proveedores.
* Seguimiento de adquisiciones.

## 📦 Gestión de Inventario

* Control de stock.
* Movimientos de almacén.
* Transferencias.
* Alertas de inventario.

## 💳 Gestión Financiera

* Cuentas por cobrar.
* Cuentas por pagar.
* Flujo de caja.
* Estados financieros.

## 👨‍💼 Recursos Humanos

* Gestión de empleados.
* Control de asistencia.
* Vacaciones.
* Nóminas.

## 📈 Gestión de Proyectos

* Planificación.
* Asignación de tareas.
* Seguimiento de actividades.
* Control de avances.

---

# 📦 Módulos ERP

| Módulo        | Descripción            |
| ------------- | ---------------------- |
| CRM           | Gestión de clientes    |
| Sales         | Gestión de ventas      |
| Buying        | Gestión de compras     |
| Stock         | Gestión de inventario  |
| Accounts      | Gestión financiera     |
| HR            | Recursos humanos       |
| Projects      | Gestión de proyectos   |
| Manufacturing | Producción             |
| Reports       | Reportes empresariales |

---

# 🔄 Metodología Scrum

El proyecto fue desarrollado utilizando Scrum como marco de trabajo ágil.

## Roles Scrum

### Scrum Masters

* Coordinación del equipo.
* Seguimiento del Sprint.
* Eliminación de impedimentos.

### Equipo de Desarrollo

* Desarrollo Backend.
* Desarrollo Frontend.
* Testing y validación.

## Flujo de Trabajo

```text
Product Backlog
      │
      ▼
Sprint Planning
      │
      ▼
Sprint Backlog
      │
      ▼
Desarrollo
      │
      ▼
Testing
      │
      ▼
Sprint Review
      │
      ▼
Sprint Retrospective
```

---

# 📁 Estructura del Proyecto

```text
ERP-NEXT/
│
├── apps/
├── sites/
├── config/
├── docker/
├── scripts/
├── docs/
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

# 💻 Instalación

## Clonar repositorio

```bash
git clone https://github.com/Suarezsh/ERP-NEXT.git
```

## Ingresar al directorio

```bash
cd ERP-NEXT
```

## Levantar contenedores

```bash
docker compose up -d
```

---

# ▶ Ejecución

Acceder desde:

```text
http://localhost:8000
```

---

# 📈 Beneficios

* Centralización de información.
* Automatización de procesos.
* Reducción de errores manuales.
* Mayor productividad.
* Información en tiempo real.
* Mejor toma de decisiones.
* Escalabilidad empresarial.

---

# 🔮 Mejoras Futuras

* Integración con Inteligencia Artificial.
* Dashboards analíticos avanzados.
* Aplicación móvil.
* Firma digital.
* Integración con SUNAT.
* Reportes predictivos.
* Automatización de procesos mediante workflows.

---

# 📚 Enlaces de Referencia

## Repositorio

https://github.com/Suarezsh/ERP-NEXT

## GitHub Projects

https://github.com/Suarezsh/ERP-NEXT/projects

## ERPNext

https://frappe.io/erpnext

## Documentación Frappe

https://frappeframework.com/docs

---

# 📄 Licencia

Proyecto académico desarrollado utilizando tecnologías Open Source basadas en ERPNext y Frappe Framework.

**© 2026 - Equipo ERP NEXT**
