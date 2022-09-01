import json
import logging
import time
import uuid
import azure.functions as func


def main(request: func.HttpRequest, translation: func.Out[str]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    start = time.time()

    req_body = request.get_json()
    subtitle = req_body.get("subtitle")

    data = {
        "Text": "test",
        "PartitionKey": "subtitle",
        "RowKey": str(uuid.uuid4())
    }
    translation.set(json.dumps(data))

    end = time.time()
    processingTime = end - start

    return func.HttpResponse(
        f"Processing took {str(processingTime)} seconds. Translation is: {subtitle}",
        status_code=200
    )
