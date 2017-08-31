from carto.auth import APIKeyAuthClient
from carto.datasets import DatasetManager
from _settings import USERNAME, APIKEY

USR_BASE_URL = "https://{user}.carto.com/".format(user=USERNAME)
auth_client = APIKeyAuthClient(api_key=APIKEY, base_url=USR_BASE_URL)

USR_BASE_URL = 'https://carto.com/user/dms2203'

#BASE_URL = "https://{organization}.carto.com/user/{user}/". \
    #format(user=USERNAME) # organization=ORGANIZATION
USR_BASE_URL = "https://{user}.carto.com/".format(user=USERNAME)
auth_client = APIKeyAuthClient(api_key=APIKEY, base_url=USR_BASE_URL, organization='dms2203')

# write here the path to a local file or remote URL
LOCAL_FILE_OR_URL = "data/processing/new-york_new-york_points.csv"

dataset_manager = DatasetManager(auth_client)
dataset = dataset_manager.create(LOCAL_FILE_OR_URL)

