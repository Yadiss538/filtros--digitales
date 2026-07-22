# Implementación y Evaluación de Filtros Digitales

## Descripción del Proyecto
Este proyecto tiene como objetivo el diseño, implementación y evaluación de filtros digitales (en este caso, un filtro pasa bajas de tipo Butterworth) utilizando **Python**. La práctica permite analizar el comportamiento de las señales antes y después de aplicar el filtrado, evaluando su efectividad frente a señales con ruido.

## Conceptos Clave
* **Diseño de filtros digitales:** Uso de técnicas matemáticas para permitir o bloquear rangos específicos de frecuencias (pasa bajas, pasa altas, pasa bandas).
* **Respuesta en frecuencia:** Análisis de la ganancia y atenuación del filtro en función de la frecuencia.
* **Procesamiento de señales con ruido:** Filtrado de ruido blanco y separación de componentes frecuenciales no deseados.

---

## Estructura del Código

El script de Python está dividido en las siguientes secciones principales:

1. **Definición de la señal de entrada:**
   * Se genera una señal compuesta por la suma de dos ondas senoidales de diferentes frecuencias (5 Hz y 50 Hz).
   * Se le añade ruido blanco gaussiano para simular una señal real distorsionada.

2. **Diseño del filtro:**
   * Se implementa un filtro digital **Butterworth** de orden 4 mediante la librería `scipy.signal`.
   * Se define una frecuencia de corte específica para aislar las frecuencias de interés.

3. **Aplicación del filtro a la señal:**
   * Se procesa la señal ruidosa a través de la función de transferencia del filtro diseñado utilizando `lfilter`.

4. **Visualización de los resultados:**
   * Se generan gráficas comparativas en el dominio del tiempo (señal original, señal con ruido y señal filtrada).
   * Se grafica la respuesta en frecuencia del filtro para comprobar su comportamiento teórico.

---

## Requisitos y Dependencias
Para ejecutar este código, asegúrate de tener instaladas las siguientes librerías de Python:
```bash
pip install numpy scipy matplotlib# filtros--digitales
