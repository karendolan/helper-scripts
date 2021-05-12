# Script to count published episodes

With this script, you can count published episodes from Opencast search service.

## How to Use

### Configuration

First you need to configure the script in `config.py`:

| Configuration Key     | Description                                                                 | Example                                  |
| :-------------------- | :-------------------------------------------------------------------------- | :--------------------------------------- |
| `presentation_url`    | The (tenant-specific) presentation URL\*                                    | https://tenant.presentation.opencast.com |
| `digest_user`         | The user name of the digest user                                            | opencast_system_account                  |
| `digest_pw`           | The password of the digest user                                             | CHANGE_ME                                |


### Usage

The script can be called with the following parameters (all parameters in brackets are optional):

`main.py -s SERIES_ID [SERIES_ID ...]`


| Short Option | Long Option | Description                                                     |
| :----------: | :---------- | :-------------------------------------------------------------- |
| `-s`         | `--series`  | The id(s) of the series to count                                |

#### Usage example

`main.py -s 20210119999 20210119998 20210119997`

## Requirements

This script was written for Python 3.8. You can install the necessary packages with

`pip install -r requirements.txt`

Additionally, this script uses modules contained in the _lib_ directory.