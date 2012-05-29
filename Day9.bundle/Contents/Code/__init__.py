import urllib
import re

PLUGIN_PREFIX = "/video/Day9Daily"
ROOT = "http://blip.tv/day9tv?skin=rss"

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, "Day9 Daily", "icon-default.png", "art-default.png")
	Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
	Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
	MediaContainer.title1 = L('Day9 Daily')
	MediaContainer.viewGroup = 'List'
	MediaContainer.art = R('art-default.png')

def MainMenu(sender=None, page=1):
	dir = MediaContainer()
	#youTubeCookies = HTTP.GetCookiesForURL('http://www.youtube.com/')
	#dir.httpCookies = youTubeCookies
	
	if page == 1:
		pageURL = ROOT
	else:
		pageURL = ROOT + '&page=' + str(page)
		dir.replaceParent = True

	for episode in RSS.FeedFromURL(pageURL).entries:
		thumb = ''
		try:
			thumb='http://1.i.blip.tv/g?src=' + episode['blip_thumbnail_src'] + '&w=300&h=169&fmt=jpg'
		except:
			thumb = episode['blip_picture'] 
		dir.Append(Function(VideoItem(PlayEpisode, title=episode['title'], thumb=thumb), url=episode['links'][1]['href']))
	dir.Append(Function(DirectoryItem(MainMenu, title='More', thumb=R('icon-default.png')), page=page+1))
	return dir

def PlayEpisode(sender, url):
  return Redirect(url)
 
