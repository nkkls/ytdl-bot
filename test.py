import exporting
exporter = exporting.Exporter()

result = exporter.export("video", "https://soundcloud.com/deethew/eyes-closed", "mp4", True)
print(result)