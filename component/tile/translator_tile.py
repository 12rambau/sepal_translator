from pathlib import Path
from shutil import copyfile

from sepal_ui import sepalwidgets as sw 
from traitlets import Unicode


class TranslatorTile(sw.Tile):
    
    def __init__(self, user_folder):
        
        # gather the info 
        self.folder = Path(user_folder).expanduser()
        
        # set the available locales 
        self.locales = self._get_locales()
        
        # initialized the draft files (if needed)
        self._init_drafts()
        
        
        # create the actual tile
        super().__init__(
            'translator_tile',
            "Translate module",
            inputs = [],
            output = sw.Alert(),
            btn = sw.Btn("validate translation")
        )
        
    def _get_locales(self):
        """read the folder searching for json files and get the available languages of the app"""
        
        locales = [f.stem for f in self.folder.glob('*.json')]
        
        # check that at least english exist
        if not ('en' in locales):
            raise Exception("You don't have a dict for the source language (\"en\")")
        
        # check that there is at least one target 
        if len(locales) < 2:
            raise Exception("You don't have any target language")
            
        return locales
    
    def _init_drafts(self):
        """init the draft files if needed, we'll use the already existing one if they exist"""
        
        # we don't create drafts fo en.json as it is the reference
        locales = [l for l in self.locales if l != 'en']
        
        # create a draft file if needed
        for l in locales:
            valid = self.folder.joinpath(f'{l}.json')
            draft = valid.with_suffix(valid.suffix + '.draft')
            
            if not draft.is_file():
                copyfile(valid, draft)
         
        
        return self
        
        
            
        
        