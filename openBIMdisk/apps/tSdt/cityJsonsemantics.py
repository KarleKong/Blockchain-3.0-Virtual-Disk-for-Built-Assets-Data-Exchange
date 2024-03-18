import hashlib
import json


class cityJsonSemantics:
  def __init__(self):
    self.data = {}
    self.dict = {}
    self.dict_hash = {}
    self.dict_rev = {}
    self.dict_hash_rev = {}
    self.dict_obj = {}
    self.dict_obj_trim = {}
    self.dict_cnt = {}
    self.dict_hash_cnt = {}
    self.tmp_GUID_obj = {}
    self.tmp_GUID_obj_trim = {}
    self.type_cnt = {}
    self.hashed_type_cnt = {}
    # self.conf_unordered_list = {'hasProperties', 'cfsFaces'}
    # self.comp_use_name = {'IfcDistributionPort', 'IfcRelConnectsPortToElement'}
    # self.hash_final_types = {'IfcShapeRepresentation', 'IfcRelDefinesByProperties', 'IfcRelAssociatesMaterial'}
    # self.ignore_parent_ref = {'contextOfItems': None, 'parentContext': None, 'ofProductRepresentation': None, 'propertyDefinitionOf': None, 'relatedOpeningElement': None, 'isDefinedBy': None, 'hasAssociations': None, 'hasFillings': None}
    self.ignore_update_date = {'LASTUPDATEDATE': None}
  
  def put(self, key, val):
    self.dict[key] = val
  
  def get(self, key):
    return self.dict[key]

  def getObj(self):
    return self.data

  def getDictObj(self):
    return self.dict_obj
  
  def remove(self, key):
    self.dict.pop(key, None)
  
  def contains(self, key):
    return key in self.dict
  
  def loadjson(self, fname):
    with open(fname) as json_file:
      self.data = json.load(json_file)
      self.sortdata()

  def adddict(self, id, obj):
    if id in self.dict_cnt:
      self.dict_cnt[id] += 1
      self.dict_obj[id].append(obj)
      id += '#' + str(self.dict_cnt[id])
    else:
      self.dict_cnt[id] = 1
      self.dict_obj[id] = [obj]

  
  def sortdata(self):
    to_pop = []
    self.data['features_item'] = {}
    for i in range(len(self.data['features'])):
      if 'GRAPHICID' in self.data['features'][i]['properties']:
        key = self.data['features'][i]['properties']['GRAPHICDATASET'] + "-" + str(self.data['features'][i]['properties']['GRAPHICID'])
        if key in self.data['features_item']:
          self.data['features_item'][key].append(self.data['features'][i])
        else:
          self.data['features_item'][key] = [self.data['features'][i]]
        to_pop.insert(0, i)
    for i in to_pop:
      self.data['features'].pop(i)
    if len(self.data['features']) == 0:
      self.data.pop('features', None)

  def load(self, obj):
    # print(type(obj), obj)
    if isinstance(obj, list):
      for i in range(len(obj)):
        if isinstance(obj[i], dict) or isinstance(obj[i], list):
          self.load(obj[i])
        if isinstance(obj[i], float):
          obj[i] = round(obj[i], 10)
    elif isinstance(obj, dict):
      id = list(obj.keys())[0]
      for e in self.ignore_update_date:
        if e in obj:
          self.ignore_update_date[e] = obj[e]
          obj[e] = None
      self.adddict(id, obj)
      for k in obj:
        v = obj[k]
        if isinstance(v, dict) or isinstance(v, list):
          self.load(v)
        if isinstance(v, float):
          obj[k] = round(v, 10)