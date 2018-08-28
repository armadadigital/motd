# http://www2.e-solat.gov.my/zon-waktusolat.php
# https://github.com/SyafiqTermizi/waktu-solat

import solat
import json

print(" Selangor ( GOMBAK,H.SELANGOR,RAWANG, H.LANGAT,SEPANG,PETALING, S.ALAM, DAN KAWASAN YANG SEWAKTU DENGANNYA ) : SGR01 ")
print(" Selangor ( SABAK BERNAM, KUALA SELANGOR, DAN KAWASAN YANG SEWAKTU DENGANNYA ) : SGR02 ")
print(" Selangor ( KLANG, KUALA LANGAT DAN KAWASAN YANG SEWAKTU DENGANNYA ) : SGR05 ")
print(" Putrajaya : SGR04 ")

data = input("Masukkan Zon Solat : ")
pray = solat.prayer(data)

# parsed.load method converts JSON String 
parsed = json.loads(pray)

# print
print json.dumps(parsed, indent=2, sort_keys=True)

