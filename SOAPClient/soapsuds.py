from suds.client import Client
import xml.etree.ElementTree as ET
import SOAPClient.parseData as parseData

def getWeatherData_suds(longitude,latitude,parameters):
    url="https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl"
    client = Client(url)

    result = client.service.NDFDgen(float(longitude),float(latitude),'time-series','2004-01-01T00:00:00','2021-04-30T00:00:00','e',parameters)

    resultData = parseData.parseData(result,parameters)

    return resultData



