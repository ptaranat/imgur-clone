# Imgur Clone

![Build](https://github.com/ptaranat/shopify-challenge/actions/workflows/build.yml/badge.svg)
![Deploy](https://github.com/ptaranat/shopify-challenge/actions/workflows/deployer.yml/badge.svg)
![Vue](https://img.shields.io/badge/vue-2.6.12-green.svg)
![Issues](https://img.shields.io/github/issues/ptaranat/shopify-challenge)
![Size](https://img.shields.io/github/repo-size/ptaranat/shopify-challenge)
![License](https://img.shields.io/github/license/ptaranat/shopify-challenge)

This is currently live at [http://image-repo-frontend.s3-website.us-east-2.amazonaws.com/](http://image-repo-frontend.s3-website.us-east-2.amazonaws.com/)

### Features

- [x] Account registration and login using Amazon Cognito
  - If you would like to test it without your email, please use a service like [temp-mail.org](https://temp-mail.org/)
- [x] Secure upload to S3 bucket when logged in
  - Upload one or multiple images using drag and drop
  - You can access the images at `https://dev-image-repo-bucket.s3.us-east-2.amazonaws.com/your-image-name.png`
- [x] CI/CD using Github Actions [.github/workflows](.github/workflows)
  - [x] Build, lint and deploy Vue frontend in S3 bucket
  - [x] Deploy AWS Lambda functions using Serverless CLI
  - [x] Use Terraform to plan and apply infrastructure
  - [ ] Unit test Vue frontend
- [x] Populate home page with latest images from S3 bucket
- [ ] Access control for private/public images
- [ ] Secure deletion of images
  - This should use Cognito Auth to delete images from DB if the user owns that image
- [ ] Automatic tagging based on image features using Rekognition
- [ ] Search DynamoDB based on filenames and tags

### Local Deployment

Install Vue CLI

```
yarn global add @vue/cli
```

Serve a local version of the frontend

```
cd ./frontend
yarn install
yarn serve
```

### Resources

- [Elliot Forbes's "Building an Imgur Clone with Vue.JS and Node.JS"](https://tutorialedge.net/projects/building-imgur-clone-vuejs-nodejs/)
  - I have limited frontend experience so I followed most of this tutorial. Main difference is that I used Python for AWS Lambda functions instead of Node.
