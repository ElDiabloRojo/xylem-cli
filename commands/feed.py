import click
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("192.168.0.254",1883,60)


@click.command()
def cli():
    client.publish("vaxer/actions", "F")
    client.disconnect()
