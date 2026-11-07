
# Taller de Análisis de Datos - CESDE

**Estudiante:** Maria Fernanda Correa Agudelo

---

## Respuestas al Desafío Final (Preguntas de Negocio)

### 1. ¿Qué categoría genera más ingresos?
* **Resultado en terminal:** categoria

Tecnologia    14290000

Hogar          3653000

Papeleria       749000

Accesorios      484000
* **Respuesta:** La categoría que genera más ingresos es Tecnologia, acumulando un total de $14,290,000.
* **Criterio usado:** Se agrupó el DataFrame por la columna `"categoria"`, se sumó la columna `"total"` de las ventas y se ordenó de forma descendente con `.sort_values(ascending=False)`.

### 2. ¿Qué canal vende más?
* **Resultado en terminal:** canal                   

Online      35  14669000

Tienda      33   4507000


* **Respuesta:** El canal Online vende más, registrando 35 transacciones y un ingreso total de $14,669,000, superando al canal Tienda
* **Criterio usado:** Se agrupó por la columna `"canal"` aplicando `.agg()` para contar el número de transacciones (`id_venta`) y sumar los ingresos (`total`).

### 3. ¿Los clientes VIP compran más que los Regulares?
* **Resultado en terminal:** segmento_cliente                                  

Regular            308611.111111          1.083333

VIP                336083.333333          1.208333
* **Respuesta:** Sí, en promedio los clientes VIP compran más tanto en gasto promedio ($336,083.33) como en compras promedio por cliente (1.20), en comparación con los clientes Regulares
* **Criterio usado:** Se calculó el número de clientes únicos (nunique), las compras y el gasto total por segmento (segmento_cliente), dividiendo luego el total de compras y gasto entre la cantidad de clientes de cada categoría para obtener una comparación justa por persona.

### 4. ¿Qué método de pago es el más usado?
* **Resultado en terminal:** metodo_pago

Efectivo         30

Tarjeta          25

Transferencia    13

Name: count, dtype: int64
* **Respuesta:** El método de pago más usado es el Efectivo
* **Criterio usado:** Se aplicó el método .value_counts() sobre la columna "metodo_pago" para contar la frecuencia de cada modalidad de pago.

### 5. ¿Cuáles son los cinco clientes con más compras?

* **Respuesta:**Los 5 clientes con más compras son:

id_cliente nombre_cliente                        

21         Nicolas Cardona         2      2515000

35         Matias Rodriguez        2      1278000

52         Mia Quintero            2      1090000

58         Luna Montoya            2      1007000

3          Luis Perez              2       730000 

* **Criterio usado:** Se agrupó por "id_cliente" y "nombre_cliente", contando la cantidad de compras y sumando el gasto total, ordenando de mayor a menor por compras y gasto, y tomando los primeros 5 registros con .head(5).