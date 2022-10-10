from chalice import Chalice
from chalice import BadRequestError
import boto3
import json

app = Chalice(app_name='odaAPI')

@app.route('/batch-upload', methods=['POST'])
def batch_update():
    list = app.current_request.json_body

    # create sqs message for each item in list
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='BatchUpdateQueue')

    for item in list:
    #check if item is valid
        if 'id' not in item or 'status' not in item or 'path' not in item:
            raise BadRequestError("Invalid file information in request")
    #item json to string
        itemString = json.dumps(item)
   
    #send message to queue
        queue.send_message(MessageBody=itemString)

    return {
        'status': 200,
        'message': 'Success'
    }


  








