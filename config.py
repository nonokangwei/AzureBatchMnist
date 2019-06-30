#-------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
#----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
#--------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "azurebatchdemo.py"

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.

_BATCH_ACCOUNT_NAME ='batchgpu'
_STORAGE_ACCOUNT_NAME = '' # Input your storage account name here
_STORAGE_ACCOUNT_KEY = '' # Input your storage account key here
_POOL_ID = '' # Set your batch pool name you'd like to use, example: GPUDEMOPOOL
_DEDICATED_POOL_NODE_COUNT = 0 # Set zero here, this demo using low priority resouce
_LOW_PRIORITY_POOL_NODE_COUNT = 1 # set one here, just using standalone node to do the demo
_POOL_VM_SIZE = 'Standard_NC6' # NC6 with K80 GPU Card as demo node
_JOB_ID = ''  # Set your batch job name you'd like to use, example: MnistTrainJob
_IMAGE_ID = "" # Set your customized image resource id here
_MAX_TASKS_PER_NODE = 1 # Set maximum task per node
_OUTPUT_FILE_PREFIX = ""  # Set the training output file prefix name, example: mnisttrain1
_CLIENT_ID = '' # Set your service principal client id here
_TENANT_ID = '' # Set your tenant id here
_SP_SECRET = '' # Set your service principal secret key here
