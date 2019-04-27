

elif Section == "Discovery":
    for iDict in self.migratedata[Section]:
        for column_name in iDict["value"]:
            dat = iDict["value"][column_name]
            if type(dat) == bytearray:
                iDict["value"][column_name] = "ENCRYPTED"

    