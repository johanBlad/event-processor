# Bucket for Templates
aws s3 mb s3://event-processor-sqs
aws s3 rb s3://event-processor-sqs [--force]


aws cloudformation package \
    --s3-bucket event-processor-sqs \
    --template-file template.yml \
    --output-template-file dist/template-packaged.yml

aws cloudformation deploy \
    --template-file dist/template-packaged.yml \
    --stack-name event-processor-sqs \
    --capabilities CAPABILITY_IAM 


# Can only be used without SAM templates
aws cloudformation create-stack \
    --stack-name event-processor-sqs \
    --template-body file://template.yml \
    --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND 


aws cloudformation delete-stack \
    --stack-name event-processor-sqs 

# Layers
cd lambdas/layers/generator-deps/
cd lambdas/layers/processor-deps/

rm -rf ./python; rm python.zip
pip install -r requirements.txt -t ./python --upgrade; cp -r ../../common ./python
zip -r python.zip python/

cd ../../../

# aws s3 cp python.zip s3://event-processor-sqs/layers/generator/python.zip
# aws lambda publish-layer-version --layer-name event-generator  \
# --content S3Bucket=event-processor-sqs,S3Key=layers/generator/python.zip --compatible-runtimes python3.7 python3.8

# aws s3 cp python.zip s3://event-processor-sqs/layers/processor/python.zip
# aws lambda publish-layer-version --layer-name event-processor  \
# --content S3Bucket=event-processor-sqs,S3Key=layers/processor/python.zip --compatible-runtimes python3.7 python3.8