#-------------------------For Single Video----------------------------

# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=TH3d5cyeer0")
# dw = yt.streams.get_by_itag(22)
#
# dw.download("E:/")

#-------------------------For Multiple Video----------------------------

# from pytube import YouTube
#
# video_list = ["https://www.youtube.com/watch?v=UT58ETAj3cg","https://www.youtube.com/watch?v=TH3d5cyeer0"]
#
# for i in video_list:
#     yt = YouTube(i)
#     dw = yt.streams.get_by_itag(22)
#     dw.download("F:/")
#     print("Downloaded",i)

#-------------------------For Multiple Video using file handling----------------------------

# from pytube import YouTube
#
# video_list = open("list.txt","r")
#
# for i in video_list:
#     yt = YouTube(i)
#     try:
#         dw = yt.streams.first()  # take highest resolution
#         dw.download("F://")
#         print("Downloaded", i)
#     except:
#             print("Download Failed",i)

#----------------------For One Line Code---------------------------

# import pytube
#
# pytube.YouTube("https://www.youtube.com/watch?v=ULHNeeb5Yls").streams.first().download("F:/")

#----------------------For Complete Playlist----------------------------

import pytube

pytube.Playlist("https://www.youtube.com/watch?v=1sXdoIECpuk&list=PLyDNc-mLpTPYJ_bN_iMsFhlCSw4u5OhOB").download_all("F:/")

#------------------------------------------------------------------------
