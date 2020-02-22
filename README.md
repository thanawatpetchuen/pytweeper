# Pytweeper
A Twitter API crawler

## Features
* Twitter Authentication (OAuth)
* User's timeline `image only` crawler (up to `3000` tweets) (1 page = 200 tweets)

## Usage
```
pytweeper -o path/to/output -p last_page
```
### Arguments
* `-o` Output directory (Optional)
* `-p` The last page that you want to crawl
* `--logout` For logout and get new token 