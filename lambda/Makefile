# deploy, deploy-invoke and invoke variables
LAMBDA_FUNCTION ?= dig-lambda
LAMBDA_INVOCATION_TYPE ?= Event
LAMBDA_LOG_TYPE ?= Tail
LAMBDA_OUTFILE ?= dig-lambda.out
LAMBDA_REGION ?= us-east-1

# internal variables
SHELL := /bin/sh

# build generates an Amazon Lambda compatible function zip file
build: clean requirements update-submodules
	rm -f dig-lambda.zip
	mkdir -p .build
	cp main.py .build/
	cp -rp bin .build/
	cp -rp .requirements/* .build/
	cp dnspop/results/bitquark_*_subdomains_popular_1000 .build/dnspop-1k
	cp dnspop/results/bitquark_*_subdomains_popular_10000 .build/dnspop-10k
	if find dictionaries -mindepth 1 -print -quit | grep -q .; then cp dictionaries/* .build/; fi
	if [ -f 'name-servers.txt' ]; then cp name-servers.txt .build/; fi
	cd .build && zip -r dig-lambda.zip .
	mv .build/dig-lambda.zip .
	make clean


# removes build artifaces
clean:
	if [ -d '.build' ]; then rm -rf .build; fi


# builds and deploys the function code and supporting files to the designated 
# Amazon Lambda function using the arguments specified (see README.md and above)
deploy: build
	echo "Deploying to AWS Lambda..."
	aws lambda update-function-code --function-name $(LAMBDA_FUNCTION) --region $(LAMBDA_REGION) --zip-file fileb://dig-lambda.zip
	rm -f dig-lambda.zip


# both deploys and invokes the function in one command
deploy-invoke: deploy invoke


# invokes the Amazon Lambda function using the arguments specified (see 
# README.md and above)
invoke:
	echo "Invoking dig-lambda - results will be written to $(LAMBDA_OUTFILE)"
	aws lambda invoke --invocation-type $(LAMBDA_INVOCATION_TYPE) --cli-connect-timeout 300 --function-name $(LAMBDA_FUNCTION) --log-type $(LAMBDA_LOG_TYPE) --region $(LAMBDA_REGION) $(LAMBDA_OUTFILE)
	cat $(LAMBDA_OUTFILE)
	echo ""


# Downloads DNSRecon's required Python libraries
requirements:
	echo "Adding Python libraries to deployment package..."
	mkdir -p .requirements
	cd .requirements && pip install validators --upgrade -t .


# Updates the repository sub-modules - dnspop and dig
update-submodules:
	cd dnspop && git pull
