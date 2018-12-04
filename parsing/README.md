# Instructions on Accessing the Million Song Datset From AWS Public Snapshot
Note that an output of ~400,000 songs can be located inside the data directory (hosted on Google Drive).
To gain access to the entire Million Song Dataset and convert it to CSV, follow the following steps:
 1. First go to AWS EC2 and create a new instance (e.g. m5a.2xlarge) that already has support for python and associated libraries. Make sure that it is running before proceeding.
2. Then ensure that AWS CLI is setup and run ./create_volume.sh.
3. Now attach the volume to the EC2 instance by running ./attatch_volume.sh. Make sure to fill out the volume id and EC2 instance id inside the file. These can be obtained via the web console.
4. Now transfer the parsing directory to the EC2 machine.
5. Run ./convert_hdf5_to_csv.sh to mount the volume and start converting HDF5 to CSV.
6. Once complete, run ./transfer_file_to_aws.sh to upload the file to S3. Remember to fill out the bucket name! Also MAKE SURE THAT YOUR DEFAULT BUCKET POLICY IS NO PUBLIC ACCESS!!!
7. Now clean up all your instances by going to EC2 instance and terminating the running instance. Also go to EC2->Volumes and delete the volume.

Reminder:
To transfer a file to AWS:
  scp -i AWS-KEY.pem -r /parsing/ ec2-user@awsaddress:
