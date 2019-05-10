Elite Exploration Map
=====================
This is a simple tool to draw a picture of your adventure in the Elite Dangerous Universe. This uses data sent to [EDSM](https://edsm.net). You'll need to set up a tool like EDDiscovery or Elite Dangerous Market Connector to send your data there, which is outside the scope of this tutorial.

Setup
-----
You will need python3 and pygame to use this application. On Mac, this might look something like

```
brew install python3
pip3 install pygame
```


Usage
-----
Download the latest [EDSM nightly dump](https://www.edsm.net/dump/systemsWithCoordinates.json). Save this in the same directory as the code.

[Export your flight logs](https://www.edsm.net/en/settings/export) - save the main flight logs as "all.txt" and the first-discovered flight logs as "first.txt".

Then run

    ./mapping.py parse
    ./mapping.py draw

The parse step will take several minutes depending on your CPU. It will print out a message every 100000 stars that get scanned. Drawing will be simpler: it will draw every system you have seen with a yellow pixel and every system you discovered first with a green pixel.
