import pika
from influxdb import InfluxDBClient

# إعداد اتصال RabbitMQ
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
rabbitmq_channel = rabbitmq_connection.channel()
rabbitmq_channel.queue_declare(queue='temperature')

# إعداد اتصال InfluxDB
influx_client = InfluxDBClient(host='localhost', port=8086)
influx_client.switch_database('temperature_data')

def callback(ch, method, properties, body):
    temperature = float(body)
    data = [
        {
            "measurement": "temperature",
            "tags": {
                "location": "office"
            },
            "fields": {
                "value": temperature
            }
        }
    ]
    influx_client.write_points(data)
    print(f"Written to InfluxDB: {temperature}")

rabbitmq_channel.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
rabbitmq_channel.start_consuming()
