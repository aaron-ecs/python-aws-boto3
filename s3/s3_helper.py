""" Simple AWS S3 bucket client """
import boto3


class S3Helper:
    """ Simple AWS S3 bucket client """
    s3 = boto3.resource('s3')
    BUCKET_NAME = 'aaron-williams-s3-bucket'

    @staticmethod
    def list_all_s3_buckets():
        """ List All S3 Buckets"""
        buckets = boto3.resource('s3')
        return buckets.buckets.all()

    def upload_file_to_bucket(self, file):
        """ Upload to Bucket """
        self.s3.Object('aaron-williams-s3-bucket', file).put(Body=open(file, 'rb'))

    def download_file_from_bucket(self, file):
        """ Download from Bucket"""
        self.s3.Bucket(self.BUCKET_NAME).download_file(file, 'download_file.txt')

    def list_all_content_in_bucket(self):
        """ List All Contents """
        for bucket in self.s3.buckets.all().filter(Bucket='aaron-williams-s3-bucket'):
            return bucket.objects.all()

    def delete_all_items_in_bucket(self):
        """ Purge all items in given bucket """
        self.s3.Bucket(self.BUCKET_NAME).objects.delete()
