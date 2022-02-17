import http.client
import mimetypes
from codecs import encode
import json
def OCR(image): # input image output text
    conn = http.client.HTTPSConnection("pen-to-print-handwriting-ocr.p.rapidapi.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=session;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("string"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=includeSubScan;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("0"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=srcImg; filename={0}'.format(
        'C:\\Users\\MinaF\\Desktop\\GP\\api\\img.jpeg')))

    fileType = mimetypes.guess_type(image)[0] or 'application/octet-stream'
    dataList.append(encode('Content-Type: {}'.format(fileType)))
    dataList.append(encode(''))

    with open(image, 'rb') as f:  # change here only
        dataList.append(f.read())
    dataList.append(encode('--' + boundary + '--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
        'content-type': 'multipart/form-data; boundary=---011000010111000001101001',
        'x-rapidapi-key': '7e7c65fd3amshe164efe8b6f01f2p14b006jsn300d62bbc02f',
        'x-rapidapi-host': 'pen-to-print-handwriting-ocr.p.rapidapi.com',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/recognize/", payload, headers)
    res = conn.getresponse()
    binData = res.read()
    data = json.loads(binData.decode())
    print(data["value"])
    return data["value"]