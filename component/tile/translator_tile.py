from pathlib import Path

from sepal_ui import sepalwidgets as sw 
from traitlets import Unicode


class TranslatorTile(sw.Tile):
    
    folder = Unicode('').tag(sync=True)
    
    def __init__(self, user_folder):
        
        # gather the info 
        self.folder = user_folder
        
        # set the available locales 
        self.locales = self._get_locales()
        
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
        
        message_dir = Path(self.folder)
        
        locales = [f.stem for f in message_dir.glob('*.json')]
        
        # check that at least english exist
        if not ('en' in locales):
            raise Exception("You don't have a dict for the source language (\"en\")")
        
        # check that there is at least one target 
        if len(locales) < 2:
            raise Exception("You don't have any target language")
            
        return locales
            
        
        