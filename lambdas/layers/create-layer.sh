zip -r python.zip python/

aws s3 cp python.zip s3://event-processor-sqs/layer/processor

aws lambda publish-layer-version --layer-name event-processor-generator  \
--content S3Bucket=event-processor-sqs,S3Key=layer/processor/python.zip --compatible-runtimes python3.7 python3.8

