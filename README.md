# Backend: Django on Google Cloud Platform/App Engine

## Run app locally
Activate Python Environment
MacOS
```bash
source ../env/bin/activate && cd backend && python manage.py runserver
```
Windows 10
```bash
.\env_20220112\Scripts\activate && cd backend && python manage.py runserver
```

## First time deploy
Follow these instructions.
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
-Don't worry about the old Django version (2.2) they use. v3.1.7 is fine.
-Use Python 3.7, not Python 3.6.
-Remember to append ```--profile lcog``` to ```eb create```, ```eb status```, and ```eb deploy``` commands

## Deploy backend
In mainsite/middleware/CorsMiddleware, make sure the correct response["Access-Control-Allow-Origin"] is commented out.
`source ../env/bin/activate`
`eb deploy --profile lcog`

# Frontend: Quasar (Vue) on AWS S3

## First time setup
Install the dependencies
```bash
npm install
```

## Other userful things
Lint the files
```bash
yarn run lint
```



# Run the frontend locally
```bash
cd frontend && quasar dev
```

# Deploy frontend
```bash
cd frontend
quasar build
```
Navigate to https://s3.console.aws.amazon.com/s3/buckets/lane-fiber
Under the 'Objects' tab is the list of files
Drag the contents of frontend/dist/spa to the window to upload the build

# Locations
Production Frontend
```url
http://lane-fiber.s3-website-us-west-2.amazonaws.com/
```
Production Backend (API)
```url
http://lane-fiber-env.eba-n4u348rr.us-west-2.elasticbeanstalk.com/api/
```
Production Backend (Admin)
```url
http://lane-fiber-env.eba-n4u348rr.us-west-2.elasticbeanstalk.com/admin/
```

Local Frontend
```url
http://lane-fiber:8080/dashboard
```
Local Backend (API)
```url
http://lane-fiber:8000/api/
```
Local Backend (Admin)
```url
http://lane-fiber:8000/admin/
```