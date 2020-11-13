# Amphora Wiki

![amphora-wiki-logo](amphora_wiki.png)

This is a simple wiki based on Pythons Flask framework.
There is much great wiki software.
Most of them are using some kind of database.
I however just want to put my markdown files in a directory and get a working wiki.

## Features/To-Dos

- [x] Plain text support for wiki entries
  - [x] Markdown Files (.md)
- [x] Entry page
  - [ ] Option to get plain text file
  - [ ] Optimize CSS for code
- [x] Start page
  - [ ] Overview of pages and namespaces
- [x] Search page
  - [x] Full-text search
  - [x] Show first few lines of each match (preview)
  - [ ] Better CSS
- [x] Navigation
  - [x] More advanced namespaces
  - [x] Header
  - [ ] Random article
  - [ ] Search bar in header
  - [x] Footer
- [x] Switchable CSS
  - [x] CSS dark-theme
  - [x] CSS light-theme
- [x] Config file
- [x] Docker installation
- [x] Logo

## Usage

### Create entries

Wiki entries are managed by plain markdown files in the `templates/entry/` directory.
The first line of each document is reserved as the title of the document.

## Deployment

### PIP/Python

- `git clone https://github.com/tiyn/amphora-wiki`
- `cd amphora-wiki/src`
- edit the `config.py` file according to your needs
- `pip3install -r requirements.txt` - install depenencies
- run `python app.py`
- wiki is available on port 5000

### Docker

Make sure you copy an example `config.py` and edit it before running the container.
The `config.py` can be found in the `src` folder.

#### Volumes

Set the following volumes with the -v tag.

| Volume-Name | Container mount           | Description                                                  |
| ----------- | ------------------------- | ------------------------------------------------------------ |
| config-file | /wiki/src/config.py       | Config file                                                  |
| entries     | /wiki/src/templates/entry | Directory for wiki entries                                   |
| css         | /wiki/src/static/css      | (optional) Directory for css files                           |
| html        | /wiki/src/templates       | (optional) Directory for templates (entry-volume not needed) |

#### Ports

Set the following ports with the -p tag.

| Container-Port | Recommended outside port | Protocol | Description |
| -------------- | ------------------------ | -------- | ----------- |
| 5000           | 80                       | TCP      | HTTP port   |

#### Example run-command

Either use the docker image `tiynger/amphora-wiki` or run
`docker build . -t amphora-wiki` in the top directory of this repository.
If so you need to change the command below apropiately
(`tiynger/amphora-wiki` to `amphora-wiki`).

`docker run --name wiki --restart unless-stopped -v <absolute-path-to>/config.py:/wiki/src/config.py -v entries:/wiki/src/templates/entry -p 80:5000 -d tiynger/amphora-wiki`
