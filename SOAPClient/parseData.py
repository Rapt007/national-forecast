import xml.etree.ElementTree as ET

def parseData(dataStr,parameters1):
    root = ET.fromstring(result)

    # print root
    maxtemp = []
    mintemp = []
    dewtemp = []
    winddirection = []
    for child in root:
        if 'data' in repr(child):
            for parameters in child:
                if 'parameters' in repr(parameters):
                    for value in parameters:
                        if 'temperature' in repr(value):
                            if m1 == True:
                                if value.attrib['type'] == 'maximum':
                                    for newvalue in value:
                                        if 'value' in repr(newvalue):
                                            maxtemp.append(newvalue.text)
                            if m2 == True:
                                if value.attrib['type'] == 'minimum':
                                    for newvalue in value:
                                        if 'value' in repr(newvalue):
                                            mintemp.append(newvalue.text)

                            if m3 == True:
                                if value.attrib['type'] == 'dew point':
                                    for newvalue in value:
                                        if 'value' in repr(newvalue):
                                            dewtemp.append(newvalue.text)

                                            #                             if m4 == True:
                                            #                             if value.attrib=={'units': 'Fahrenheit', 'type': 'hourly', 'time-layout': 'k-p3h-n37-3'}:
                                            #                                 for newvalue in value:
                                            #                                     if 'value' in repr(newvalue):
                                            #                                         temp.append(newvalue.text)


                        elif 'direction' in repr(value):
                            if m4 == True:
                                for direction in value:
                                    if 'value' in repr(direction):
                                        #                                 for newvalue in direction:
                                        winddirection.append(direction.text)

    print winddirection
    print dewtemp
    print maxtemp
    print mintemp

    parsedData = {}
    parsedData['maxt'] = maxtemp
    parsedData['mint'] = mintemp
    parsedData['dew'] = dewtemp
    parsedData['wdir'] = temp

    return parsedData
