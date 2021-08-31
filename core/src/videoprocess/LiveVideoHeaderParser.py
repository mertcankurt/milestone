def ParseLiveVideoHeader(byteArrayData):
    image =  {}
    try:
        byteArrayData = byteArrayData[:len(byteArrayData)-3]
        byteArrayData = byteArrayData.decode("utf-8")
    except UnicodeDecodeError:
        print("[ERROR] 'utf-8' codec can't decode byte 0xf7 in position 0: invalid start byte")
        print(byteArrayData)

    header_list = byteArrayData.split("\n")
    del header_list[0]
    for x in header_list:
        item = x.split(":")
        image[item[0].lower()] = item[1][:item[1].index("\r")]
    # print("image_dict", image)
    return image