configs = {}
with open("config.txt","r") as config:
    print(config.readline())
    print(config.readline())
    next(config)
    for data in config.readlines():
        key, value = data.split("=")
        configs[key.strip()] = value.strip()
    print(configs)