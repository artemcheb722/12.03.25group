import pika
import ssl


"""

Region	amazon-web-services::eu-north-1
Cluster	kebnekaise.lmq.cloudamqp.com (DNS load balanced)
Hosts	kebnekaise-01.lmq.cloudamqp.com
(Availability Zone eun1-az1)
Created at	2025-04-15 16:38 UTC+00:00



User & Vhost	rwhdsdft
Password	M2gMGasBcGHTCTvDJIvtrzqDEL7r2EPX 
Ports	5672 (5671 for TLS)
URL	amqps://rwhdsdft:***@kebnekaise.lmq.cloudamqp.com/rwhdsdft
"""

RMQ_HOST = 'kebnekaise-01.lmq.cloudamqp.com'
RMQ_PORT = 5671 #tls
RMQ_USER = 'rwhdsdft'
RMQ_PASSWORD = 'M2gMGasBcGHTCTvDJIvtrzqDEL7r2EPX'
RMG_VIRTUAL_HOST = 'rwhdsdft'

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    virtual_host=RMG_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=RMQ_USER, password=RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)

def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)