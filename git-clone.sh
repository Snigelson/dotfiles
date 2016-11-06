#!/bin/bash
mkdir ~/build
cd ~/build
xargs -a <(awk '/^\s*[^#]/' git-repos) -r -n 1 -- git clone
