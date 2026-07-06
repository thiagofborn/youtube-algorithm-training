# Training a model for YouTube Comments Classification

## Scope

Script drives real Chromium via Playwright, searches a set of study keywords (cloud/systems/math/science topics) on YouTube, opens top result, "watches" it for several minutes to feed YouTube's recommendation algorithm.

Goal: nudge my own YouTube home feed toward content I actually want to study, instead of microdopamine bait (shorts, drama, random algo-bait) it defaults to.

## Prerequisites (macOS / Linux)

- Python 3.9+ (`python3 --version`)
- pip (bundled with Python)
- ~500MB free disk (Playwright downloads Chromium)

macOS extra: Xcode Command Line Tools (`xcode-select --install`) if Python/pip missing.

Linux extra: Playwright's browser needs system libs. Easiest way — let Playwright install them:

```shell
sudo playwright install-deps
```

(Debian/Ubuntu users can skip that and instead `sudo apt-get install -y libnss3 libatk-bridge2.0-0 libcups2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2` if `sudo` for playwright isn't available.)

## Setup

```shell
# create venv (first time only)
python3 -m venv .venv

# activate it
source .venv/bin/activate

# install Python deps
pip install playwright

# download the Chromium browser Playwright drives
playwright install chromium
```

## Run it

```shell
./start-training.sh
```

or manually:

```shell
source .venv/bin/activate
python educating-youtube-for-me.py
```

First run opens a Chromium window under a persistent profile (`playwright_youtube_profile/`) — log into Google there if prompted; the session is reused on later runs.
