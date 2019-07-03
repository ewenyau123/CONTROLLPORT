#!/usr/bin/python
# coding: utf-8

import cherrypy
import subprocess

text = """
<html><body>
<form method='get' action='do_it'>
<input type='submit' value='Submit' />
</form></body>
{}
</html>
"""


class PiButton(object):
    @cherrypy.expose
    def index(self):
        return text.format("")

    @cherrypy.expose
    def do_it(self, *vargs, **kwargs):
        #command = "ls /"
        command = "python my_other_python.script.py"
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').replace('\n', '<br>')
        result2 = "command: {!r}<br>result:<br>{}".format(command, result)
        return text.format(result2)


    if __name__ == "__main__":
        cherrypy.engine.autoreload.unsubscribe()
        cherrypy.config.update({'server.socket_host': "0.0.0.0", 'server.socket_port': 8181})
        cherrypy.quickstart(PiButton(), '/', {'':{}})