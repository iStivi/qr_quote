import qrcode
import click

@click.command()
@click.argument('amount')
@click.option('-m', '--message', default="bitcoin payment")



def generate_quote(amount, message):
	address = "1ZUWgvPfNskFv3CeWUfE4QRHwTVsoiu9o"
	encode_string = 'bitcoin:' + address + '?amount=' + amount + '&message=' + message
	print(message)

if __name__ == '__main__':
	generate_quote()
