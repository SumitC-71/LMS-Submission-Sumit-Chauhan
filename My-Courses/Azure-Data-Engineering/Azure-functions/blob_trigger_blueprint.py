# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blob_trigger_blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging

blob_trigger_blueprint = func.Blueprint()



@blob_trigger_blueprint.blob_trigger(arg_name="myblob", path="raw-container", source="EventGrid",
                               connection="sarevision_STORAGE") 
def event_grid_blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger (using Event Grid) function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")