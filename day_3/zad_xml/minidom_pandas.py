from xml.dom.minidom import Document


def create_xml_file(file_path):
    doc = Document()

    root = doc.createElement('data')
    doc.appendChild(root)

    people = [
        {'name': "John", 'age': '30', "city": "New York"},
        {'name': "Alice", 'age': '25', "city": "Los Angeles"},
        {'name': "Bob", 'age': '35', "city": "Chicago"},
    ]

    for person in people:
        person_element = doc.createElement('person')

        name_element = doc.createElement('name')
        name_element.appendChild(doc.createTextNode(person['name']))
        person_element.appendChild(name_element)

        age_element = doc.createElement('age')
        age_element.appendChild(doc.createTextNode(person['age']))
        person_element.appendChild(age_element)

        city_element = doc.createElement('city')
        city_element.appendChild(doc.createTextNode(person['city']))
        person_element.appendChild(city_element)

        root.appendChild(person_element)

        with open(file_path, 'w') as file:
            file.write(doc.toprettyxml(indent='   '))


create_xml_file('data.xml')
print("Plik XML został utworzony jako 'data.xml'")
