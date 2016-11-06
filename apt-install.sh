#!/bin/bash
apt-get update
apt-get autoclean
xargs -a <(awk '/^\s*[^#]/' apt-packages) -r -- apt-get install --no-install-recommends
apt-get autoclean
