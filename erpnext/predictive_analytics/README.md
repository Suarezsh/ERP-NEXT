# Módulo de Análisis Predictivo

Este módulo agrega funcionalidades de inteligencia artificial a ERPNext para pronosticar ventas, detectar posibles quiebres de stock y sugerir compras.

## Funcionalidades

- **Pronóstico de ventas** por producto usando Random Forest o regresión lineal.
- **Detección de quiebre de stock** estimando la fecha de agotamiento.
- **Sugerencia de compra** basada en la demanda pronosticada más stock de seguridad.
- **Ejecución automática** diaria mediante el programador de Frappe.
- **Reporte de precisión** para comparar predicciones contra ventas reales.

## DocTypes incluidos

| DocType | Descripción |
|---------|-------------|
| `Prediction Settings` | Configuración general del módulo. |
| `Prediction Run` | Registro de cada ejecución del modelo. |
| `Product Prediction` | Predicción individual por producto y fecha. |

## Modelos disponibles

- **Random Forest** (recomendado): captura patrones no lineales y estacionalidad.
- **Linear Regression**: modelo simple para comparaciones o datos limitados.

## Ejemplo de uso

### 1. Crear historial de ventas

El modelo necesita datos históricos. Crea facturas de venta anteriores para los productos que quieres predecir.

Ejemplo para el producto **Laptop**:

| Fecha | Producto | Cantidad |
|-------|----------|----------|
| 01/05/2026 | Laptop | 5 |
| 15/05/2026 | Laptop | 3 |
| 01/06/2026 | Laptop | 7 |
| 15/06/2026 | Laptop | 4 |

### 2. Configurar predicciones

Ve a **Predictive Analytics > Configuración de Predicciones**:

- **Activar predicciones**: Sí
- **Modelo de predicción**: Random Forest
- **Días de predicción predeterminados**: 30
- **Días mínimos de historial**: 14 (para pruebas)
- **Días de stock de seguridad**: 7

Guarda.

### 3. Ejecutar predicción

Ve a **Predictive Analytics > Ejecutar Predicción**:

1. Crea un nuevo registro.
2. Define el período de predicción.
3. Guarda.
4. Presiona **Generar Predicciones**.

### 4. Revisar resultados

Ve a **Predictive Analytics > Predicciones por Producto**.

Verás resultados como:

| Producto | Cantidad Predicha | Stock Actual | Fecha Agotamiento | Compra Sugerida |
|----------|-------------------|--------------|-------------------|-----------------|
| Laptop | 45 | 10 | 25/07/2026 | 42 |

### 5. Ver precisión

Ve a **Predictive Analytics > Precisión de Predicciones** para comparar predicciones contra ventas reales.

## Despliegue en Docker

Si usas `frappe_docker`, después de clonar el código debes:

```bash
# Copiar el módulo al contenedor
docker cp ./ERP-NEXT/erpnext/predictive_analytics frappe_docker-backend-1:/home/frappe/frappe-bench/apps/erpnext/erpnext/
docker cp ./ERP-NEXT/erpnext/modules.txt frappe_docker-backend-1:/home/frappe/frappe-bench/apps/erpnext/erpnext/modules.txt
docker cp ./ERP-NEXT/erpnext/hooks.py frappe_docker-backend-1:/home/frappe/frappe-bench/apps/erpnext/erpnext/hooks.py
docker cp ./ERP-NEXT/pyproject.toml frappe_docker-backend-1:/home/frappe/frappe-bench/apps/erpnext/pyproject.toml

# Instalar dependencias
docker exec frappe_docker-backend-1 bash -c "cd /home/frappe/frappe-bench && bench pip install scikit-learn pandas numpy"

# Ejecutar migrate
docker exec frappe_docker-backend-1 bash -c "cd /home/frappe/frappe-bench && bench --site frontend migrate"

# Reiniciar frontend
docker restart frappe_docker-frontend-1
```

> Nota: en ERPNext v16 también es necesario crear un `Desktop Icon` para que el módulo aparezca en el menú lateral.

## Dependencias

Las siguientes librerías se instalan automáticamente con el proyecto:

- `scikit-learn`
- `pandas`
- `numpy`

Si usas un entorno manual, instálalas con:

```bash
bench pip install scikit-learn pandas numpy
```

## Notas técnicas

- El módulo lee el historial de ventas desde `Sales Invoice` y `Sales Invoice Item`.
- Requiere al menos los días de historial configurados en `Prediction Settings`.
- Las predicciones se guardan en el DocType `Product Prediction` para su análisis posterior.
- La ejecución automática diaria se configura en `erpnext/hooks.py`.
