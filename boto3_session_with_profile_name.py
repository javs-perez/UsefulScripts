# for debugging purposes
session = boto3.session.Session(profile_name="developer-xero-ps-paas-svc")
s3 = session.resource('s3')
bucket_tagging = s3.BucketTagging('xero-wtf-uat')
tags = bucket_tagging.tag_set
tag_names = [x['Key'] for x in tags]
