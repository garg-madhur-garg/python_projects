import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"DownloadSpeed: {download}\n"
      f"Upload speed: {upload}")