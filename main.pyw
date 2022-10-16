""" main.py """
# Copyright 2022 Yuki Yamamoto
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import subprocess

import keyboard
import pyperclip

logging.basicConfig(filename='myapp.log', level=logging.INFO)


def main():
    """main"""
    word = pyperclip.paste().replace(" ", "+")
    url = f"https://www.google.com/search?q={word}+meaning"
    exe_str = f"start {url}"
    logging.info("searched words: %s", str(word))
    _ = subprocess.Popen(exe_str, shell=True,
                         stdin=None, stdout=None,
                         stderr=None, close_fds=True)


if __name__ == "__main__":
    logging.info("Start hot_google_py.")
    keyboard.add_hotkey("ctrl+alt+c", main)
    keyboard.wait("ctrl+alt+space")
