# PartyBotNoAds

A Fortnite HTTP/XMPP bot coded in Python with party capabilities rewritten by kaaaxcreators without Ads.

---

## Installation

Install Python 3.7, you can get it from here: [Python 3.7.0 Download](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe).

1. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

2. [Register](https://epicgames.com/id/register) a new Epic Games account.

3. Configure your bot and enter the new Epic Games account details.

4. Launch the fortnite.py file and enjoy.

If you use Caprover or Docker there is a Dockerfile and captain-definition which fine.

I didnt test repl.it compatibility with the custom module, but because of the Express Server it is easy to setup e.g. UptimeRobot to keep the Repl alive and online 24/7.

## Ads

I removed all the Ads piped into BenBotAsync. You can edit the ad text in the `config.json`. There are only shell and website ads but no ads that users of the bot will see
With `\n` you make a new line, therefore you can create a multiline text

## License

By downloading this, you agree to the Commons Clause license and that you're not allowed to sell this repository or any code from this repository. For more info see <https://commonsclause.com/>.

All Credits to [xMistt](https://github.com/xMistt) and [xMistt/fortnitepy-bot](https://github.com/xMistt/fortnitepy-bot)

Because of License and Rights I wont upload the Package to [PyPI](https://pypi.org/)

You can use my [Downloader](https://downloader.kaaaxcreators.de/#/home) and download only BenBotAsyncNoAds Folder by clicking [here](https://downloader.kaaaxcreators.de/#/home?url=https:%2F%2Fgithub.com%2Fkaaaxcreators%2Ffortnitepy%2Ftree%2Fmain%2FBenBotAsyncNoAds)

## Common Problems

`Captcha was enforced. Please enter a valid authorization code`

How to retrieve an authorization code:

Click the link below and log in to the account you want an authorization code for.
Copy the code from the redirectUrl value (<http://prntscr.com/srbujz>).
Link: <https://www.epicgames.com/id/logout?redirectUrl=https%3A//www.epicgames.com/id/login%3FredirectUrl%3Dhttps%253A%252F%252Fwww.epicgames.com%252Fid%252Fapi%252Fredirect%253FclientId%253D3446cd72694c4a4485d81b77adbb2141%2526responseType%253Dcode>
