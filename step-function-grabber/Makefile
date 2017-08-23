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
	docker build -t flowers .

dev:
	docker run -it -v `pwd`:/code flowers bash

libs:
	conda install --yes --file requirements.txt
	mkdir -p serverless/libs
	cp -a /opt/conda/pkgs/. /code/serverless/libs

zip:
	cp serverless/grabber.py /code/serverless/libs/
	zip -r serverless/grabber-package.zip /code/serverless/libs/

clean:
	rm -rf $(LIBS_DIR)/*
	rm serverless/grabber-package.zip

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