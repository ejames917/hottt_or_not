#!/bin/bash

# Credit to https://docs.aws.amazon.com/cli/latest/reference/ec2/create-volume.html
# Credit to https://aws.amazon.com/datasets/million-song-dataset/
aws ec2 create-volume --size 500 --region us-east-1 --availability-zone us-east-1a --snapshot-id snap-5178cf30 --volume-type io1 --volume-type gp2
