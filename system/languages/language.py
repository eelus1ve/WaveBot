# from typing import Union
# import discord
# from discord.ext import commands
import os


class Lang():
	def __init__(self, ctx: Union[commands.Context, discord.Interaction]):
		self.language = self.lang()

	def get_lang(self, ctx: commands.Context):
		lang_dict = {}
		path = "system\\Languages\\"
		lang_name = ""
		return self.language[lang_name]
    
	@staticmethod
	def lang(ctx: commands.Context):
		lang_dict = {}
		path = "system\\Languages\\"
		for i in os.listdir(path):
			if i == "language.py":
				continue
			lang_dict[i[:-4]] = {}
			with open(f'{part+i}', 'r', encoding='utf-8') as f:
				for line in f:
					if not (line.startswith('//')) and not (line == '\n'):
						key, *value = line.split()
						lang_dict[key] = ' '.join([i.replace('\\n', '\n') for i in value])
		return lang_dict