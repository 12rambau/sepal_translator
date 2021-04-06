from pathlib import Path
import json

import ipyvuetify as v
from sepal_ui import sepalwidgets as sw

class KeyTree(sw.SepalWidget, v.Treeview):
    
    def __init__(self, folder, locales):
        
        # get the english file (source language)
        self.en_file = folder.joinpath('en.json')
        
        # check the file 
        if not self.en_file.is_file():
            raise Exception("no en file")
            
        # read the data 
        with self.en_file.open() as f: 
            en_data = json.loads(f.read())
        
        # create the tree items 
        items = self._get_items(en_data)
        
        # create the tree 
        super().__init__(
            items = items
        )
        
    def _get_items(self, v):

        list_ = []

        # create an enum object 
        if isinstance(v, dict):
            enum = v.items()
        elif isinstance(v, list):
            enum = enumerate(v)

        for k, v2 in enum:
            item = {'name': k}
            if isinstance(v2, dict) or isinstance(v2, list):
                item['children'] = self._get_items(v2)

            list_.append(item)

        return list_