import urllib
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook

allBrandsURL = "https://www.gsmarena.com/makers.php3"
page=urllib.urlopen(allBrandsURL)
soup=BeautifulSoup(page, 'lxml')
allPhoneBrands=soup.find_all('td')
# this is an array that has all of the brands included in the GSMarena DB. This array will be used to append to gsmarena.com/
allBrandsURLArray = []

for brand in allPhoneBrands:
        currentBrand = str(brand)
        if len(currentBrand) > 5:
            currentBrand1 = currentBrand.split('"')
            # print(currentBrand1)
            currentBrand2 = currentBrand1[1].split('">')
            currentBrand3 = currentBrand2[0]
            # print(currentBrand3)
            # currentBrandURL.append(currentBrand3)

            # currentBrand2 = currentBrand1[1].split('">')
            # currentBrand3 = currentBrand2[0]
            # currentBrandURL.append(currentBrand3)
        else:
            pass
        allBrandsURLArray.append(currentBrand3)
# print(allBrandsURLArray)

allBrandsPages = []
phones = []
# The below line should be commented out in order to run the whole program.
allBrandsURLArray = ["apple-phones-48.php"]
for brandURL in allBrandsURLArray:
    #Before we get all the links from each main page, we need to figure out how to get every page. This is found in the pages links at the bottom of the page.
    currentBrandName = str(brandURL).split("-")
    print(currentBrandName[0])
    currentBrand = []
    currentBrandStrings = []
    page=urllib.urlopen("https://www.gsmarena.com/"+str(brandURL))
    soup=BeautifulSoup(page, 'lxml')

    newBrandsURLArray = []
    totalBrandPages = soup.find(class_="nav-pages")
    li=soup.find_all('li')
    for i in li:
        string = str(i)
        string1 = string.split('href="')
        string2 = string1[1].split('"')
        if currentBrandName[0]+"_" not in string2[0]:
            pass
        else:
            phones.append("https://www.gsmarena.com/"+string2[0])
    if totalBrandPages is not None:
        for i in totalBrandPages.descendants:
            string = str(i)
            if currentBrandName[0]+"-phones" not in string:
                pass
            else:
                string1 = string.split('="')
                # print(string1[1])
                string2 = string1[1].split('">')
                print(string2[0])
                page=urllib.urlopen("https://www.gsmarena.com/"+str(string2[0]))
                soup=BeautifulSoup(page, 'lxml')
                li=soup.find_all('li')
                for i in li:
                    string = str(i)
                    string1 = string.split('href="')
                    string2 = string1[1].split('"')
                    if currentBrandName[0]+"_" not in string2[0]:
                        pass
                    else:
                        phones.append("https://www.gsmarena.com/"+string2[0])

# for brandURL in newBrandsURLArray:
#     currentBrandName = str(brandURL).split("-")
#     print(currentBrandName[0])
#     currentBrand = []
#     currentBrandStrings = []
#     page=urllib.urlopen("https://www.gsmarena.com/"+str(brandURL))
#     soup=BeautifulSoup(page, 'lxml')

# for i in phones:
#     print(i)
    #Now we need to get every page for every manufacturer.









        #Need to figure out how to get all the links from the "makers" data. Need to either push all of these to a div or find a better way to just grab the links from the a tags in the makers div.

