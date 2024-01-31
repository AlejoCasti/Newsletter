from io import BytesIO

import boto3


class StorageService:
    @staticmethod
    def download_file(
            *,
            file_name: str
    ):
        f = BytesIO()
        s3 = boto3.client('s3')
        s3.download_fileobj('storienewsletter', file_name, f)

        return f.getvalue()
