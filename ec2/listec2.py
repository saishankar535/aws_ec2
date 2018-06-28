import boto3
import click
session = boto3.Session()
ec2 = session.resource('ec2')
type(ec2)

@click.command()
@click.option ('--project', default=None,
               help = "Only instances for project")
def list_instances(project):
    instances = []
    if project:
        filter = [{'Name':'tag:Project','Values':[project]}]
        print(filter)
        instances = ec2.instances.filter(Filters=filter)
    else:
        instances = ec2.instances.all()
    for i in instances:
        print(i)
        print(', '.join((
            i.id,i.instance_type)))
    return
if __name__ == '__main__':
    list_instances()