import cherrypy

from TeleEngine.core import bot
from .TeleWebHookConfig import *
from telebot import types

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if all (('content-length' in cherrypy.request.headers,
                 'content-type' in cherrypy.request.headers,
                  cherrypy.request.headers['content-type'] == 'application/json')):

            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")

            update = types.Update.de_json(json_string)
            bot.process_new_updates([update])

            return ''
        else:
            raise cherrypy.HTTPError(403)

def start():
    WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = "/{}/".format(TOKEN)

    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))

    cherrypy.config.update({'global': {'engine.autoreload.on': False}})

    cherrypy.config.update({
        'server.socket_host': WEBHOOK_LISTEN,
        'server.socket_port': WEBHOOK_PORT,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': WEBHOOK_SSL_CERT,
        'server.ssl_private_key': WEBHOOK_SSL_PRIV,
        })

    cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})