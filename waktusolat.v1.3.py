# http://www2.e-solat.gov.my/zon-waktusolat.php
# https://github.com/SyafiqTermizi/waktu-solat

import solat
import re


print(" Selangor ( GOMBAK,H.SELANGOR,RAWANG, H.LANGAT,SEPANG,PETALING, S.ALAM, DAN KAWASAN YANG SEWAKTU DENGANNYA ) : SGR01 ")
print(" Selangor ( SABAK BERNAM, KUALA SELANGOR, DAN KAWASAN YANG SEWAKTU DENGANNYA ) : SGR02 ")
print(" Selangor ( KLANG, KUALA LANGAT DAN KAWASAN YANG SEWAKTU DENGANNYA ) : SGR05 ")
print(" Putrajaya : SGR04 ")

data = input("Masukkan Zon Solat : ")
pray = solat.prayer(data)

# zon 	= list(pray[0])
# imsak = list(pray[1])
# print(imsak)


# Print dalam loop
for waktuSolat in pray:
	print(waktuSolat, end="\n")
