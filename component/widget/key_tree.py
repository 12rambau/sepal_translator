import ipyvuetify as v
from sepal_ui import sepalwidgets as sw

class KeyTree(sw.SepalWidget, v.Treeview):
    
    def __init__(self, folder, locales):
        
        # create the tree items 
        items = [
            {
                'name': 'Applications :',
                'children': [
                    { 'name': 'Calendar : app' },
                    { 'name': 'Chrome : app' },
                    { 'name': 'Webstorm : app' },
                ],
            },
            {
                'name': 'Documents :',
                'children': [
                    {
                        'name': 'vuetify :',
                        'children': [
                            {
                                'name': 'src :',
                                'children': [
                                    { 'name': 'index : ts' },
                                    { 'name': 'bootstrap : ts' },
                                ],
                            },
                        ],
                    },
                    {
                        'name': 'material2 :',
                        'children': [
                            {
                                'name': 'src :',
                                'children': [
                                    { 'name': 'v-btn : ts' },
                                    { 'name': 'v-card : ts' },
                                    { 'name': 'v-window : ts' },
                                ],
                            },
                        ],
                    },
                ],
            },
            {
                'name': 'Downloads :',
                'children': [
                    { 'name': 'October : pdf' },
                    { 'name': 'November : pdf' },
                    { 'name': 'Tutorial : html' },
                ],
            },
            {
                'name': 'Videos :',
                'children': [
                    {
                        'name': 'Tutorials :',
                        'children': [
                            { 'name': 'Basic layouts : mp4' },
                            { 'name': 'Advanced techniques : mp4' },
                            { 'name': 'All about app : dir' },
                        ],
                    },
                    { 'name': 'Intro : mov' },
                    { 'name': 'Conference introduction : avi' },
                ],
            },
        ]
        
        # create the tree 
        super().__init__(
            items = items
        )