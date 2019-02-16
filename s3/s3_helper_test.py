""" Test class for S3 client s3_helper """
import os
import random
import string
import unittest

from s3.s3_helper import S3Helper


class Test(unittest.TestCase):
    """ Test class for S3 client s3_helper """
    s3_helper = S3Helper()

    def test_listing_buckets(self):
        """ Check if our bucket is returned in the bucket collection """
        for bucket in self.s3_helper.list_all_s3_buckets():
            for _ in bucket.objects.filter(Bucket='aaron-williams-s3-bucket'):
                pass

    def test_deleting_all_items(self):
        """ Test all files are deleted after calling delete function """

        # GIVEN
        file = self.create_random_text_file()
        self.s3_helper.upload_file_to_bucket(file)

        # WHEN
        self.s3_helper.delete_all_items_in_bucket()

        # THEN
        for key in self.s3_helper.list_all_content_in_bucket():
            self.fail(key.key + " was found in bucket")
        self.delete_file(file)

    def test_uploading_to_bucket(self):
        """ Tests files can be uploaded correctly """

        # GIVEN
        file = self.create_random_text_file()

        # WHEN
        self.s3_helper.upload_file_to_bucket(file)

        # THEN
        assert self.check_for_file(file)
        self.delete_file(file)

    def test_downloading_from_bucket(self):
        """ Test files are downloaded correctly """
        # GIVEN
        file = self.create_random_text_file()
        self.s3_helper.upload_file_to_bucket(file)

        # WHEN
        self.s3_helper.download_file_from_bucket(file)

        # THEN
        assert self.check_file_exists(file)
        self.delete_file(file)
        self.delete_file("download_file.txt")

    def check_for_file(self, file):
        """ Test support method to check if a file exists within a bucket """
        for key in self.s3_helper.list_all_content_in_bucket():
            if key.key == file:
                return True
        return None

    def tearDown(self):
        self.s3_helper.delete_all_items_in_bucket()

    def create_random_text_file(self):
        """ Test support method to create a random new text file """
        file_name = format("%s.txt" % self.random_string(5))
        file = open(file_name, "w+")
        file.write(self.random_string(1))
        file.close()
        return file_name

    @staticmethod
    def random_string(string_length):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))

    @staticmethod
    def check_file_exists(file):
        """ Attempts to open a given file """
        return open(file, "r")

    @staticmethod
    def delete_file(file):
        """ Attempts to delete a given file """
        os.remove(file)
