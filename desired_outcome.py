import pandas


rX = [
    {
        "ID_x": "62bf",
        "HOST_NM": "philip",
        "IP_ADDRESS_x": "192.168.1.115",
        "SERIAL_x": "12345",
        "ID_y": "32",
        "IP_ADDRESS_y": "192.168.1.115",
        "COST": "36.78",
        "PURCHASE_DATE": "2018-05-05",
        "ID": "2",
        "IP_ADDRESS": "192.168.1.115",
        "SERIAL_y": "12345",
        "OS": "Debian 11 Linux",
    },
    {
        "ID_x": "3a73",
        "HOST_NM": "vic",
        "IP_ADDRESS_x": "192.168.1.145",
        "SERIAL_x": "17B0P",
        "ID_y": "33",
        "IP_ADDRESS_y": "192.168.1.145",
        "COST": "749.64",
        "PURCHASE_DATE": "2018-07-25",
        "ID": "3",
        "IP_ADDRESS": "192.168.1.145",
        "SERIAL_y": "17B0P",
        "OS": "DSM 7.1-42661",
    },
    {
        "ID_x": "4237",
        "HOST_NM": "BILL",
        "IP_ADDRESS_x": "192.168.1.99",
        "SERIAL_x": "38174",
        "ID_y": "31",
        "IP_ADDRESS_y": "192.168.1.99",
        "COST": "3584.83",
        "PURCHASE_DATE": "2018-03-15",
        "ID": "1",
        "IP_ADDRESS": "192.168.1.99",
        "SERIAL_y": "38174",
        "OS": "Windows 10 LTSC",
    },
    {
        "ID_x": "3027",
        "HOST_NM": "tim",
        "IP_ADDRESS_x": "192.168.1.96,192.168.1.100",
        "SERIAL_x": "C02G7",
        "ID_y": "34",
        "IP_ADDRESS_y": "192.168.1.96,192.168.1.100",
        "COST": "1289.00",
        "PURCHASE_DATE": "2021-10-13",
        "ID": "4",
        "IP_ADDRESS": "192.168.1.96,192.168.1.100",
        "SERIAL_y": "C02G7",
        "OS": "macOS Monterey 12.4",
    },
]

df = pandas.DataFrame(rX)
print(df)
