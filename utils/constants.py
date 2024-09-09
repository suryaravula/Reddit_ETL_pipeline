from configparser import ConfigParser, NoSectionError, NoOptionError
import os

# Get the parent directory of the current script
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the path to the config file
config_file_path = os.path.join(parent_dir, 'config', 'config.conf')
config = ConfigParser()

try:
    # Check if the config file exists
    if os.path.exists(config_file_path):
        print(f"Loading config from {config_file_path}")

        # Read the config file
        with open(config_file_path, 'r') as config_file:
            config.read_file(config_file)

        # Get the SECRET and CLIENT_ID from the config file
        SECRET = config.get('api_keys', 'reddit_secret_key')
        CLIENT_ID = config.get('api_keys', 'reddit_client_id')

        INPUT_PATH = config.get('file_paths', 'input_path')
        OUTPUT_PATH = config.get('file_paths', 'output_path')

        AWS_ACCESS_KEY_ID = config.get('aws', 'aws_access_key_id')
        AWS_ACCESS_KEY = config.get('aws', 'aws_secret_access_key')
        AWS_REGION = config.get('aws', 'aws_region')
        AWS_BUCKET_NAME = config.get('aws', 'aws_bucket_name')

        print(f"Constants loaded from config file.")
    else:
        print(f"Config file not found. Using hardcoded values for SECRET and CLIENT_ID.")
except (NoSectionError, NoOptionError, FileNotFoundError) as e:
    print(f"Error loading config file: {str(e)}. Using hardcoded values for SECRET and CLIENT_ID.")

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)

