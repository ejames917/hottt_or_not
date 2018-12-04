#!/bin/bash

# Credit to https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-volume.html

vol_id=
instance_id=

aws ec2 attach-volume --volume-id $vol_id --instance-id $instance_id --device /dev/sdb