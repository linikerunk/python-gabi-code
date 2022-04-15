"""
Aula 06 - Modulos

"""
import json


def convert_data(data:list) -> json:
    return json.dumps(data)

data = [{'nome': 'Gabriela'}, {'nome': 'Guilherme'}, {'nome': 'Julio'},]
import pdb; pdb.set_trace();

print(convert_data(data))
