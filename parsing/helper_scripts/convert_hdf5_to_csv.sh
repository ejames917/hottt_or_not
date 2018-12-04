#!/bin/bash

# Mount volume and Convert hdf5 to csv
# Credit to https://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset
sudo mkdir /mnt/snap
sudo mount -t ext4 /dev/sdb /mnt/snap


sudo pip install tables
sudo pip install pandas
python h5_to_csv.py /mnt/snap/data/