def classify(titles, classes, start_title, end_title, class_label):
    '''detecta el inicio y fin de los indices correspondientes a los titulos, y les asigna la categoria a ambos y sus intermedios'''
    start_index = None
    end_index = None

    # extrae el titulo de la url de cada registro
    for i, tag in enumerate(titles):
        soup = BeautifulSoup(tag.text, 'html.parser')
        title_text = soup.get_text(strip=True)

        # compara para determinar su indice
        if start_title == title_text:
            start_index = i
        elif end_title == title_text:
            end_index = i

    # asigna el valor de clase
    if start_index is not None and end_index is not None:
        for i in range(start_index, end_index + 1):
            classes[i] = class_label

# lista vacia para las clases
classes = [None for _ in range(len(menu))]

# selección manual de inicio y fin de las categorias
classify(menu, classes, 'What is a Knowledge Base', 'GeneXus IDE', 'General')
classify(menu, classes, 'Transaction object', 'File object', 'Modeling')
classify(menu, classes, 'Reorganization', 'Impact Database Tables', 'Building')
classify(menu, classes, 'Data View object', 'Payment services', 'Integration')
classify(menu, classes, 'Knowledge Manager', 'Application Security', 'Knowledge')

df_menu['Class'] = classes