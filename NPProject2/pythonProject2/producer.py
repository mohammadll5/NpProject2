from influxdb import InfluxDBClient
import time
import psutil

# إعداد اتصال InfluxDB
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('performance_data')

while True:
    # قراءة نسبة استخدام CPU
    cpu_usage = psutil.cpu_percent(interval=1)

    data = [
        {
            "measurement": "cpu_usage",
            "tags": {
                "location": "cpu"
            },
            "fields": {
                "value": cpu_usage
            }
        }
    ]
    client.write_points(data)
    print(f"Written: {cpu_usage} %")

    time.sleep(10)
