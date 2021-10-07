import pprint
import re
import time

import html2text
from textblob import TextBlob
import requests
import os

# data_path="files/"
# files=[i.name for i in os.scandir(data_path)]
beds = "https://www.covidbedmbmc.in/HospitalInfo/show"  # "https://coronabeds.jantasamvad.org/beds.html"
icu_beds = "https://coronabeds.jantasamvad.org/all-covid-icu-beds.html"


def bed_availability(beds):
    data = html2text.html2text(requests.get(beds).text)
    time.sleep(2)
    blob = TextBlob(data)
    # print(blob)
    x = blob.split("####")
    # print(x)
    j = [i for i in x if i.startswith(" **")]
    extract_out = []
    for hospital in j:
        try:
            contact = re.findall("[0-9]{10}", hospital)[0]
        except IndexError:
            contact = None
        hospital_name = hospital.split("\n")[0].replace('*', '')
        vacant_index = hospital.split("\n").index('Vacant')
        icu_vacant_index = hospital.split("\n").index('ICU Vacant')
        non_icu_vacant_index = hospital.split("\n").index('Non ICU Vacant')
        # print(vacant_index,icu_vacant_index,non_icu_vacant_index)

        vacant = hospital.split("\n")[vacant_index - 2].replace('*', '').replace(' ', '').replace('_', '')
        icu_vacant = hospital.split("\n")[icu_vacant_index - 2].replace('*', '').replace(' ', '').replace('_', '')
        non_icu_vacant = hospital.split("\n")[non_icu_vacant_index - 2].replace('*', '').replace(' ', '').replace('_',
                                                                                                                  '')
        # print(vacant,icu_vacant,non_icu_vacant)

        extract_out.append((hospital_name, contact, int(vacant), int(icu_vacant), int(non_icu_vacant)))
    return extract_out