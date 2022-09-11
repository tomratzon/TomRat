#!/bin/python3
import boto3
import sys

print("Menu\n1)Deploy Instances\n2)Stop Instances\n3)Start Instaces\n4)Describe Instances\n5)Terminate Instances\n")
choice=input("enter your choice here: ")

if choice == "1" :
	#exec(aws_deploy.py)
	#import aws_deploy.py
	ec2=boto3.resource('ec2')
	image=input("enter image id to create: ")
	minC=input("enter mincount: ")
	maxC=input("enter maxcount: ")
	#create new ec2 instances
	instances=ec2.create_instances(
        	ImageId=str(image),
		MinCount=int(minC),
		MaxCount=int(maxC),
		InstanceType='t2.micro',
		KeyName='toms_key')
elif choice == "2" :
	#exec(aws_stop.py)
	#import aws_stop.py
	ec2 = boto3.client('ec2')
	instId=input("enter the instance id to stop: ")
	idList=[]
	idList.append(instId)
	response = ec2.stop_instances(InstanceIds=idList, DryRun=False)
	print(response)
	print(str(instId)+"has stopped...")

elif choice == "3" :
        #exec(aws_start.py)
	#import aws_start.py
	instId=input("enter instance id to start: ")
	ec2 = boto3.client('ec2')
	idList=[]
	idList.append(instId)
	ec2.start_instances(InstanceIds=idList, DryRun=False)
	print(str(instId)+"has started...")

elif choice == "4" :
        #exec(aws_describe.py)
	#import aws_describe.py
	ec2 = boto3.client('ec2')
	response = ec2.describe_instances()
	print(response)

elif choice == "5" :
        #exec(aws_terminate.py)
	#import aws_terminate.py
	ec2 = boto3.resource('ec2')
	idList=[]
	for id in sys.argv[1:]:
		idList.append(ec2.Instance(id))
	ec2.instances.filter(InstanceIds = idList).terminate()

else:
	print("not avalid choice good bye...")

