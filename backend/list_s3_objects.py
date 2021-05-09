import boto3
import decimal
import json

bucket = "dev-image-repo-bucket"
s3 = boto3.client("s3")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def list(event, context):
    try:
        keys = []
        body = s3.list_objects_v2(Bucket=bucket)
        for obj in body["Contents"]:
            keys.append(obj["Key"])

        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json",
            },
            "body": json.dumps(keys, cls=DecimalEncoder, default=str),
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)}),
        }
    finally:
        return response
