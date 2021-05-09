import boto3
import json
import os

s3 = boto3.client("s3")


def request_upload_URL(event, context):
    params = json.loads(event["body"])
    parts = s3.generate_presigned_post(
        Bucket=os.environ["BUCKET"],
        Key=params["name"],
        Fields={
            "Content-Type": params["type"],
            "Expires": 3600,
            "acl": "public-read",
        },
    )
    url = parts["url"]
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"uploadURL": url}),
    }
    return response
