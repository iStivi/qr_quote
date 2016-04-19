import qrcode
import click
from urllib.parse import quote

@click.command()
@click.argument('amount')
@click.option('-m', '--message', type=str, default='bitcoin payment')



def generate_quote(message, amount):
  address = "1ZUWgvPfNskFv3CeWUfE4QRHwTVsoiu9o"
  encode_string = 'bitcoin:' + address + '?amount=' +  amount + '&message=' + quote(message, safe='')
  print(encode_string)
  qr = qrcode.QRCode(
        version=5,  #version 3 is smallest size bitcoin address will compress to
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        border=4,
    )
  qr.add_data(encode_string)
  qr.make()
  img = qr.make_image()
  img.save("qr_view.png")

if __name__ == '__main__':
	generate_quote()
