import pafy

url=input("URL: ")
video = pafy.new(url)

streams = video.streams

for i in streams:
    print(i)

best = video.getbest()

print(best.resolution, best.extension)

best.download()
print("Download complete!")