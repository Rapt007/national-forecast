from zeep import Client
from zeep import xsd
import datetime

def getWeatherData_zeep(longitude,latitude,maxt,mint,dew,waveh):
    url="https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl"
    client = Client(url)

    # print(client)
    # print(client.get_type('tns:weatherParametersType'))
    startDate = datetime.datetime('2004-01-01T00:00:00')
    endDate = datetime.datetime('2021-04-30T00:00:00')

    m1 = False
    m2 = False
    m3 = False
    m4 = False
    if maxt == 'true':
        m1 = True
    if mint == 'true':
        m2 = True
    if dew == 'true':
        m3 = True
    if waveh == 'true':
        m4 = True


    parameter = {'maxt':m1,'mint':m2,'temp':False,'dew':m3,'pop12':False,'qpf':False,'sky':False,'snow':False,'wspd':False,'wdir':False
                 ,'wx':False,'waveh':m4,'icons':False,'rh':False,'appt':False,'incw34':False,'incw50':False,'incw64':False,'cumw34':False
                 ,'cumw50':False,'cumw64':False,'critfireo':False,'dryfireo':False,'conhazo':False,'ptornado':False,'phail':False,'ptstmwinds':False
                 ,'pxtornado':False,'pxhail':False,'pxtstmwinds':False,'ptotsvrtstm':False,'pxtotsvrtstm':False,'tmpabv14d':False,'tmpblw14d':False
                 ,'tmpabv30d':False,'tmpblw30d':False,'tmpabv90d':False,'tmpblw90d':False,'prcpabv14d':False,'prcpblw14d':False,'prcpabv30d':False
                 ,'prcpblw30d':False,'prcpabv90d':False,'prcpblw90d':False,'precipa_r':False,'sky_r':False,'td_r':False,'temp_r':False,'wdir_r':False
                 ,'wspd_r':False,'wwa':False,'wgust':False,'iceaccum':False,'maxrh':False,'minrh':False}

    result = client.service.NDFDgen(float(longitude),float(latitude),'time-series',startDate,endDate,'e',parameter)
    return result