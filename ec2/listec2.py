import boto3
session = boto3.Session()
ec2 = session.resource('ec2')
type(ec2)
for i in ec2.instances.all():print(i)