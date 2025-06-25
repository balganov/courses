s = input("Filename: ").lower().strip().split(".")

d = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
}

if s[-1] in d:
    print(d[s[-1]])
else:
    print("application/octet-stream")
