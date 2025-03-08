Next steps:

- Django Settings: toggle AWS vs STATIC_ROOT static file storage based on environment type (dev,staging,production)
- CI: Set up GitHub Actions to build + push container
- CD: Set up Github Actions to redeploy ECS service
- Trusted domain: Register a domain in Route 53, create SSL certificates in ACM, update CloudFront distribution to use your domain and certificate