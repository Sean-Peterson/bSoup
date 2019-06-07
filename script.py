import urllib
urls = ["https://www.gsmarena.com/apple_iphone_xs_max-9319.php","https://www.gsmarena.com/samsung_galaxy_s10+-9535.php"]
from bs4 import BeautifulSoup
allPhones = []
for url in urls:
    currentPhone = []
    currentPhoneStrings = []
    page=urllib.urlopen(url)
    soup=BeautifulSoup(page, 'lxml')

    # to find Model Name 0
    title=soup.find_all(attrs={"data-spec": "modelname"})
    currentPhone.append(str(title))
    # to find Network 1
    network=soup.find_all(attrs={"data-spec": "nettech"})
    currentPhone.append(str(network))
    # to find Launch 2,3
    year=soup.find_all(attrs={"data-spec": "year"})
    currentPhone.append(str(year))
    status=soup.find_all(attrs={"data-spec": "status"})
    currentPhone.append(str(status))
    # to find Body  4-8
    dimensions=soup.find_all(attrs={"data-spec": "dimensions"})
    currentPhone.append(str(dimensions))
    weight=soup.find_all(attrs={"data-spec": "weight"})
    currentPhone.append(str(weight))
    build=soup.find_all(attrs={"data-spec": "build"})
    currentPhone.append(str(build))
    sim=soup.find_all(attrs={"data-spec": "sim"})
    currentPhone.append(str(sim))
    bodyother=soup.find_all(attrs={"data-spec": "bodyother"})
    currentPhone.append(str(bodyother))
    # to find Display 9-13
    displaytype=soup.find_all(attrs={"data-spec": "displaytype"})
    currentPhone.append(str(displaytype))
    displaysize=soup.find_all(attrs={"data-spec": "displaysize"})
    currentPhone.append(str(displaysize))
    displayresolution=soup.find_all(attrs={"data-spec": "displayresolution"})
    currentPhone.append(str(displayresolution))
    displayprotection=soup.find_all(attrs={"data-spec": "displayprotection"})
    currentPhone.append(str(displayprotection))
    displayother=soup.find_all(attrs={"data-spec": "displayother"})
    currentPhone.append(str(displayother))
    # to find Platform 14-17
    os=soup.find_all(attrs={"data-spec": "os"})
    currentPhone.append(str(os))
    chipset=soup.find_all(attrs={"data-spec": "chipset"})
    currentPhone.append(str(chipset))
    cpu=soup.find_all(attrs={"data-spec": "cpu"})
    currentPhone.append(str(cpu))
    gpu=soup.find_all(attrs={"data-spec": "gpu"})
    currentPhone.append(str(gpu))
    # to find Memory 18,19
    memoryslot=soup.find_all(attrs={"data-spec": "memoryslot"})
    currentPhone.append(str(memoryslot))
    internalmemory=soup.find_all(attrs={"data-spec": "internalmemory"})
    currentPhone.append(str(internalmemory))
    # to find Main Camera 20-22
    cam1modules=soup.find_all(attrs={"data-spec": "cam1modules"})
    currentPhone.append(str(cam1modules))
    cam1features=soup.find_all(attrs={"data-spec": "cam1features"})
    currentPhone.append(str(cam1features))
    cam1video=soup.find_all(attrs={"data-spec": "cam1video"})
    currentPhone.append(str(cam1video))
    # to find Selfie Camera 23-25
    cam2modules=soup.find_all(attrs={"data-spec": "cam2modules"})
    currentPhone.append(str(cam2modules))
    cam2features=soup.find_all(attrs={"data-spec": "cam2features"})
    currentPhone.append(str(cam2features))
    cam2video=soup.find_all(attrs={"data-spec": "cam2video"})
    currentPhone.append(str(cam2video))
    # to find Sound 26
    # LOUDSPEAKER does not have a data spec
    # 3.5mm jack does not have a data spec
    optionalother=soup.find_all(attrs={"data-spec": "optionalother"})
    currentPhone.append(str(optionalother))
    # to find Comms 27-32
    wlan=soup.find_all(attrs={"data-spec": "wlan"})
    currentPhone.append(str(wlan))
    bluetooth=soup.find_all(attrs={"data-spec": "bluetooth"})
    currentPhone.append(str(bluetooth))
    gps=soup.find_all(attrs={"data-spec": "gps"})
    currentPhone.append(str(gps))
    nfc=soup.find_all(attrs={"data-spec": "nfc"})
    currentPhone.append(str(nfc))
    radio=soup.find_all(attrs={"data-spec": "radio"})
    currentPhone.append(str(radio))
    usb=soup.find_all(attrs={"data-spec": "usb"})
    currentPhone.append(str(usb))
    # to find Features 33-34
    sensors=soup.find_all(attrs={"data-spec": "sensors"})
    currentPhone.append(str(sensors))
    featuresother=soup.find_all(attrs={"data-spec": "featuresother"})
    currentPhone.append(str(featuresother))
    # to find Battery 35
    batdescription1=soup.find_all(attrs={"data-spec": "batdescription1"})
    currentPhone.append(str(batdescription1))
    # CHARGING does not have a data spec 36-37
    battalktime1=soup.find_all(attrs={"data-spec": "battalktime1"})
    currentPhone.append(str(battalktime1))
    batmusicplayback1=soup.find_all(attrs={"data-spec": "batmusicplayback1"})
    currentPhone.append(str(batmusicplayback1))
    # to find MISC 38-40
    colors=soup.find_all(attrs={"data-spec": "colors"})
    currentPhone.append(str(colors))
    models=soup.find_all(attrs={"data-spec": "models"})
    currentPhone.append(str(models))
    price=soup.find_all(attrs={"data-spec": "price"})
    currentPhone.append(str(price))
    # to find Tests
    # No tests have data specs
    for spec in currentPhone:
        currentString = str(spec)
        if len(currentString) > 5:
            currentString1 = currentString.split('>')
            currentString2 = currentString1[1].split('<')
            currentString3 = currentString2[0]
            currentPhoneStrings.append(currentString3)
        else:
            pass
    allPhones.append(currentPhoneStrings)
