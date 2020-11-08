import click
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("192.168.0.254",1883,60)


@click.command()
@click.option('--on/--off', default=False)
def cli(on):
    if on:
        click.echo('switching light on...')
        client.publish("vaxer/actions", "F")
    else:
        click.echo('switching light off...')
        client.publish("vaxer/actions", "E")
    client.disconnect()
