import json
import re

from Instance import Instance
from Snapshot import Snapshot
from Volume import Volume


def parse_obj_data(obj_type, data_str):
    """
     parse provided data strings and return as a list of Obj
    """
    obj_list = []
    obj_class_type = assign_class_type(obj_type)
    json_obj_list = parse_to_json(data_str)

    for item in json_obj_list:
        record = json.loads(item)
        obj = obj_class_type(**record)
        obj_list.append(obj)
    return obj_list

 
def parse_to_json(data_str):
    """
     Convert string to a valid json object
    """
    json_obj_list = []
    obj = data_str.split('%')
    for record in obj:
        attributes = re.split(',', record)

        data = json.dumps(attributes)
        data = re.sub(r':', '":"', data)
        data = re.sub(r'\[', '{', data)
        data = re.sub(r']', '}', data)
        json_obj_list.append(data)

    return json_obj_list


def assign_class_type(obj_type):
    """
     assign appropriate class type to provided obj_type
    """
    if obj_type == 'instance':
        return Instance
    elif obj_type == 'snapshot':
        return Snapshot
    elif obj_type == 'volume':
        return Volume
    else:
        raise NameError("obj_type not found")


def obj_lookup(obj_list, property_dict):
    """
     finds subset of obj_list by filtering the list according to provided property_dict
    """

    def filer_obj_by_prop(obj, prop_dict):
        for prop in prop_dict:
            if getattr(obj, prop) != prop_dict[prop]:
                return False
        return True

    filtered_objects_list = filter(lambda obj_list: filer_obj_by_prop(obj_list, property_dict), obj_list)
    return filtered_objects_list
