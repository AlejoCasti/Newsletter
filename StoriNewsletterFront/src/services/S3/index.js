import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: import.meta.env.VITE_AWS_ACCESS_KEY,
  secretAccessKey: import.meta.env.VITE_AWS_SECRET_KEY,
  region: 'us-east-1'
});

const s3 = new AWS.S3();

export default s3;