import boto3

s3 = boto3.resource('s3')

#listar buckets
#for bucket in s3.buckets.all():
#    print(bucket.name)

# Enviar arquivo
data = open('novoArquivo.txt')
s3.Bucket('python-codes').put_object(Key='novoArquivo.txt', Body=data)
