import pandas as pd
from xml.dom import minidom


def read_xml_to_dataframe(file_path):
    doc = minidom.parse(file_path)

    persons = doc.getElementsByTagName('person')

    data = []

    for person in persons:
        name = person.getElementsByTagName('name')[0].firstChild.nodeValue
        age = person.getElementsByTagName('age')[0].firstChild.nodeValue
        city = person.getElementsByTagName('city')[0].firstChild.nodeValue

        data.append({"name": name, 'age': age, 'city': city})

    df = pd.DataFrame(data)

    return df


df = read_xml_to_dataframe('data.xml')
print(df)
#     name age         city
# 0   John  30     New York
# 1  Alice  25  Los Angeles
# 2    Bob  35      Chicago
