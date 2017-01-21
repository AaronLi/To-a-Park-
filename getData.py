def getData(f):
    "f is the opened file"
    getdata = []
    #ali is the entire file
    ali = f.read().decode().split("<entry>")

    for entry in ali:#looking for
        linedata = []

        for line in entry.split("\n") :
            if line[:4] == "<id>":
                continue
            data = line.strip(">").split(">")
            if len(data) == 1 or len(data) > 2:
                continue
            data2 = []
            for k in data:
                data2 = data2 + k.split("<")
            if data2[-1][3:] != "__id":
                 linedata.append(data2[-1][3:]+" " + data2[-2].strip())
        getdata.append(linedata)
    return getdata
