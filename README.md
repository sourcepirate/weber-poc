## Web Archiver

A proof of concept implementation for a webarchival system

## Description

Essential components of web archival system

* Versioner
* Archiver
* Sheduler

In this implementation Git is used as a versioner, Cron is used as a scheduler. All data are stored in local disk.

## Running It

```

pip install git+http://github.com/sourcepirate/weber

weber add http://wikipedia.org

weber update # update the archiver

weber update_cron daily # updated the archive every one hour.


```

