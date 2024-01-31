import s3 from './index';
const bucketName = import.meta.env.VITE_AWS_S3_BUCKET;

export default {
  sendFile({ file }) {
    if (!file) return;

    const params = {
      Bucket: bucketName,
      Key: file.name,
      Body: file,
    };

    s3.putObject(params, function (err, data) {
      if (err) console.log(err, err.stack);
    });
  },
};
