#!/bin/bash
for f in .ros/log/*/master.log do
cat $f | grep goal | tee -a goal.log
done
