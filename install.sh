su -c "easy_install --upgrade google-api-python-client"

#su -c "$PACKAGE_MANAGER $1 &> /dev/null"
if [ ! $? -eq 0 ]; then
	echo -e "$1 installed"
else
	#show_msn_w "$1 $RED no installed $RESET"
	su -c  "pip install google-api-python-client"
fi

sudo curl https://sdk.cloud.google.com | bash

if [ ! $? -eq 0 ]; then
	echo -e "$1 installed"
else
	#get last ver
	curl -s https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz | tar -zxO google-cloud-sdk/lib/googlecloudsdk/core/config.json | grep '"version"' | sed "s/.*:.*\"\(.*\)\".*/\1/"
fi
