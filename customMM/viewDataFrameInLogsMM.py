import logging

from iotfunctions import ui
from iotfunctions.base import BaseTransformer

logger = logging.getLogger(__name__)

#Specify the URL to your package here.
#This URL must be accessible via pip install

PACKAGE_URL = 'git+https://github.com/momadison/monitorMultiplyByFactor'

class viewDataFrameInLogsMM(BaseTransformer):

    def __init__(self, input_items,  output_items):

        self.input_items = input_items
        self.output_items = output_items
        super().__init__()
        logger.info('data items whole: ', self.input_items)
    def execute(self, df):
        df = df.copy()
        for i,input_item in enumerate(self.input_items):
            df[self.output_items[i]] = df[input_item]
            logger.info('data items in enumeration: ', df[input_item])
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items',
                datatype=float,
                description = "Data items adjust",
                output_item = 'output_items',
                is_output_datatype_derived = True)
                      )
        inputs.append(ui.UISingle(
                name = 'factor',
                datatype=float)
                      )
        outputs = []
        return (inputs,outputs)