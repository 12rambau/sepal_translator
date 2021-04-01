from sepal_ui import sepalwidgets as sw 


class FolderTile(sw.Tile):
    
    def __init__(self):
        
        # create the widget 
        file_input = sw.FileInput(extentions=[''])
        txt = sw.Markdown("here I will add a lot of explanations")
        
        # create the actual tile
        super().__init__(
            'folder_tile',
            "Select folder",
            inputs = [txt, file_input],
            output = sw.Alert(),
            btn = sw.Btn("validate this folder")
        )