allPhonesData=[]
# phones = ["https://www.gsmarena.com/apple_iphone_xs_max-9319.php","https://www.gsmarena.com/apple_iphone_6_plus-6665.php","https://www.gsmarena.com/apple_iphone_6-6378.php"]
for phone in phones:
    currentPhone = []
    currentPhoneStrings = []
    page=urllib.urlopen(phone)
    soup=BeautifulSoup(page, 'lxml')

    # to find Model, index numbers Name 0
    title=soup.find_all(attrs={"data-spec": "modelname"})
    currentPhone.append("title")
    currentPhone.append(str(title))
    # to find Network, index numbers 1
    network=soup.find_all(attrs={"data-spec": "nettech"})
    currentPhone.append("network")
    currentPhone.append(str(network))
    # to find Launch, index numbers 2,3
    year=soup.find_all(attrs={"data-spec": "year"})
    currentPhone.append("year")
    currentPhone.append(str(year))
    status=soup.find_all(attrs={"data-spec": "status"})
    currentPhone.append("status")
    currentPhone.append(str(status))
    # to find Body, index numbers  4-8
    dimensions=soup.find_all(attrs={"data-spec": "dimensions"})
    currentPhone.append("dimensions")
    currentPhone.append(str(dimensions))
    weight=soup.find_all(attrs={"data-spec": "weight"})
    currentPhone.append("weight")
    currentPhone.append(str(weight))
    build=soup.find_all(attrs={"data-spec": "build"})
    currentPhone.append("build")
    currentPhone.append(str(build))
    sim=soup.find_all(attrs={"data-spec": "sim"})
    currentPhone.append("sim")
    currentPhone.append(str(sim))
    bodyother=soup.find_all(attrs={"data-spec": "bodyother"})
    currentPhone.append("bodyother")
    currentPhone.append(str(bodyother))
    # to find Display, index numbers 9-13
    displaytype=soup.find_all(attrs={"data-spec": "displaytype"})
    currentPhone.append("displaytype")
    currentPhone.append(str(displaytype))
    displaysize=soup.find_all(attrs={"data-spec": "displaysize"})
    currentPhone.append("displaysize")
    currentPhone.append(str(displaysize))
    displayresolution=soup.find_all(attrs={"data-spec": "displayresolution"})
    currentPhone.append("displayresolution")
    currentPhone.append(str(displayresolution))
    displayprotection=soup.find_all(attrs={"data-spec": "displayprotection"})
    currentPhone.append("displayprotection")
    currentPhone.append(str(displayprotection))
    displayother=soup.find_all(attrs={"data-spec": "displayother"})
    currentPhone.append("displayother")
    currentPhone.append(str(displayother))
    # to find Platform, index numbers 14-17
    os=soup.find_all(attrs={"data-spec": "os"})
    currentPhone.append("os")
    currentPhone.append(str(os))
    chipset=soup.find_all(attrs={"data-spec": "chipset"})
    currentPhone.append("chipset")
    currentPhone.append(str(chipset))
    cpu=soup.find_all(attrs={"data-spec": "cpu"})
    currentPhone.append("cpu")
    currentPhone.append(str(cpu))
    gpu=soup.find_all(attrs={"data-spec": "gpu"})
    currentPhone.append("gpu")
    currentPhone.append(str(gpu))
    # to find Memory, index numbers 18,19
    memoryslot=soup.find_all(attrs={"data-spec": "memoryslot"})
    currentPhone.append("memoryslot")
    currentPhone.append(str(memoryslot))
    internalmemory=soup.find_all(attrs={"data-spec": "internalmemory"})
    currentPhone.append("internalmemory")
    currentPhone.append(str(internalmemory))
    # to find Main, index numbers Camera 20-22
    cam1modules=soup.find_all(attrs={"data-spec": "cam1modules"})
    currentPhone.append("cam1modules")
    currentPhone.append(str(cam1modules))
    cam1features=soup.find_all(attrs={"data-spec": "cam1features"})
    currentPhone.append("cam1features")
    currentPhone.append(str(cam1features))
    cam1video=soup.find_all(attrs={"data-spec": "cam1video"})
    currentPhone.append("cam1video")
    currentPhone.append(str(cam1video))
    # to find Selfie, index numbers Camera 23-25
    cam2modules=soup.find_all(attrs={"data-spec": "cam2modules"})
    currentPhone.append("cam2modules")
    currentPhone.append(str(cam2modules))
    cam2features=soup.find_all(attrs={"data-spec": "cam2features"})
    currentPhone.append("cam2features")
    currentPhone.append(str(cam2features))
    cam2video=soup.find_all(attrs={"data-spec": "cam2video"})
    currentPhone.append(str(cam2video))
    currentPhone.append("cam2video")
    # to find Sound, index numbers 26
    # LOUDSPEAKER does not have a data spec
    # 3.5mm jack does not have a data spec
    optionalother=soup.find_all(attrs={"data-spec": "optionalother"})
    currentPhone.append("optionalother")
    currentPhone.append(str(optionalother))
    # to find Comms, index numbers 27-32
    wlan=soup.find_all(attrs={"data-spec": "wlan"})
    currentPhone.append("wlan")
    currentPhone.append(str(wlan))
    bluetooth=soup.find_all(attrs={"data-spec": "bluetooth"})
    currentPhone.append("bluetooth")
    currentPhone.append(str(bluetooth))
    gps=soup.find_all(attrs={"data-spec": "gps"})
    currentPhone.append("gps")
    currentPhone.append(str(gps))
    nfc=soup.find_all(attrs={"data-spec": "nfc"})
    currentPhone.append("nfc")
    currentPhone.append(str(nfc))
    radio=soup.find_all(attrs={"data-spec": "radio"})
    currentPhone.append("radio")
    currentPhone.append(str(radio))
    usb=soup.find_all(attrs={"data-spec": "usb"})
    currentPhone.append("usb")
    currentPhone.append(str(usb))
    # to find Features, index numbers 33-34
    sensors=soup.find_all(attrs={"data-spec": "sensors"})
    currentPhone.append("sensors")
    currentPhone.append(str(sensors))
    featuresother=soup.find_all(attrs={"data-spec": "featuresother"})
    currentPhone.append("featuresother")
    currentPhone.append(str(featuresother))
    # to find Battery, index numbers 35
    batdescription1=soup.find_all(attrs={"data-spec": "batdescription1"})
    currentPhone.append("batdescription1")
    currentPhone.append(str(batdescription1))
    # CHARGING does not have a data spec 36-37
    battalktime1=soup.find_all(attrs={"data-spec": "battalktime1"})
    currentPhone.append("battalktime1")
    currentPhone.append(str(battalktime1))
    batmusicplayback1=soup.find_all(attrs={"data-spec": "batmusicplayback1"})
    currentPhone.append("batmusicplayback1")
    currentPhone.append(str(batmusicplayback1))
    # to find MISC, index numbers 38-40
    colors=soup.find_all(attrs={"data-spec": "colors"})
    currentPhone.append("colors")
    currentPhone.append(str(colors))
    models=soup.find_all(attrs={"data-spec": "models"})
    currentPhone.append("models")
    currentPhone.append(str(models))
    price=soup.find_all(attrs={"data-spec": "price"})
    currentPhone.append("price")
    currentPhone.append(str(price))
    # to find Tests, index numbers
    # No tests have data specs
    for spec in currentPhone:
        currentString = str(spec)
        # print(currentString)
        if ">" in currentString:
            currentString1 = currentString.split('>')
            currentString2 = currentString1[1].split('<')
            currentString3 = currentString2[0]
            currentPhoneStrings.append(str(currentString3))
        else:
            currentPhoneStrings.append(str(currentString))
    allPhonesData.append(currentPhoneStrings)

# for i in allPhonesData:
#     print(i)


# This is the part of the script to create an XLS using the data
wb = Workbook()
sheet = wb.add_sheet("apple")


first = 0
second = 1
for phone in allPhonesData:
    j = 0
    flipper = 0
    for spec in phone:
        column = j
        if flipper == 0:
            row = first
            sheet.write(row,column,spec)
            flipper = 1
        else:
            row = second
            sheet.write(row,column,spec)
            j+= 1
            flipper = 0
    first += 2
    second += 2
wb.save('GSM_phones_data.xls')






























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
            # # to find Model, index numbers Name 0
            # title=soup.find_all(attrs={"data-spec": "modelname"})
            # currentPhone.append(title)
            # # to find Network, index numbers 1
            # network=soup.find_all(attrs={"data-spec": "nettech"})
            # currentPhone.append(network)
            # # to find Launch, index numbers 2,3
            # year=soup.find_all(attrs={"data-spec": "year"})
            # currentPhone.append(year)
            # status=soup.find_all(attrs={"data-spec": "status"})
            # currentPhone.append(status)
            # # to find Body, index numbers  4-8
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
            # # to find Display, index numbers 9-13
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
            # # to find Platform, index numbers 14-17
            # os=soup.find_all(attrs={"data-spec": "os"})
            # currentPhone.append(os)
            # chipset=soup.find_all(attrs={"data-spec": "chipset"})
            # currentPhone.append(chipset)
            # cpu=soup.find_all(attrs={"data-spec": "cpu"})
            # currentPhone.append(cpu)
            # gpu=soup.find_all(attrs={"data-spec": "gpu"})
            # currentPhone.append(gpu)
            # # to find Memory, index numbers 18,19
            # memoryslot=soup.find_all(attrs={"data-spec": "memoryslot"})
            # currentPhone.append(memoryslot)
            # internalmemory=soup.find_all(attrs={"data-spec": "internalmemory"})
            # currentPhone.append(internalmemory)
            # # to find Main, index numbers Camera 20-22
            # cam1modules=soup.find_all(attrs={"data-spec": "cam1modules"})
            # currentPhone.append(cam1modules)
            # cam1features=soup.find_all(attrs={"data-spec": "cam1features"})
            # currentPhone.append(cam1features)
            # cam1video=soup.find_all(attrs={"data-spec": "cam1video"})
            # currentPhone.append(cam1video)
            # # to find Selfie, index numbers Camera 23-25
            # cam2modules=soup.find_all(attrs={"data-spec": "cam2modules"})
            # currentPhone.append(cam2modules)
            # cam2features=soup.find_all(attrs={"data-spec": "cam2features"})
            # currentPhone.append(cam2features)
            # cam2video=soup.find_all(attrs={"data-spec": "cam2video"})
            # currentPhone.append(cam2video)
            # # to find Sound, index numbers 26
            # # LOUDSPEAKER does not have a data spec
            # # 3.5mm jack does not have a data spec
            # optionalother=soup.find_all(attrs={"data-spec": "optionalother"})
            # currentPhone.append(optionalother)
            # # to find Comms, index numbers 27-32
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
            # # to find Features, index numbers 33-34
            # sensors=soup.find_all(attrs={"data-spec": "sensors"})
            # currentPhone.append(sensors)
            # featuresother=soup.find_all(attrs={"data-spec": "featuresother"})
            # currentPhone.append(featuresother)
            # # to find Battery, index numbers 35
            # batdescription1=soup.find_all(attrs={"data-spec": "batdescription1"})
            # currentPhone.append(batdescription1)
            # # CHARGING does not have a data spec 36-37
            # battalktime1=soup.find_all(attrs={"data-spec": "battalktime1"})
            # currentPhone.append(battalktime1)
            # batmusicplay1=soup.find_all(attrs={"data-spec": "batmusicplay1"})
            # currentPhone.append(batmusicplay1)
            # # to find MISC, index numbers 38-40
            # colors=soup.find_all(attrs={"data-spec": "colors"})
            # currentPhone.append(colors)
            # models=soup.find_all(attrs={"data-spec": "models"})
            # currentPhone.append(models)
            # price=soup.find_all(attrs={"data-spec": "price"})
            # currentPhone.append(price)
            # # to find Tests, index numbers
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
