from sepal_ui import sepalwidgets as sw 

class TranslatorTile(sw.Tile):
    
    def __init__(self):
        
        # create the actual tile
        super().__init__(
            'translator_tile',
            "Translate module",
            inputs = [],
            output = sw.Alert(),
            btn = sw.Btn("validate translation")
        )