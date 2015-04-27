#!/usr/bin/python
#coding:utf-8
__author__ = 'fuxin'

import csv
import requests
import urllib
import os


def run(file_name):
  mycsv = open(file_name,"rb")
  reader = csv.reader(x.replace('\0', '') for x in mycsv)
  for i in reader:
    print i


if __name__ == "__main__":
  run("date/ZARA - 2014.1..xls")