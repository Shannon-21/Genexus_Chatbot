# Universidad Nacional de Rosario

## Facultad de Ciencias Exactas, Ingeniería y Agrimensura

### TUIA - IA 4.2 - Procesamiento de Lenguaje Natural

### **Trabajo Práctico Integrador**

---

**Fechas**: 
- primera entrega: 18/12/2023
- segunda entrega: 20/02/2023

**Estudiante**:
 - Giampaoli Fabio

**Docentes**:
- Juan Pablo Manson
- Alan Geary
- Andrea Leon Cavallo
- Ariel D'Alessandro

**Acceso**: 
- *Colab*: [https://colab.research.google.com/drive/1lpm_vQsMMsVcRcXwM6rprbxXDDlaFszO#scrollTo=5Dq3FE-9IlTr](https://colab.research.google.com/drive/1lpm_vQsMMsVcRcXwM6rprbxXDDlaFszO#scrollTo=_cCagmvEfkJ-)
- *Documento*:[https://docs.google.com/document/d/1eknZhk3JdW7vd83pa7GRfzGugkBjukmEVaIyEwrM31s/edit?usp=sharing](https://docs.google.com/document/d/1eknZhk3JdW7vd83pa7GRfzGugkBjukmEVaIyEwrM31s/edit?usp=sharing)

  

---

## **Resumen**

Este proyecto consiste en la creación de un modelo de lenguaje como asistente para conversar con lenguaje natural sobre algún dominio de interés a alección, y la investigación de la posibilidad de convertirlo en un sistema multiagente que pueda conectar con diversas herramientas.

En este caso, mi interés es que el agente sea experto en Genexus. Genexus en un entorno de desarrollo de software que mediante un lenguaje de programación simiplificado e integraciones con otras herramientas, se puede generar código fuente para compilar y desplegar aplicaciones.

El objetivo es que el agente pueda tener a disposición la documentación oficial de Genexus para que pueda mantener una conversación al respecto como si Genexus fuera parte de su fuente de su conocimiento, para finalmente darle al usuario que interactua la sensación de que el agente puede ayudar a resolver dudas y problemas relacionados.

El modelo conversacional alimentara su contexto mediante diferentes fuentes de datos. Las tres fuentes principales que tomara serán:

- Wiki de Genexus: mediante extracción del texto de las páginas de la documentación oficial mediante técnicas de scrapping.
- Cursos de Genexus: Genexus posee videos que enseñan desde los conceptos más básicos hasta conceptos y metodológias avanzadas. Los video son acompañados por documentos pdf como transcripciones de los videos.
- WikiData: Es una base de conocimiento de grafos abierta de dominio general que dotará al modelo de conocimiento general de cualquier tópico en general.

Hacia el final de este proyecto, la arquitectura del modelo conversacional luce como en el siguiente esquema:

![image](https://github.com/Shannon-21/Genexus_Chatbot/assets/81629492/ca871139-878e-4196-831c-1a39f369bef9)

--- 

## **Uso**

Este proyecto esta desarrollado en un entorno de Google Colab como una notebook de código Python.

Para la ejecución del modelo se debe ejecutar de forma ordenada y secuencial aquellas secciones del cuaderno tituladas como "Acceso rápido" si el fin es solamente ejecutar el modelo conversacional.

**Importante**: Notar que el cuaderno entregado utiliza el token de HuggingFace para poder utilizar el modelo de lenguaje mediante API.
Debe ingresar este token personal en la variable correspondiente o en el gestor de claves secretas del entorno de Google Colab en la celda de codigo que lo requiere. (Desplegable 'Modelo de clasificación')


La ejecución de la ultima celda en el proyecto dara lugar inmediatamente debajo a un dialogo interactivo con el modelo experto en Genexus.

```python
start_genexus_model()
```

Ejemplo de conversación recortada entre un usuario y el modelo.

```
>>> [Usuario]: Es posible usar una formula find en la definicion de un data provider…

>>> [Modelo]: Sí, es posible utilizar una fórmula de búsqueda en la definición…

>>> [Usuario]: Si pongo esta formula de busqueda en un procedimiento…

>>> [Modelo]: No, la fórmula de búsqueda proporcionada recupera solo las líneas…

>>> [Usuario]: Esta bien que no retorne una coleccion de pedidos, ya que…

>>> [Modelo]: Sí, puede utilizar una fórmula de búsqueda en la definición de…
```

