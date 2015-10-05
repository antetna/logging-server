# logging-server

## Description
Simple logging via socket handler allows simultane logging from different processes. 
This solves problems of writing to same log file from different processes.

## Requirements 
 - Python 3

## Configure
All settings are inside `config.py`
  - HOST - `localhost`
  - PORT - `9020` (DEFAULT_TCP_LOGGING_PORT)
  - LOG_CONFIG - https://docs.python.org/3.4/library/logging.config.html#logging-config-dictschema

## How to use
 - Start server `python logging-server.py`
 - Try demo app `python main.py`
 - inside logs directory you will find your logs


 

