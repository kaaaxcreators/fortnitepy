# BenBotAsyncNoAds
Python wrapper for the BenBot API without Ads.

## Examples:
```
import BenBotAsyncNoAds as BenBotAsync
import asyncio

async def ben_search():
    result = await BenBotAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name="Ghoul Trooper"
    )

    print(result.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(ben_search())
loop.close()
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

fortnitepy example:
```
import fortnitepy
import BenBotAsyncNoAds as BenBotAsync

client = fortnitepy.Client(
    auth=fortnitepy.EmailAndPasswordAuth(
        email='example@email.com',
        password='password123'
    )
)

@client.event
async def event_friend_message(message):
    args = message.content.split()
    split = args[1:]
    content = " ".join(split)

    if args[0] == '!skin':
        skin = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=content,
            backendType="AthenaCharacter"
        )

        await client.user.party.me.set_outfit(asset=skin.id)

client.run()
```
