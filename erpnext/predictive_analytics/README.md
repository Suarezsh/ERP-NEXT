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

## Uso

1. Ve a **Análisis Predictivo > Configuración de Predicciones** y activa las predicciones.
2. Crea una nueva **Ejecución de Predicción** y guarda.
3. Presiona el botón **Generar Predicciones**.
4. Revisa los resultados en **Predicciones por Producto** o en el reporte **Precisión de Predicciones**.

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
