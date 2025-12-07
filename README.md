# Immich Random Photo API

This api is intended to run on the same host as an Immich install, where the database is exposed out of the container.

It's purpose is to serve random images to local photo frames/TVs on the same network.

With that in place, this api can be called as follows:

GET http://192.168.1.x/:8000/random-photo

```
{
    "album":"Spain 2018",
    date":"2018-07-26",
    "id":"0959c410-ce4a-4907-8118-40ba319e913c",
    "path":"b97a4f5d-0316-4b82-b46f-5e10f1a57ceb/91/65/9165a819-e928-4c6c-933d-f7ebafa67666.JPG"
}
```

The path can then be provided to the second endpoint to load the image

GET http://192.168.1.x:8000/{width}x{height}/image/{path}

A sample .service file is include to run the API via Gunicorn.

## Viewing the images

Two options are provided:

### 1. Browser-based slideshow

Access the slideshow endpoint. It is designed to work with _very_ old browsers so is good for those supplied with most TVs. It has pause/back/forward buttons that work with tv pointer remotes.

GET http://192.168.1.x:8000/slideshow

### 2. Direct HDMI output

* Get a network-enabled raspberry pi
* Clone this repo, populate .env with the HDMI_X values
* Install the packages in `requirements-hdmi.txt`
* Possibly install `libegl-dev` also
* Install and enable the hdmi-slideshow.service
