# -*- coding: utf-8 -*-

"""
“Commons Clause” License Condition v1.0
Copyright Oli 2019-2020

The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.

Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.

For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.

Software: PartyBot (fortnitepy-bot)

License: Apache 2.0
"""

# System imports.
from typing import Optional, Union

import asyncio
# Third party imports.
from fortnitepy.ext import commands

import fortnitepy
import aiohttp
import crayons
import random


class PartyCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def get_playlist(self, display_name: str) -> str:
        async with aiohttp.ClientSession() as session:
            request = await session.request(
                method='GET',
                url='http://scuffedapi.xyz/api/playlists/search',
                params={
                    'displayName': display_name
                })

            response = await request.json()

        return response['id'] if 'error' not in response else None

    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the banner of the self.bot.",
        help="Sets the banner of the self.bot.\n"
             "Example: !banner BRSeason01 defaultcolor15 100"
    )
    async def banner(self, ctx: fortnitepy.ext.commands.Context,
                     icon: Optional[str] = None,
                     colour: Optional[str] = None,
                     banner_level: Optional[int] = None
                     ) -> None:
        await self.bot.party.me.set_banner(icon=icon, color=colour, season_level=banner_level)

        await ctx.send(f'Banner set to: {icon} with {colour} at level {banner_level}.')
        print(self.bot.message % f"Banner set to: {icon} with {colour} at level {banner_level}.")

    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the battlepass info of the self.bot.",
        help="Sets the battlepass info of the self.bot.\n"
             "Example: !bp 100"
    )
    async def bp(self, ctx: fortnitepy.ext.commands.Context, tier: int) -> None:
        await self.bot.party.me.set_battlepass_info(
            has_purchased=True,
            level=tier,
        )

        await ctx.send(f'Set battle pass tier to {tier}.')

    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the level of the self.bot.",
        help="Sets the level of the self.bot.\n"
             "Example: !level 999"
    )
    async def level(self, ctx: fortnitepy.ext.commands.Context, banner_level: int) -> None:
        await self.bot.party.me.set_banner(
            season_level=banner_level
        )

        await ctx.send(f'Set level to {level}.')

    @commands.dm_only()
    @commands.command(
        description="[Party] Sends message to party chat with the given content.",
        help="Sends message to party chat with the given content.\n"
             "Example: !echo i cant fix the fucking public lobby bots"
    )
    async def echo(self, ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
        await self.bot.party.send(content)
        await ctx.send('Sent message to party chat.')

    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the lobbies selected playlist.",
        help="Sets the lobbies selected playlist.\n"
             "Example: !playlist_id Playlist_Tank_Solo"
    )
    async def playlist_id(self, ctx: fortnitepy.ext.commands.Context, playlist_: str) -> None:
        try:
            await self.bot.party.set_playlist(playlist=playlist_)
            await ctx.send(f'Gamemode set to {playlist_}')
        except fortnitepy.errors.Forbidden:
            await ctx.send(f"Failed to set gamemode to {playlist_}, as I'm not party leader.")
            print(crayons.red(self.bot.message % f"[ERROR] "
                              "Failed to set gamemode as I don't have the required permissions."))


    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the parties custom matchmaking code.",
        help="Sets the parties custom matchmaking code.\n"
             "Example: !skin Nog Ops"
    )
    async def matchmakingcode(self, ctx: fortnitepy.ext.commands.Context, *, custom_matchmaking_key: str) -> None:
        await self.bot.party.set_custom_key(
            key=custom_matchmaking_key
        )

        await ctx.send(f'Custom matchmaking code set to: {custom_matchmaking_key}')

    @commands.dm_only()
    @commands.command(
        description="[Party] Sends the defined user a friend request.",
        help="Sends the defined user a friend request.\n"
             "Example: !friend Ninja"
    )
    async def friend(self, ctx: fortnitepy.ext.commands.Context, *, epic_username: str) -> None:
        if data['friend_accept']:
            await ctx.send('All friend requests will be accepted so there is no need to add manually.')
            print(self.bot.message % f'!friend command ignored as friend requests will be accepted '
                  'so there is no need to add manually.')
        else:
            user = await self.bot.fetch_user(epic_username)

            if user is not None:
                await self.bot.add_friend(user.id)
                await ctx.send(f'Sent/accepted friend request to/from {user.display_name}.')
                print(self.bot.message % f'Sent/accepted friend request to/from {user.display_name}.')
            else:
                await ctx.send(f'Failed to find user with the name: {epic_username}.')
                print(
                    crayons.red(self.bot.message % f"[ERROR] Failed to find a user with the name {epic_username}."))

    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the lobbies selected playlist using playlist name.",
        help="Sets the lobbies selected playlist using playlist name.\n"
             "Example: !playlist Food Fight"
    )
    async def playlist(self, ctx: fortnitepy.ext.commands.Context, *, playlist_name: str) -> None:
        try:
            scuffedapi_playlist_id = await self.get_playlist(playlist_name)

            if scuffedapi_playlist_id is not None:
                await self.bot.party.set_playlist(playlist=scuffedapi_playlist_id)
                await ctx.send(f'Playlist set to {scuffedapi_playlist_id}.')
                print(self.bot.message % f'Playlist set to {scuffedapi_playlist_id}.')

            else:
                await ctx.send(f'Failed to find a playlist with the name: {playlist_name}.')
                print(crayons.red(self.bot.message % f"[ERROR] "
                                  f"Failed to find a playlist with the name: {playlist_name}."))

        except fortnitepy.errors.Forbidden:
            await ctx.send(f"Failed to set playlist to {playlist_name}, as I'm not party leader.")
            print(crayons.red(self.bot.message % f"[ERROR] "
                              "Failed to set playlist as I don't have the required permissions."))

    @commands.dm_only()
    @commands.command(
        name="invite",
        description="[Party] Invites the defined friend to the party. If friend is left blank, "
                    "the message author will be used.",
        help="Invites the defined friend to the party.\n"
             "Example: !invite Terbau"
    )
    async def _invite(self, ctx: fortnitepy.ext.commands.Context, *, epic_username: Optional[str] = None) -> None:
        if epic_username is None:
            epic_friend = self.bot.get_friend(ctx.author.id)
        else:
            user = await self.bot.fetch_user(epic_username)

            if user is not None:
                epic_friend = self.bot.get_friend(user.id)
            else:
                epic_friend = None
                await ctx.send(f'Failed to find user with the name: {epic_username}.')
                print(crayons.red(self.bot.message % f"[ERROR] "
                                  f"Failed to find user with the name: {epic_username}."))

        if isinstance(epic_friend, fortnitepy.Friend):
            try:
                await epic_friend.invite()
                await ctx.send(f'Invited {epic_friend.display_name} to the party.')
                print(self.bot.message % f"[ERROR] Invited {epic_friend.display_name} to the party.")
            except fortnitepy.errors.PartyError:
                await ctx.send('Failed to invite friend as they are either already in the party or it is full.')
                print(crayons.red(self.bot.message % f"[ERROR] "
                                  "Failed to invite to party as friend is already either in party or it is full."))
        else:
            await ctx.send('Cannot invite to party as the friend is not found.')
            print(crayons.red(self.bot.message % f"[ERROR] "
                              "Failed to invite to party as the friend is not found."))



    @commands.dm_only()
    @commands.command(
        description="[Party] Sets the client to the \"Just Chattin'\" state.",
        help="Sets the client to the \"Just Chattin'\" state.\n"
             "Example: !justchattin"
    )
    async def justchattin(self, ctx: fortnitepy.ext.commands.Context) -> None:
        self.bot.default_party_member_config.cls = fortnitepy.JustChattingClientPartyMember

        party_id = self.bot.party.id
        await self.bot.party.me.leave()

        await ctx.send('Set state to Just Chattin\'. Now attempting to rejoin party.'
                       '\nUse the command: !lobby to revert back to normal.')

        try:
            await self.bot.join_party(party_id)
        except fortnitepy.errors.Forbidden:
            await ctx.send('Failed to join back as party is set to private.')
        except fortnitepy.errors.NotFound:
            await ctx.send('Party not found, are you sure Fortnite is open?')
