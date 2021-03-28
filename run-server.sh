#!/usr/bin/env bash

set -Eeuo pipefail

python3 -m http.server 8000 --bind 127.0.0.1 --directory example-site/

