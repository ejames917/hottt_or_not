#!/bin/bash

# Must have setup aws configure first
bucketName=
aws s3 mb s3://$bucketName
aws s3 cp msds.csv s3://$bucketName
aws s3 ls s3://$bucketName