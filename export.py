#!/usr/bin/env python3
import argparse
import subprocess
import os
import time
from datetime import datetime as dt
from pathlib import Path

LIVE_OUTPUT_FILE_PATH = '/tmp/summaries-out.pdf'
PANDOC_COMMAND = 'pandoc'
LAUNCH_PDF_VIEWER_COMMAND = 'open'
UPDATE_PERIOD_S = 1
TO_WATCH = [ 'styles.css', 'template.html' ]
EXPORT_BASE_PATH = f'{Path.home()}/OneDrive/Corsi'

parser = argparse.ArgumentParser(
    prog='./export.py',
    description='Automates the export of markdown files to PDF through pandoc. It supports live reload.'
)

parser.add_argument('input_file_path', metavar='input-file')
parser.add_argument('-l', '--live', action='store_true')

args = parser.parse_args()

TO_WATCH.append(args.input_file_path)

def render():
    print(f'[{dt.now()}] Rendering document...')
    subprocess.run([PANDOC_COMMAND, args.input_file_path, '-o', LIVE_OUTPUT_FILE_PATH,
                    '--defaults', 'defaults'])

render()

if not args.live:
    export_path = Path(f'{Path(args.input_file_path).parts[0]}/summaries/{Path(*Path(args.input_file_path).parts[1:]).with_suffix(".pdf")}')
    full_export_path = Path(f'{EXPORT_BASE_PATH}/{export_path}')

    print(f'Export path: {full_export_path}')

    full_export_path.parent.mkdir(exist_ok=True, parents=True)

    os.popen(f'cp {LIVE_OUTPUT_FILE_PATH} {full_export_path}')

    exit(0)

subprocess.Popen([LAUNCH_PDF_VIEWER_COMMAND, LIVE_OUTPUT_FILE_PATH])

old_stamps = [ os.stat(file_path).st_mtime for file_path in TO_WATCH ]

while True:
    time.sleep(UPDATE_PERIOD_S)

    current_stamps = [ os.stat(file_path).st_mtime for file_path in TO_WATCH ]

    if current_stamps != old_stamps:
        old_stamps = current_stamps
        render()
