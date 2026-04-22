## Mastodon-to-Twitter-Sync
Syncs new posts from Mastodon to Twitter.

Supports media uploads and the automatic splitting of long posts. Posts are synced as replies on Twitter; replies, quoted posts, and posts beginning with `@` are excluded. Also supports the automatic extension of short videos.

If this is your first time running the script, it will only begin syncing posts created *after* this initial run.

If you wish to sync all your *previous* tweets to Mastodon, [give this a try! ](https://github.com/klausi/mastodon-twitter-sync) — I have successfully imported all my previous tweets into the instance I set up myself.

- Required packages: `requests`, `mastodon.py`, `pickle`, `tweepy`, `retrying`, `termcolor`, `bs4`, `moviepy`

- The automatically generated `media` folder is used to store cached media files, while `synced_toots.pkl` stores a record of all toots that have already been synchronized.

![1689405706148.png](https://global.cdn.mikupics.cn/2023/07/15/64b24910d56be.png)

## Usage

- Install packages: ```pip install -r requirements.txt```
- Copy `config.sample.py` to the same directory and rename it to `config.py`.
- Modify the Twitter and Mastodon parameters within `config.py`, then simply run `python mtSync.py`.
- Since commit [9399c2](https://github.com/XiaoMouz/Mastodon-to-Twitter-Sync/commit/09399c2255c497b9bfa61beaba481fc21a6b56d8), a check for the `#no_sync` tag has been implemented; adding the `#no_sync` tag to the end of a toot will prevent it from being synchronized to Twitter.

## Running as a Background Service (Linux)

- Modify the systemd service file (`mastodon-twitter-sync.service`) to suit your specific Linux distribution and system configuration.
- ```systemctl enable mastodon-twitter-sync # Enable auto-start on boot```
- ```systemctl start mastodon-twitter-sync # Start the service```

## config.py Parameter Descriptions
`sync_time`: The program periodically polls Mastodon to check for new posts; this parameter controls the interval between checks (in seconds).

`log_to_file`: Determines whether logs are saved to the file `out.log`.

`limit_retry_attempt`: The maximum number of retry attempts. The default is 13; if retries are exhausted without success, the post is skipped, and its ID is saved to `sync_failed.txt`. Setting this value to 0 enables infinite retries; while this may potentially exhaust your API request quota, it ensures the program does not terminate due to reaching a maximum retry limit caused by errors.

`wait_exponential_max`: The maximum waiting time for a single retry attempt (in milliseconds). The default is 30 minutes. In the event of an error, the waiting time between consecutive retries increases exponentially.

`wait_exponential_multiplier`: The multiplier governing the exponential growth of the waiting time between retries. The default value is 800 (representing `original waiting time × 0.8`); if you wish to shorten the waiting time for each subsequent retry, you can reduce this value.

Waiting time per retry (seconds) = ( `2` raised to the power of `current retry count` ) * ( `wait_exponential_multiplier` / 1000 )
