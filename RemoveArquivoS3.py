import boto3

s3 = boto3.resource('s3')
s3.Bucket('python-codes').delete_object(Key='novoArquivo.txt')