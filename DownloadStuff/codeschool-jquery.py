#!/bin/python
 
import requests
import re
 
def start():
	chapter_links=[]
	course="http://try.jquery.com/"
	response=requests.get(course)
	chapter_pattern=re.compile(r'(http[s]?://try.jquery.com/levels/\d)"')
	for each in chapter_pattern.findall(response.content):
		chapter_links.append(each)
	print "Number of Chapters:", len(chapter_links)
	return chapter_links
 
def gather_pages(chapter_links):
	page_links=[]
	page_pattern=re.compile(r'href=\\"(http[s]?://try.jquery.com/levels/\d+/sections/\d+)\\"')
	for each in chapter_links: 
		response=requests.get(each)
		page_links.extend(list(set(page_pattern.findall(response.content))))
	return page_links
 
def gather_videos(page_links):
	video_links={}
	video_pattern=re.compile(r'\"url\":"(http://projector.codeschool.com/videos/.*?profile=720p.*?)\"')
	count=0
	for each in page_links:
		response=requests.get(each)
		video_link=video_pattern.findall(response.content)
		if video_link:
			count+=1
			video_links[str(count)]=video_link
	print "Number of videos to download:", len(video_links.keys())
	return video_links
 
with open("downloads.txt", 'w') as f:
	for k,v in gather_videos(gather_pages(start())).items():
		line='url="' + ",".join(v) + '"' + '\n' + 'output="' + k + '.mp4"' + '\n'
		f.write(line)
 
# Run downloads.txt in terminal with `curl -L -K downloads.txt`
