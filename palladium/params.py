import os
import sys
import json

from palladium.chromium_setup import setup

project_dir = os.path.dirname(sys.modules['__main__'].__file__)

module_dir = os.path.dirname(os.path.realpath(__file__))

setup(module_dir)

with open(os.path.join(module_dir, 'config.json'), 'r') as fp:
    config = json.load(fp)

chromebinary = config['chromebinary']
chromedriver = config['chromedriver']