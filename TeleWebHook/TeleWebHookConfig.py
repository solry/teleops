"""Config for TeleWebHook"""

WEBHOOK_HOST = '200.1.1.1'
WEBHOOK_PORT = 8443  # 443, 80, 88, 8443
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_SSL_CERT = '/root/dev/nproject/ssl/webhook_cert.pem'  # certificate dir
WEBHOOK_SSL_PRIV = '/root/dev/nproject/ssl/webhook_pkey.pem'  # private key dir

TOKEN = ''