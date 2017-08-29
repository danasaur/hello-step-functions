build:
	docker build --no-cache -t deploy-container .

dev:
	docker run -it -v `pwd`:/code deploy-container bash

stack:
	AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
	AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

	docker run --rm -it -e AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) -e AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY) -v `pwd`:/code ansible2 ansible-playbook deploy.yml --connection=local
