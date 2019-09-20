# uses Tabs for indentation
def timelineFormat(names, keys, times,fkt_name="dance",file_name="dance_fkt.py"):
    file = open(r""+file_name,"w+") 
    time_string = "\n\n\tif timestep == 0:\n\t\ttimes = list()"
    # write in File
    str1 = "def " + fkt_name + "(motionProxy, timestep=0, time_start=1):" + "\n\t" + "names = list()\n\tkeys = list()\n"
    file.write(str1)
    for n_i,name in enumerate(names):
        str1 = "\n\tnames.append(\"" + name + "\")" + "\n\tkeys.append(["
        file.write(str1)
        time_string += "\n\t\ttimes.append(" + str(times[n_i]) + ")" + " # " + name
        for k_i, key in enumerate(keys[n_i]):
            if k_i == len(keys[n_i])-1:
                file.write(str(key) + "])")
            else:
                file.write(str(key) + ", ")
                #time_string += str(n_i)
    time_string += "\n\telse:\n\t\ttimes = set_times(names, keys, timestep, time_start)"
    file.write(time_string)
    file.write("\n\n\tmotionProxy.angleInterpolation(names, keys, times, True)\n\t#return names, times, keys")
    file.close()

# uses 4*Space for indentation
def timelineFormat_space(names, keys, times,fkt_name="dance",file_name="dance_fkt.py"):
    file = open(r""+file_name,"w+") 
    time_string = "\n\n    if timestep == 0:\n        times = list()"
    # write in File
    str1 = "def " + fkt_name + "(motionProxy, timestep=0, time_start=1):" + "\n    " + "names = list()\n    keys = list()\n"
    file.write(str1)
    for n_i,name in enumerate(names):
        str1 = "\n    names.append(\"" + name + "\")" + "\n    keys.append(["
        file.write(str1)
        time_string += "\n        times.append(" + str(times[n_i]) + ")" + " # " + name
        for k_i, key in enumerate(keys[n_i]):
            if k_i == len(keys[n_i])-1:
                file.write(str(key) + "])")
            else:
                file.write(str(key) + ", ")
                #time_string += str(n_i)
    time_string += "\n    else:\n        times = set_times(names, keys, timestep, time_start)"
    file.write(time_string)
    file.write("\n\n    motionProxy.angleInterpolation(names, keys, times, True)\n    #return names, times, keys")
    file.close()