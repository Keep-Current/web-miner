#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Executes the app when running using gunicorn
"""


from webminer.external_interfaces.flask_server.app import create_app
app = create_app()

if __name__ == '__main__':
    app.run()
