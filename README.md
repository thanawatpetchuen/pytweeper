# Pytweeper
A Twitter API images crawler

## Features
* Twitter Authentication (OAuth)
* User's timeline `image only` crawler (up to `3000` tweets) (1 page = 200 tweets)

## Usage
First init the consumer keys
```
pytweeper init
```
Then
```
pytweeper
```
### Arguments
* `-o O` Output directory (Optional)
* `-p P` The last page that you want to crawl
* `--logout` For logout and get new token 