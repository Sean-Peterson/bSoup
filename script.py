import urllib
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import time

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
for brandURL in allBrandsURLArray:
    # time.sleep(.333)
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
            # time.sleep(.333)
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


# allPhonesData=[]
# phones = ["https://www.gsmarena.com/apple_iphone_xs_max-9319.php","https://www.gsmarena.com/apple_iphone_6_plus-6665.php","https://www.gsmarena.com/apple_iphone_6-6378.php"]

wb = Workbook()
sheet0 = wb.add_sheet("phones")
sheet1 = wb.add_sheet("phones2")
sheet2 = wb.add_sheet("phones3")
sheet3 = wb.add_sheet("phones4")
sheet4 = wb.add_sheet("phones5")
sheet5 = wb.add_sheet("phones6")
sheet6 = wb.add_sheet("phones7")
sheet7 = wb.add_sheet("phones8")
i = 0
starting = 1
starting2 = 1
starting3 = 1
starting4 = 1
starting5 = 1
starting6 = 1
starting7 = 1
starting8 = 1
counter = 0
headers = ["title", "network", "year", "status", "dimensions", "weight", "build", "sim", "body other", "display type", "display size", "display resolution", "display protection", "display other", "os", "chipset", "cpu", "gpu", "memory slot", "internal memory", "cam 1 modules", "cam 1 features", "cam 1 video", "cam 2 modules", "cam 2 features", "cam 2 video", "optional other", "wlan", "bluetooth", "gps", "nfc", "radio", "usb", "sensors", "features other", "battery description", "battery talk time", "battery music playback", "colors", "models", "price"]
for header in headers:
    row = 0
    column = i
    sheet0.write(row,column,header)
    sheet1.write(row,column,header)
    sheet2.write(row,column,header)
    sheet3.write(row,column,header)
    i+=1
for phone in phones:
    # time.sleep(.333)
    currentPhone = []
    currentPhoneStrings = []
    page=urllib.urlopen(phone)
    soup=BeautifulSoup(page, 'lxml')

    # to find Model, index numbers Name 0
    title=soup.find_all(attrs={"data-spec": "modelname"})
    currentPhone.append(str(title))
    # to find Network, index numbers 1
    network=soup.find_all(attrs={"data-spec": "nettech"})
    currentPhone.append(str(network))
    # to find Launch, index numbers 2,3
    year=soup.find_all(attrs={"data-spec": "year"})
    currentPhone.append(str(year))
    status=soup.find_all(attrs={"data-spec": "status"})
    currentPhone.append(str(status))
    # to find Body, index numbers  4-8
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
    # to find Display, index numbers 9-13
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
    # to find Platform, index numbers 14-17
    os=soup.find_all(attrs={"data-spec": "os"})
    currentPhone.append(str(os))
    chipset=soup.find_all(attrs={"data-spec": "chipset"})
    currentPhone.append(str(chipset))
    cpu=soup.find_all(attrs={"data-spec": "cpu"})
    currentPhone.append(str(cpu))
    gpu=soup.find_all(attrs={"data-spec": "gpu"})
    currentPhone.append(str(gpu))
    # to find Memory, index numbers 18,19
    memoryslot=soup.find_all(attrs={"data-spec": "memoryslot"})
    currentPhone.append(str(memoryslot))
    internalmemory=soup.find_all(attrs={"data-spec": "internalmemory"})
    currentPhone.append(str(internalmemory))
    # to find Main, index numbers Camera 20-22
    cam1modules=soup.find_all(attrs={"data-spec": "cam1modules"})
    currentPhone.append(str(cam1modules))
    cam1features=soup.find_all(attrs={"data-spec": "cam1features"})
    currentPhone.append(str(cam1features))
    cam1video=soup.find_all(attrs={"data-spec": "cam1video"})
    currentPhone.append(str(cam1video))
    # to find Selfie, index numbers Camera 23-25
    cam2modules=soup.find_all(attrs={"data-spec": "cam2modules"})
    currentPhone.append(str(cam2modules))
    cam2features=soup.find_all(attrs={"data-spec": "cam2features"})
    currentPhone.append(str(cam2features))
    cam2video=soup.find_all(attrs={"data-spec": "cam2video"})
    currentPhone.append(str(cam2video))
    # to find Sound, index numbers 26
    # LOUDSPEAKER does not have a data spec
    # 3.5mm jack does not have a data spec
    optionalother=soup.find_all(attrs={"data-spec": "optionalother"})
    currentPhone.append(str(optionalother))
    # to find Comms, index numbers 27-32
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
    # to find Features, index numbers 33-34
    sensors=soup.find_all(attrs={"data-spec": "sensors"})
    currentPhone.append(str(sensors))
    featuresother=soup.find_all(attrs={"data-spec": "featuresother"})
    currentPhone.append(str(featuresother))
    # to find Battery, index numbers 35
    batdescription1=soup.find_all(attrs={"data-spec": "batdescription1"})
    currentPhone.append(str(batdescription1))
    # CHARGING does not have a data spec 36-37
    battalktime1=soup.find_all(attrs={"data-spec": "battalktime1"})
    currentPhone.append(str(battalktime1))
    batmusicplayback1=soup.find_all(attrs={"data-spec": "batmusicplayback1"})
    currentPhone.append(str(batmusicplayback1))
    # to find MISC, index numbers 38-40
    colors=soup.find_all(attrs={"data-spec": "colors"})
    currentPhone.append(str(colors))
    models=soup.find_all(attrs={"data-spec": "models"})
    currentPhone.append(str(models))
    price=soup.find_all(attrs={"data-spec": "price"})
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
    # This is the part of the script to create an XLS using the data

    j = 0
    for spec in currentPhoneStrings:
        counter += 1
        starting += 1
        if counter < 60000:
            print(counter)
            column = j
            row = starting
            sheet0.write(row,column,spec)
            j+= 1
            # starting += 1
        elif counter >= 60000 and counter < 120000:
            print(counter)
            column = j
            row = starting2
            sheet1.write(row,column,spec)
            j+= 1
            # starting2 += 1
        elif counter >= 120000 and counter < 180000:
            print(counter)
            column = j
            row = starting3
            sheet2.write(row,column,spec)
            j+= 1
            # starting3 += 1
        elif counter >= 180000 and counter < 240000:
            print(counter)
            column = j
            row = starting4
            sheet3.write(row,column,spec)
            j+= 1
            # starting4 += 1
        elif counter >= 240000 and counter < 300000:
            print(counter)
            column = j
            row = starting5
            sheet4.write(row,column,spec)
            j+= 1
            # starting5 += 1
        elif counter >= 300000 and counter < 360000:
            print(counter)
            column = j
            row = starting6
            sheet5.write(row,column,spec)
            j+= 1
            # starting6 += 1
        elif counter >= 360000 and counter < 420000:
            print(counter)
            column = j
            row = starting7
            sheet6.write(row,column,spec)
            j+= 1
            # starting7 += 1
        else:
            print(counter)
            column = j
            row = starting8
            sheet7.write(row,column,spec)
            j+= 1
            # starting8 += 1


    # allPhonesData.append(currentPhoneStrings)

# for i in allPhonesData:
#     print(i)


wb.save('GSM_phones_data.xls')
