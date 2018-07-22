#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask_script import Manager, Server
from flask_script.commands import Clean, ShowUrls

from flask_server.app import create_app


#app = create_app(os.environ.get('FLASK_ENV') or 'DevConfig')
app = create_app()
manager = Manager(app)

manager.add_command('server', Server())
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('docker', Server(host='0.0.0.0', port=5000))

if __name__ == '__main__':
    manager.run()
