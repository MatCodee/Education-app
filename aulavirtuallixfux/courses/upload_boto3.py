'''
from django.conf import settings
import os
import threading
import sys
import boto3
from boto3.s3.transfer import TransferConfig


def multi_part_upload_with_s3():
    config = TransferConfig(multipart_threshold=1024 * 25,max_concurrency=10,multipart_chunksize=1024 * 25, use_threads=True)   
    file_path = os.path.dirname(__file__) + '/largefile.pdf'
    
    key_path = 'multipart_files/largefile.pdf'

    s3.meta.client.upload_file(file_path, settings.AWS_STORAGE_BUCKET_NAME, key_path,
                            ExtraArgs={
                                'ACL': 'public-read',
                                'ContentType': 'text/pdf'
                            },
                            Config=config,
                            Callback=ProgressPercentage(file_path))
    
    

class ProgressPercentage(object):
    def __init__(self, filename):
            self._filename = filename
            self._size = float(os.path.getsize(filename))
            self._seen_so_far = 0
            self._lock = threading.Lock()
            
    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            
            sys.stdout.write("\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))

            sys.stdout.flush()
'''