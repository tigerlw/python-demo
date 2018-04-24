# -*- coding: utf-8 -*-

import  AwsCollection as awsc




commitNum = '1,855'

commitNum = commitNum.replace(',','')

print commitNum


msg = '//www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_beauty_sr_pg2_3?ie=UTF8&adId=A04323733TB96LOR735WK&url=https%3A%2F%2Fwww.amazon.com%2FHair-Styling-Clay-Men-Hairstyles%2Fdp%2FB0167HOOEC%2Fref%3Dsr_1_63_sspa%3Fs%3Dbeauty%26ie%3DUTF8%26qid%3D1524474272%26sr%3D1-63-spons%26keywords%3Dhair%2Bwax%26psc%3D1&qualifier=1524474272&id=6719411151089883&widgetName=sp_mtf'

print msg.find('dp%2F')

print msg[192:202]

print "123"+"\n"+"222"