print(allPhones)























            # import urllib
            # iphonexsmax="https://www.gsmarena.com/apple_iphone_xs_max-9319.php"
            # page=urllib.urlopen(iphonexsmax)
            # from bs4 import BeautifulSoup
            # soup=BeautifulSoup(page, 'lxml')
            # all_ths=soup.find_all('th')
            # all_tds=soup.find_all('td')
            # nfo_td=soup.find_all('td', class_='nfo')
            # currentPhone = []
            # allInfo = []
            # # to find Model Name 0
            # title=soup.find_all(attrs={"data-spec": "modelname"})
            # currentPhone.append(title)
            # # to find Network 1
            # network=soup.find_all(attrs={"data-spec": "nettech"})
            # currentPhone.append(network)
            # # to find Launch 2,3
            # year=soup.find_all(attrs={"data-spec": "year"})
            # currentPhone.append(year)
            # status=soup.find_all(attrs={"data-spec": "status"})
            # currentPhone.append(status)
            # # to find Body  4-8
            # dimensions=soup.find_all(attrs={"data-spec": "dimensions"})
            # currentPhone.append(dimensions)
            # weight=soup.find_all(attrs={"data-spec": "weight"})
            # currentPhone.append(weight)
            # build=soup.find_all(attrs={"data-spec": "build"})
            # currentPhone.append(build)
            # sim=soup.find_all(attrs={"data-spec": "sim"})
            # currentPhone.append(sim)
            # bodyother=soup.find_all(attrs={"data-spec": "bodyother"})
            # currentPhone.append(bodyother)
            # # to find Display 9-13
            # displaytype=soup.find_all(attrs={"data-spec": "displaytype"})
            # currentPhone.append(displaytype)
            # displaysize=soup.find_all(attrs={"data-spec": "displaysize"})
            # currentPhone.append(displaysize)
            # displayresolution=soup.find_all(attrs={"data-spec": "displayresolution"})
            # currentPhone.append(displayresolution)
            # displayprotection=soup.find_all(attrs={"data-spec": "displayprotection"})
            # currentPhone.append(displayprotection)
            # displayother=soup.find_all(attrs={"data-spec": "displayother"})
            # currentPhone.append(displayother)
            # # to find Platform 14-17
            # os=soup.find_all(attrs={"data-spec": "os"})
            # currentPhone.append(os)
            # chipset=soup.find_all(attrs={"data-spec": "chipset"})
            # currentPhone.append(chipset)
            # cpu=soup.find_all(attrs={"data-spec": "cpu"})
            # currentPhone.append(cpu)
            # gpu=soup.find_all(attrs={"data-spec": "gpu"})
            # currentPhone.append(gpu)
            # # to find Memory 18,19
            # memoryslot=soup.find_all(attrs={"data-spec": "memoryslot"})
            # currentPhone.append(memoryslot)
            # internalmemory=soup.find_all(attrs={"data-spec": "internalmemory"})
            # currentPhone.append(internalmemory)
            # # to find Main Camera 20-22
            # cam1modules=soup.find_all(attrs={"data-spec": "cam1modules"})
            # currentPhone.append(cam1modules)
            # cam1features=soup.find_all(attrs={"data-spec": "cam1features"})
            # currentPhone.append(cam1features)
            # cam1video=soup.find_all(attrs={"data-spec": "cam1video"})
            # currentPhone.append(cam1video)
            # # to find Selfie Camera 23-25
            # cam2modules=soup.find_all(attrs={"data-spec": "cam2modules"})
            # currentPhone.append(cam2modules)
            # cam2features=soup.find_all(attrs={"data-spec": "cam2features"})
            # currentPhone.append(cam2features)
            # cam2video=soup.find_all(attrs={"data-spec": "cam2video"})
            # currentPhone.append(cam2video)
            # # to find Sound 26
            # # LOUDSPEAKER does not have a data spec
            # # 3.5mm jack does not have a data spec
            # optionalother=soup.find_all(attrs={"data-spec": "optionalother"})
            # currentPhone.append(optionalother)
            # # to find Comms 27-32
            # wlan=soup.find_all(attrs={"data-spec": "wlan"})
            # currentPhone.append(wlan)
            # bluetooth=soup.find_all(attrs={"data-spec": "bluetooth"})
            # currentPhone.append(bluetooth)
            # gps=soup.find_all(attrs={"data-spec": "gps"})
            # currentPhone.append(gps)
            # nfc=soup.find_all(attrs={"data-spec": "nfc"})
            # currentPhone.append(nfc)
            # radio=soup.find_all(attrs={"data-spec": "radio"})
            # currentPhone.append(radio)
            # usb=soup.find_all(attrs={"data-spec": "usb"})
            # currentPhone.append(usb)
            # # to find Features 33-34
            # sensors=soup.find_all(attrs={"data-spec": "sensors"})
            # currentPhone.append(sensors)
            # featuresother=soup.find_all(attrs={"data-spec": "featuresother"})
            # currentPhone.append(featuresother)
            # # to find Battery 35
            # batdescription1=soup.find_all(attrs={"data-spec": "batdescription1"})
            # currentPhone.append(batdescription1)
            # # CHARGING does not have a data spec 36-37
            # battalktime1=soup.find_all(attrs={"data-spec": "battalktime1"})
            # currentPhone.append(battalktime1)
            # batmusicplay1=soup.find_all(attrs={"data-spec": "batmusicplay1"})
            # currentPhone.append(batmusicplay1)
            # # to find MISC 38-40
            # colors=soup.find_all(attrs={"data-spec": "colors"})
            # currentPhone.append(colors)
            # models=soup.find_all(attrs={"data-spec": "models"})
            # currentPhone.append(models)
            # price=soup.find_all(attrs={"data-spec": "price"})
            # currentPhone.append(price)
            # # to find Tests
            # # No tests have data specs
            #
            # allInfo.append(currentPhone)
            # tester = str(allInfo[0][39][0])
            # tester1 = tester.split('>')
            # print(tester1)
            # tester2 = tester1[1].split('<')
            # print(tester2)
            # tester3 = tester2[0]

            # print(tester3)
