import socket
import asyncio
import time
import random
import json
from dingtalkchatbot.chatbot import DingtalkChatbot

from walkoff_app_sdk.app_base import AppBase

class DingTalk(AppBase):
    __version__ = "1.0.0"
    app_name = "DingTalk"  # this needs to match "name" in api.yaml
    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    def send_text(self, access_token, access_token_secret, message): 
        bot = DingtalkChatbot(
            f"https://oapi.dingtalk.com/robot/send?access_token={access_token}",
            secret=access_token_secret,
        )
        return bot.send_text(message)

    def send_markdown(self, access_token, access_token_secret, title, message): 
        bot = DingtalkChatbot(
            f"https://oapi.dingtalk.com/robot/send?access_token={access_token}",
            secret=access_token_secret,
        )
        return bot.send_markdown(title, message)

if __name__ == "__main__":
    DingTalk.run()
