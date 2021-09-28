# Use Discord Webhooks with Python

I coded an example to send post messagenges over a discord webhook with the python requests module.

## Configuration

Edit the 'config.json' in the config folder and change the url to you're webhook url

```json
{
    "url": "https://discord.com/api/webhooks/..."
}
```

## Usage
Just edit the payload. (Examples for the payload: https://gist.github.com/Birdie0/78ee79402a4301b1faf412ab5f1cdcf9)
```python
payload = {
	'avatar_url': 'https://linktopicture.png',
	'username': 'example username',
	'content': 'example message'
}
```
