# shopify-challenge

# Installation

`sudo npm install -g @vue/cli`  
`sudo npm update -g @vue/cli`  
`vue create frontend`  
In /backend:  
`npm install --save express`

# Terraform

Install terraform from zip
`tf init`  
Git ignore the .terraform cache.  
Set up AWS access keys (Account->My Security Credentials)
`tf plan`  
`tf apply`

# Serverless

This will be done on a new branch.
`sls deploy`

- S3 ETag must be wrapped in " quotes
- list_objects_v2 returns `Content[{"LastModified":datetime.datetime}]` and datetime is not serializable
- To fix, dump json with `default=str` so that datetime is resolved first
