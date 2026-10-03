with open("log.txt", 'r') as logs:
    with open('error.log','w') as err_log:
        for log in logs:
            if "ERROR" in log:
                err_log.write(log)
