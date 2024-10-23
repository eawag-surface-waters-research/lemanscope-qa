# -*- coding: utf-8 -*-
import sys
import argparse
from qa import quality_assurance
from functions import download_metadata, upload_metadata

def main(params):
    print("Downloading Eye on Water metadata")
    data = download_metadata()
    print("Running quality assurance")
    data = quality_assurance(data)
    if params["upload"]:
        if params["aws_id"] and params["aws_key"] and params["bucket"]:
            print("Uploading metadata to {}".format(params["bucket"]))
            upload_metadata(data, params["bucket"], params["aws_id"], params["aws_key"])
        else:
            raise ValueError("aws_id, aws_key and bucket must be provided for upload.")

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 9):
        raise Exception('Requires python 3.9')
    parser = argparse.ArgumentParser()
    parser.add_argument('--upload', '-u', help='Upload', action='store_true')
    parser.add_argument('--bucket', '-b', help="Bucket", type=str, default=False)
    parser.add_argument('--aws_id', '-i', help="AWS access key id", type=str, default=False)
    parser.add_argument('--aws_key', '-k', help="AWS secret access key", type=str, default=False)
    args = parser.parse_args()
    main(vars(args))
