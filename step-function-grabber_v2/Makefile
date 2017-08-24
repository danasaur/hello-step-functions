NAME = "python:2"

ENVDIR=envs
LIBS_DIR=serverless/libs
PROJECT=supersecret

.PHONY: clean \
	deploy \
	env-dir \
	shell \
	test \
	test-watch \
	libs

run = docker run --rm -it \
		-v `pwd`:/code \
		--env ENV=$(ENV) \
		--env-file envs/$2 \
		--name=$(PROJECT)-serverless-$(ENV) $(NAME) $1

build:
	docker build --no-cache -t flowers .

dev:
	docker run -it -v `pwd`:/code flowers bash

libs:
	conda install --yes --file /code/serverless/get_data_lambda/requirements.txt -v
	mkdir -p serverless/get_data_lambda/libs
	cp -a /opt/conda/pkgs/. /code/serverless/get_data_lambda/libs

zip:
	cp /code/serverless/get_data_lambda/get_data.py /code/serverless/get_data_lambda/libs/
	rm -rf /code/tmpdir
	mkdir -p /code/tmpdir
	cp -r /code/serverless/get_data_lambda/libs/* /code/tmpdir
	cd /code/tmpdir
	zip data.zip *
	# zip -r9 --exclude=Dockerfile \
	# --exclude=Makefile \
	# --exclude=*.pyc* \
	# --exclude=serverless \
	# --exclude=code \
	# /tmpdir/get_data_lambda-package.zip /tmpdir/*

clean:
	rm -rf $(LIBS_DIR)/*
	rm serverless/get_data_lambda/get_data_lambda-package.zip

shell: check-env env-dir
	$(call run,bash,$(ENV))

env-dir:
	@test -d $(ENVDIR) || mkdir -p $(ENVDIR)

# make libs should be run from inside the container
makelibs:
	@test -d $(LIBS_DIR) || mkdir -p $(LIBS_DIR)
	pip install -t $(LIBS_DIR) -r requirements.txt -v
	rm -rf $(LIBS_DIR)/*.dist-info
	find $(LIBS_DIR) -name '*.pyc' | xargs rm
	find $(LIBS_DIR) -name tests | xargs rm -rf

# NOTE:
#
#   Deployments assume you are already running inside the docker container
#
deploy: check-env
	cd serverless && sls deploy -s $(ENV)

# Note the ifndef must be unindented
check-env:
ifndef ENV
	$(error ENV is undefined)
endif