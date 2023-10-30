#!/usr/bin/env python3
import argparse
import subprocess
import os
import time
from datetime import datetime as dt

LIVE_OUTPUT_FILE_PATH = '/tmp/summaries-out.pdf'
PANDOC_COMMAND = 'pandoc'
LAUNCH_PDF_VIEWER_COMMAND = 'open'
UPDATE_PERIOD_S = 1
TO_WATCH = [ 'styles.css', 'template.html' ]

parser = argparse.ArgumentParser(
    prog='./export.py',
    description='Automates the export of markdown files to PDF through pandoc. It supports live reload.'
)

parser.add_argument('input_file_path', metavar='input-file')
parser.add_argument('-l', '--live', action='store_true')

args = parser.parse_args()

TO_WATCH.append(args.input_file_path)

if not args.live:
    raise NotImplementedError

def render():
    print(f'[{dt.now()}] Rendering document...')
    subprocess.run([PANDOC_COMMAND, args.input_file_path, '-o', LIVE_OUTPUT_FILE_PATH,
                    '--defaults', 'defaults'])

render()

subprocess.Popen([LAUNCH_PDF_VIEWER_COMMAND, LIVE_OUTPUT_FILE_PATH])

old_stamps = [ os.stat(file_path).st_mtime for file_path in TO_WATCH ]

while True:
    time.sleep(UPDATE_PERIOD_S)

    current_stamps = [ os.stat(file_path).st_mtime for file_path in TO_WATCH ]

    if current_stamps != old_stamps:
        old_stamps = current_stamps
        render()
