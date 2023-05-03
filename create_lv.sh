#!/bin/bash

fdisk /dev/sda<<endl
n


+2G
w
endl

PARTNAME=`ls -l /dev/sda* | tail -n 1 | awk '{ print $10 }'`

pvcreate $PARTNAME

vgcreate myvol  $PARTNAME

lvcreate -L 170M --name vo myvol

mkfs.ext3	/dev/myvol/vo

mkdir /my_volume

mount -t ext3 /dev/myvol/vo /my_volume

