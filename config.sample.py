# Twitter API Config
twitter_config = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': '',
    'bearer_token': ''
}

# Mastodon Config
mastodon_config = {
    'client_id': '',
    'client_secret': '',
    'access_token': '',
    'api_base_url': 'https://'
}

main_config = {
    'sync_time' : 60 , # Check the interval (in seconds) for new synchronization checks. If posts are published frequently, you may reduce this value.
    'log_to_file' : True , # Whether to write logs to a file
    'limit_retry_attempt' : 13 , # Maximum number of retries. The default is 13; if the operation still fails, it is saved to `sync_failed.txt`. Setting this value to 0 enables infinite retries, though doing so may exhaust your API request quota.
    'wait_exponential_max': 1000*60*30 ,# The maximum waiting time for a single retry, in milliseconds; defaults to 30 minutes.
    'wait_exponential_multiplier': 800 # The waiting time for a single retry increases exponentially (in milliseconds); it defaults to 800 ms. Decreasing this value reduces the waiting time for each attempt.
}
