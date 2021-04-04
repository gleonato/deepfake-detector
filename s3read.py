import boto3

s3 = boto3.resource('s3')
# bucket = s3.Bucket('raw-videos-gleonato/datasets/dfdc/deepfake-detection-challenge/test_videos/')
bucket = s3.Bucket('raw-videos-gleonato')

for obj in bucket.objects.all():
    key = obj.key
    print(key)
    body = obj.get()['Body'].read()
    print(body)

