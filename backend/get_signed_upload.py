import boto3
import json
import os

s3 = boto3.client("s3")


def request_upload_URL(event, context):
    body = json.loads(event["body"])
    s3_params = {
        "Bucket": os.environ["BUCKET"],
        "Key": body["name"],
        "ContentType": body["type"],
        "ACL": "public-read",
    }

    url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params=s3_params,
    )
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"uploadURL": url}),
    }
    return response
