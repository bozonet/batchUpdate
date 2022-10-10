# batchUpdate API

# Endpoint
https://3yj4p8wp1a.execute-api.eu-west-1.amazonaws.com/api/batch-upload

# Example Request Body
Endpoint needs an array of file informations.

```
 [
  {
		"id": "oythPLfwaPr0-83",
		"status": "completed",
        "path": "s3://bucket/83.jpg"
	},
    {
		"id": "oythPLfwaPr0-50",
		"status": "completed",
        "path": "s3://bucket/50.jpg"
	},
    {
		"id": "oythPLfwaPr0-12",
		"status": "completed",
        "path": "s3://bucket/12.jpg"
	}
]
```

# Architecture
* Chalice (Creating single file messages from batch request and send to SQS queue)
* SQS (Trigger lambda/updateFileFunction)
* Lambda Function (Request to client API with single file information)
