import logging
from pythonjsonlogger import jsonlogger
import sys
import traceback
from typing import Any, Generator, Type
import os

format_json: str = '%(asctime)s %(levelname)s %(funcName)s %(name)s %(filename)s %(lineno)d %(message)s'
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(fmt=format_json)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

def format_filepath(system_file_path):
    start = system_file_path.find('src')
    file_path = system_file_path[start:]
    if os.name == 'nt':
        file_path = file_path.replace('\\', '/')
    return file_path

def format_filename(system_file_path):
    start = system_file_path.find('src')
    file_path = system_file_path[start:]

    bar_break = '/'
    if os.name == 'nt':
        bar_break = '\\'

    list_paths = file_path.split(bar_break)
    return list_paths[-1]

def log_execept_hook(exctype, excvalue, exctraceback):
    type_error = exctype.__name__
    message = excvalue.__str__()

    traceback_stack_summary = traceback.extract_tb(exctraceback)
    last_frame_summary = traceback_stack_summary[-1]
    
    steptrace = []
    for step, frame_summary in enumerate(traceback_stack_summary):
        steptrace.append({
            'step': step + 1,
            'filepath': format_filepath(frame_summary.filename),
            'filename': format_filename(frame_summary.filename),
            'function': frame_summary.name,
            'line': frame_summary.lineno,
            'instruction': frame_summary.line
        })
      
    print('\nTraceback (most recent call last):')
    for trace in steptrace:
        print(
            f"{trace['step']}-"
            f"\tfilepath: '{trace['filepath']}'\n"
            f"\tfilename: '{trace['filename']}'\n"
            f"\tfunction: '{trace['function']}'\n"
            f"\tline: {trace['line']}\n"
            f"\tinstruction: '{trace['instruction']}'\n"
        )

    logger.error({
        'processName': 'Boilerplate',
        'message': f'{type_error}: {message}', 
        'filename': format_filename(last_frame_summary.filename),
        'pathname': format_filepath(last_frame_summary.filename),
        'lineno': last_frame_summary.lineno,
        'funcName': last_frame_summary.name
    }, extra={'traceback': steptrace})

sys.excepthook = log_execept_hook