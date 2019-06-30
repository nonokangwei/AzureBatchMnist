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
_BATCH_ACCOUNT_KEY = 's+9rsHm/wRCSvS744dyo3R00yXWfHzc/NOkTus8x+z6AgUVUdspZTZaR+XljZWIDw5Z12qNDFtA5FXAhqi4ToQ=='
_BATCH_ACCOUNT_URL = 'https://batchgpu.westus2.batch.azure.com'
_STORAGE_ACCOUNT_NAME = 'mnistdemo'
_STORAGE_ACCOUNT_KEY = 'unCUtY3w76Z4amFuYnJYybR9pf/0/GnfrjOG+pyunEDUhRy01Gs6ETYPXNsR1P3tCrrMefvbVHwLmDQOeQNuPA=='
_POOL_ID = 'GPUDEMOPOOL'
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 1
_POOL_VM_SIZE = 'Standard_NC6'
_JOB_ID = 'MnistTrainJob'
_IMAGE_ID = "/subscriptions/c04b3c63-8dfe-4f98-be18-e71ff67a1f4e/resourceGroups/mnist/providers/Microsoft.Compute/images/gpuimage-image"
_MAX_TASKS_PER_NODE = 1
_OUTPUT_FILE_PREFIX = "mnisttrain1"
_CLIENT_ID = '1f9e5432-77d0-42c4-88da-f8d6a8516291'
_TENANT_ID = '72f988bf-86f1-41af-91ab-2d7cd011db47'
_SP_SECRET = 'hF/jZy-c*6K8p6M6Sbi/2n5Y_2@1tbK2'