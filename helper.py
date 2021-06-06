import json

from db.models.event_monitor import EventLog
from kafka.consumer.fetcher import ConsumerRecord


def convert_message(message: ConsumerRecord) -> EventLog:
    timestamp = message.timestamp
    value = message.value
    monitor_name = value['monitorName']
    health_status = json.dumps(value['healthStatus'])
    return EventLog(timestamp, monitor_name, health_status)
