# Python Flask Wiki

This is a simple wiki based on Pythons Flask framework.
There is much great wiki software.
Most of them are using some kind of database.
I however just want to put my markdown files in a directory and get a working wiki.

## Features/To-Dos

- [x] Plain text support for blog entries
    - [x] Markdown Files (.md)
- [x] Entry page
    - [ ] Option to get plain text file
- [x] Search page
    - [x] Full-text search
    - [ ] Show first few lines of each match (description)
- [ ] Navigation
    - [ ] More advanced namespaces
    - [x] Header
        - [ ] Search bar in header
    - [x] Footer
- [x] Switchable CSS
    - [x] CSS dark-theme
    - [x] CSS light-theme
- [x] Config file
- [ ] Docker installation
    - [ ] Enable variables/environment variables
- [ ] Logo

## Usage

### Create entries

Wiki entries are managed by plain markdown files in the `templates/entry/` directory.
The first line of each document is reserved as the title of the document.

## Deployment

### PIP/Python

- `git clone https://github.com/tiyn/tiyny-blog`
- `cd flaskblog/src`
- edit the `config.py` file according to your needs
- `pip3install -r requirements.txt` - install depenencies
- run `python app.py`
- blog is available on port 5000

### Docker

Make sure you copy an example `config.py` and edit it before running the container.
The `config.py` can be found in the `src` folder.

#### Volumes

Set the following volumes with the -v tag.

| Volume-Name | Container mount           | Description                                                  |
|-------------|---------------------------|--------------------------------------------------------------|
| config-file | /blog/src/config.py       | Config file                                                  |
| entries     | /blog/src/templates/entry | Directory for blog entries                                   |
| css         | /blog/src/static/css      | (optional) Directory for css files                           |
| html        | /blog/src/templates       | (optional) Directory for templates (entry-volume not needed) |

#### Ports

Set the following ports with the -p tag.

| Container-Port | Recommended outside port | Protocol | Description |
|----------------|--------------------------|----------|-------------|
| 5000           | 80                       | TCP      | HTTP port   |

#### Example run-command

`docker run --name wiki --restart unless-stopped -v ./config.py:/wiki/src/config.py -v entries:/wiki/src/templates/entry -p 80:5000 -d tiynger/tiyny-wiki`
