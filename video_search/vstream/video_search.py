import json
import re
import urllib
from mechanize import Browser

PREFIX_LINK = "https://api.import.io/store/connector/_magic?url=https%3A%2F%2F"
SUFFIX_LINK = "%2F&format=JSON&js=false&_apikey=aac429e34e5c49b2b52a5c3a9303febe084eb79\
59f63562017b1cc159a6e1e2565f371008ffe01ff9422d76097c4acf642cc7a4d28615fffc992d17fc73705\
9d4b122b9b163ee36c0192e10c29b14c3a"

# test links .Remove them later
air_mozilla_2015_engineering = "https://air.mozilla.org/channels/engineering/"
pycon_india_2015 = "https://www.youtube.com/channel/UCgxzjK6GuOHVKR_08TT4hJQ/videos?spf\
reload=5"
pycon_2014 = "https://www.youtube.com/user/PyCon2014"


def create_link(link):
    link = link.replace("https://", "")
    link = link.replace("/", "%2F")
    complete_link = PREFIX_LINK + link + SUFFIX_LINK
    return complete_link


def collect_info_mozilla(mozilla_link):
    complete_link = create_link(mozilla_link)
    br = urllib.urlopen(complete_link)
    video_info = json.load(br)
    for data in video_info.get("tables"):
        results = data.get("results")
        for data in results:
            print data.get("entrysummary_link/_source")  # name
            print data.get("entrysummary_link")  # link
            print data.get("entrysummary_description")  # description
            print data.get("timeago_value")  # date and time


def collect_info_youtube(youtube_channel_link):
    complete_link = create_link(youtube_channel_link)
    br = urllib.urlopen(complete_link)
    video_info = json.load(br)
    for data in video_info.get("tables"):
        results = data.get("results")
        for data in results:
            print data.get("uixtile_link/_text")  # name
            print data.get("uixtile_link")  # link
            print data.get("lockupmeta_value_numbers")  # number of views.
            print data.get("videotime_value")  # duration 


def input_video_link():
    link = raw_input()
    if "youtube" in link:
        collect_info_youtube(link)
    elif "mozilla" in link:
        collect_info_mozilla(link)

input_video_link()

