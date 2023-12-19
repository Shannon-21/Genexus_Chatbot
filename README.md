# Universidad Nacional de Rosario

## Facultad de Ciencias Exactas, Ingeniería y Agrimensura

### TUIA - IA 4.2 - Procesamiento de Lenguaje Natural

### **Trabajo Práctico Integrador**

---

**Fecha**: 18/12/2023

**Estudiante**:
 - Giampaoli Fabio

**Docentes**:
- Juan Pablo Manson
- Alan Geary
- Andrea Leon Cavallo
- Ariel D'Alessandro

**Link a Google Colab**: 
- https://colab.research.google.com/drive/1lpm_vQsMMsVcRcXwM6rprbxXDDlaFszO#scrollTo=5Dq3FE-9IlTr

---

## **Introducción**

Este proyecto consiste en la creación de un modelo de lenguaje como asistente para conversar
con lenguaje natural sobre algún dominio de interés a elección, y la investigación de la
posibilidad de convertirlo en un sistema multiagente que pueda conectar con diversas
herramientas.

En este caso, mi interés es que el agente sea experto en Genexus. Genexus es un entorno de
desarrollo de software que mediante un lenguaje de programación simplificado e integraciones
con otras herramientas, se puede generar código fuente para compilar y desplegar
aplicaciones.

El objetivo es que el agente pueda tener a disposición la documentación oficial de Genexus
para que pueda mantener una conversación al respecto como si Genexus fuera parte de su
fuente de su conocimiento, para finalmente darle al usuario que interactúa la sensación de que
el agente puede ayudar a resolver dudas y problemas relacionados.

--- 

## **Uso**

Este proyecto esta desarrollado en un entorno de Google Colab como una notebook de código Python.

Para la ejecución del modelo se debe ejecutar de forma ordenada y secuencial todas y cada una de las celdas de codigo que definen funciones que el modelo utilizara.

**Importante**: Notar que el cuaderno entregado utiliza el token de HuggingFace para poder utilizar el modelo de lenguaje mediante API.
Debe ingresar este token personal en la variable correspondiente en la celda de codigo que lo requiere. (Desplegable 'Modelo de Lenguaje')

La celda final en el desplegable llamada 'Conversación' con este código:

```python
# inicializa el contexto y rol
global_context = []
rol = 'You are an Genexus expert programer that always responds using the provided context with brief responses and short pieces of code.'
first_question = True

# iteracion de la conversacion
while True:
    user_input = input("\u0001 [User]: ")
    user_input_en = GoogleTranslator(source='es', target='en').translate(user_input)

    print('\n')

    # keyword de escape
    if user_input.lower() == 'exit':
        print("Exiting the conversation.")
        break

    # obtiene respuesta de acuerdo de acuerdo a si usa o no contexto previo
    if first_question:
        model_answer = query_to_model(user_input, rol, memory=6)
        first_question = False
    else:
        model_answer = query_to_model(user_input, rol, context=model_answer, memory=6)

    # traducir al español la respuesta
    model_answer_es = translate_except_code(model_answer, 'en', 'es')

    print("\u0001 [Model]:", model_answer_es, '\n')
```

La ejecución de esta celda dara lugar inmediatamente debajo a un dialogo interactivo con el modelo experto en Genexus que permitira
al usuario ingresar consultas en español sobre Genexus.
