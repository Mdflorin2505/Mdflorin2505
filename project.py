import requests
import json
import uuid
import random
import string
import time
appid = "5417705"
packid = "com.match3d.puzzle.matching.game"
def generate_random_uppercase_chars(length):
    # Generate a random string of uppercase letters with the specified length
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Generate a random 5-character strinhttps://play.google.com/store/apps/details?id=net.bitburst.makecashg of uppercase letters
random_chars = str(generate_random_uppercase_chars(5))
# List of possible Android versions
android_versions = ["4.0.1", "4.1.2", "4.2.2", "4.3.1", "4.4.4", "5.0.2", "5.1.1", "6.0", "6.0.1", "7.0", "7.1.1", "8.0", "8.1", "9.0", "10.0", "11.0", "12.0"]

# List of possible Android devices
android_devices = ["Nexus 5", "Samsung Galaxy S7", "Pixel 2", "OnePlus 6T", "Xiaomi Mi 9", "LG G6"]

# Generate a random IP address in the format "xxx.xxx.xxx.xxx"
ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))

# Choose a random Android version and device
android_version = random.choice(android_versions)
android_device = random.choice(android_devices)

# Construct the user agent string with a random IP address
user_agent = f"Mozilla/5.0 (Linux; Android {android_version}; {android_device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(70, 90)}.0.4430.{random.randint(100, 999)} Mobile Safari/537.36"
user_agent = str(f"{user_agent}")


# Generate a random UUID
random_uuid = str(uuid.uuid4())
random_adid = str(uuid.uuid4())


# Print the generated UUID
# Define the URL and payload
url1 = "https://publisher-config.unityads.unity3d.com/privacy/"+appid+"/state"
payload1 = {
    "platform": "android",
    "idfi": random_uuid,
    "sdkVersionName": "3.4.6",
    "unity.privacy.permissions.all": False,
    "unity.privacy.permissions.gameExp": False,
    "unity.privacy.permissions.ads": False,
    "unity.privacy.permissions.external": False
}

# Define headers
headers1 = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": str(len(json.dumps(payload1)))
}

# Send the POST request
response1 = requests.post(url1, data=json.dumps(payload1), headers=headers1)
import requests
print(response1.status_code)
url2 = "https://publisher-config.unityads.unity3d.com/games/"+appid+"/configuration"
query_parameters2 = {
    "deviceMake": android_device,
    "screenDensity": "300",
    "screenSize": "268435810",
    "idfi": random_uuid,
    "advertisingTrackingId": random_adid,
    "limitAdTracking": "false",
    "installationId": random_uuid,
    "connectionType": "cellular",
    "screenHeight": "1465",
    "screenWidth": "720",
    "usePerPlacementLoad": "false",
    "bundleId": packid,
    "encrypted": "true",
    "rooted": "false",
    "platform": "android",
    "sdkVersion": "3460",
    "osVersion": "11",
    "deviceModel": "SM-"+ random_chars,
    "language": "en_GB",
    "test": "false",
    "first": "true",
    "userLevelFlagDetected": "false"
}

headers2 = {
    "User-Agent": user_agent,
    "Host": "publisher-config.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

response2 = requests.get(url2, params=query_parameters2, headers=headers2)

# Check the response status code and handle the response data as needed

    # Handle the successful response here
print(response2.status_code)
data = response2.json()
token_value = str(data["token"])
properties_value = str(data["properties"])
project_value = str(data["projectId"])
developer_value = str(data["organizationId"])
import time

current_time_millis = int(time.time() * 1000)
import random

# Generate a 15-digit random decimal number
random_number = ''.join([str(random.randint(0, 9)) for _ in range(15)])


import requests
import random

# Generate a random 15-digit even number
random_even_number = random.randrange(10**14, 10**15, 2)


url3 = "https://auction.unityads.unity3d.com/v6/games/"+appid+"/requests?idfi="+random_uuid+"&advertisingTrackingId="+random_adid+"&limitAdTracking=false&deviceModel=SM-"+random_chars+"&platform=android&sdkVersion=3460&stores=google&deviceMake="+android_device+"&screenSize=268435810&screenDensity=300&apiLevel=30&osVersion=11&appInstaller=com.android.vending&screenWidth=720&screenHeight=1465&connectionType=cellular&networkType=13"

headers3 = {
    "Content-Type": "application/json",
    "User-Agent":user_agent ,
    "Host": "auction.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "3966",
}

data3 = {
    "bundleVersion": "1.0",
    "bundleId": packid,
    "coppa": False,
    "language": "en_GB",
    "gameSessionId": random_even_number,
    "timeZone": "GMT+01:00",
    "token": token_value,  
    "legalFramework": "none",
    "agreedOverAgeLimit": "missing",
    "appStartTime": current_time_millis,
    "totalSpace": 114833392,
    "webviewUa": user_agent,
    "dsp": {
        "skOverlay": True,
        "productPage": True
    },
    "experiments": {
        "fullScreenCtaEnabled": True
    },
    "deviceFreeSpace": 74887304,
    "networkOperator": "47002",
    "networkOperatorName": "Cogent Communications",
    "wiredHeadset": False,
    "volume": 15,
    "batteryStatus": 3,
    "requestSignal": "Cv8BChR1bml0eS1hbmRyb2lkLXYzLjQuNhBhGAG6AQIxMcABCMgBoZevEtABnJX2GdgBiA7gAQDoAQHwAQD4AQCAAgGIAgWQAsnU2acGmALO1NmnBqoCQDQyYzRkZDAwZTE2OWE5Zjg2NWQ0OTQ1YWQzZjVlM2JlMTg5ZGIxMTM3M2NmMjliZTcxZjljNmQ2OWVmN2ZhZjiyAig2MWVkMzc3ZTg1ZDM4NmE4ZGZlZTZiODY0YmQ4NWIwYmZhYTVhZjgxugIDMS4wwAIBygISY29tLm15Lm5ld3Byb2plY3Q30gITY29tLmFuZHJvaWQudmVuZGluZ4AD0AWIA7kLkAMBGAIgAw",  # Replace with your requestSignal
    "ext": {
        "seq_num": 0,
        "granular_speed_bucket": "4g",
        "network_metered": True,
        "mobile_device_submodel": "SM-"+ random_chars,
        "prior_user_requests": 0,
        "device_battery_charging": False,
        "device_battery_level": 0.97,
        "android_market_version": "1.com.olleyo.piggy.king.free",
        "prior_click_count": 0,
        "device_incapabilities": "mt",
        "ios_jailbroken": False,
        "iu_sizes": "720x1465|1465x720",
        "ad_load_duration": 0
    },
    "batteryLevel": 0.97,
    "freeMemory": 68668,
    "appVersion": "1.0",
    "versionCode": 1,
    "placements": {
        "Interstitial_Android": {
            "adTypes": ["MRAID", "VIDEO", "DISPLAY"],
            "allowSkip": True,
            "auctionType": "cpm",
            "adFormat": "interstitial",
            "placementType": "bidding"
        },
        "Rewarded_Android": {
            "adTypes": ["MRAID", "VIDEO"],
            "allowSkip": False,
            "auctionType": "cpm",
            "adFormat": "rewarded",
            "placementType": "bidding"
        },
        "Unity_Standard_Placement": {
            "adTypes": ["MRAID", "VIDEO"],
            "allowSkip": True,
            "auctionType": "cpm",
            "adFormat": "interstitial"
        }
    },
    "properties": properties_value,
    "sessionDepth": 0,
    "projectId": project_value,
    "gameSessionCounters": {
        "adRequests": 1,
        "starts": 0,
        "views": 0,
        "startsPerTarget": {},
        "viewsPerTarget": {},
        "latestTargetStarts": {}
    },
    "gdprEnabled": False,
    "optOutEnabled": False,
    "optOutRecorded": False,
    "privacy": {
        "method": "default",
        "firstRequest": True,
        "permissions": {
            "ads": True,
            "external": True,
            "gameExp": True,
            "dataLeavesTerritory": True
        }
    },
    "abGroup": 5,
    "isLoadEnabled": False,
    "omidPartnerName": "Unity3d",
    "omidJSVersion": "1.3.0",
    "srcPayoutType": "cpm",
    "organizationId": developer_value,
    "developerId": int(appid)
}

response3 = requests.post(url3, headers=headers3, json=data3)

# Check the response

print(response3.status_code)
#print(response3.json())
data03 = response3.json()
aunction_value = str(data03['auctionId'][0])

rsmeta_value = str(data03['placementsV2']['Interstitial_Android']['meta'])

media_value = str(data03['placementsV2']['Interstitial_Android']['mediaId'][0])

url_part = data03['trackingTemplates'][0]
extracted_part = str(url_part.split('data=')[1].split('&adType=')[0])

datapts_value = str(data03["placementsV2"]["Interstitial_Android"]["tracking"][0]["events"]["start"]["params"]["datapts"])


eta1 = json.loads(data03['media'][media_value]['content'])["meta"]
meta1 = str(eta1)

video_url = json.loads(data03['media'][media_value]['content'])["trailerPortraitDownloadable"]

import re

deo_value = re.search(r'/assets/([0-9a-f]+)/', video_url).group(1) if '/assets/' in video_url else None
video_value = str(deo_value)


import time




import requests
import json
random_id1 = str(uuid.uuid4())
url6 = "https://publisher-event.unityads.unity3d.com/events/v2/video/video_start/"+appid+"/"+media_value+""

headers6 = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Host": "publisher-event.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "4201"
}

data6 = {
  "eventId": random_id1,
  "auctionId": aunction_value,
  "gameSessionId": random_even_number,
  "campaignId": media_value,
  "seatId": 9000,
  "placementId": "Interstitial_Android",
  "osVersion": "11",
  "sid": "",
  "deviceModel": "SM-"+random_chars,
  "sdkVersion": 3460,
  "bundleId": packid,
  "meta": meta1 ,
  "platform": "android",
  "language": "en_GB",
  "cached": True,
  "cachedOrientation": "portrait",
  "token": token_value,
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True,
      "dataLeavesTerritory": True
    }
  },
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "networkType": 13,
  "connectionType": "cellular",
  "screenWidth": 720,
  "screenHeight": 1465,
  "deviceFreeSpace": 74887304,
  "isLoadEnabled": False,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "loadV5Support": False,
  "rai": False,
  "raiReason": "load",
  "batteryLevel": 0.97,
  "batteryStatus": 3,
  "freeMemory": 53588,
  "adFormat": "interstitial",
  "webview_version": 0,
  "aduid": "Interstitial_Android",
  "apiLevel": 30,
  "deviceMake": android_device,
  "screenDensity": 300,
  "screenSize": 268435810,
  "idfi": random_uuid,
  "advertisingTrackingId": random_adid,
  "limitAdTracking": False,
  "videoOrientation": "portrait",
  "webviewUa": user_agent,
  "placementMeta": rsmeta_value,
  "unityCreativeId": video_value
}

response6 = requests.post(url6, headers=headers6, data=json.dumps(data6))

print(response6.status_code)

import requests
import json
random_id2 = str(uuid.uuid4())
url7 = "https://publisher-event.unityads.unity3d.com/events/v2/video/first_quartile/"+appid+"/"+media_value+""

headers7 = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Host": "publisher-event.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "4201"
}

data7 = {
  "eventId": random_id2,
  "auctionId": aunction_value,
  "gameSessionId": random_even_number,
  "campaignId": media_value,
  "seatId": 9000,
  "placementId": "Interstitial_Android",
  "osVersion": "11",
  "sid": "",
  "deviceModel": "SM-"+random_chars,
  "sdkVersion": 3460,
  "bundleId": packid,
  "meta": meta1 ,
  "platform": "android",
  "language": "en_GB",
  "cached": True,
  "cachedOrientation": "portrait",
  "token": token_value,
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True,
      "dataLeavesTerritory": True
    }
  },
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "networkType": 13,
  "connectionType": "cellular",
  "screenWidth": 720,
  "screenHeight": 1465,
  "deviceFreeSpace": 74887304,
  "isLoadEnabled": False,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "loadV5Support": False,
  "rai": False,
  "raiReason": "load",
  "batteryLevel": 0.97,
  "batteryStatus": 3,
  "freeMemory": 53588,
  "adFormat": "interstitial",
  "webview_version": 0,
  "aduid": "Interstitial_Android",
  "apiLevel": 30,
  "deviceMake": android_device,
  "screenDensity": 300,
  "screenSize": 268435810,
  "idfi": random_uuid,
  "advertisingTrackingId": random_adid,
  "limitAdTracking": False,
  "videoOrientation": "portrait",
  "webviewUa": user_agent,
  "placementMeta": rsmeta_value,
  "unityCreativeId": video_value
}

response7 = requests.post(url7, headers=headers7, data=json.dumps(data7))

print(response7.status_code)

import requests
import json
random_id3 = str(uuid.uuid4())
url8 = "https://publisher-event.unityads.unity3d.com/events/v2/video/midpoint/"+appid+"/"+media_value+""

headers8 = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Host": "publisher-event.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "4201"
}

data8 = {
  "eventId": random_id3,
  "auctionId": aunction_value,
  "gameSessionId": random_even_number,
  "campaignId": media_value,
  "seatId": 9000,
  "placementId": "Interstitial_Android",
  "osVersion": "11",
  "sid": "",
  "deviceModel": "SM-"+random_chars,
  "sdkVersion": 3460,
  "bundleId": packid,
  "meta": meta1 ,
  "platform": "android",
  "language": "en_GB",
  "cached": True,
  "cachedOrientation": "portrait",
  "token": token_value,
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True,
      "dataLeavesTerritory": True
    }
  },
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "networkType": 13,
  "connectionType": "cellular",
  "screenWidth": 720,
  "screenHeight": 1465,
  "deviceFreeSpace": 74887304,
  "isLoadEnabled": False,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "loadV5Support": False,
  "rai": False,
  "raiReason": "load",
  "batteryLevel": 0.97,
  "batteryStatus": 3,
  "freeMemory": 53588,
  "adFormat": "interstitial",
  "webview_version": 0,
  "aduid": "Interstitial_Android",
  "apiLevel": 30,
  "deviceMake": android_device,
  "screenDensity": 300,
  "screenSize": 268435810,
  "idfi": random_uuid,
  "advertisingTrackingId": random_adid,
  "limitAdTracking": False,
  "videoOrientation": "portrait",
  "webviewUa": user_agent,
  "placementMeta": rsmeta_value,
  "unityCreativeId": video_value
}

response8 = requests.post(url8, headers=headers8, data=json.dumps(data8))

print(response8.status_code)

import requests
import json
random_id4 = str(uuid.uuid4())
url9 = "https://publisher-event.unityads.unity3d.com/events/v2/video/third_quartile/"+appid+"/"+media_value+""

headers9 = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Host": "publisher-event.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "4201"
}

data9 = {
  "eventId": random_id4,
  "auctionId": aunction_value,
  "gameSessionId": random_even_number,
  "campaignId": media_value,
  "seatId": 9000,
  "placementId": "Interstitial_Android",
  "osVersion": "11",
  "sid": "",
  "deviceModel": "SM-"+random_chars,
  "sdkVersion": 3460,
  "bundleId": packid,
  "meta": meta1 ,
  "platform": "android",
  "language": "en_GB",
  "cached": True,
  "cachedOrientation": "portrait",
  "token": token_value,
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True,
      "dataLeavesTerritory": True
    }
  },
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "networkType": 13,
  "connectionType": "cellular",
  "screenWidth": 720,
  "screenHeight": 1465,
  "deviceFreeSpace": 74887304,
  "isLoadEnabled": False,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "loadV5Support": False,
  "rai": False,
  "raiReason": "load",
  "batteryLevel": 0.97,
  "batteryStatus": 3,
  "freeMemory": 53588,
  "adFormat": "interstitial",
  "webview_version": 0,
  "aduid": "Interstitial_Android",
  "apiLevel": 30,
  "deviceMake": android_device,
  "screenDensity": 300,
  "screenSize": 268435810,
  "idfi": random_uuid,
  "advertisingTrackingId": random_adid,
  "limitAdTracking": False,
  "videoOrientation": "portrait",
  "webviewUa": user_agent,
  "placementMeta": rsmeta_value,
  "unityCreativeId": video_value
}

response9 = requests.post(url9, headers=headers9, data=json.dumps(data9))

print(response9.status_code)

import requests
import json
random_id5= str(uuid.uuid4())
url10 = "https://publisher-event.unityads.unity3d.com/events/v2/video/video_end/"+appid+"/"+media_value+""

headers10 = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Host": "publisher-event.unityads.unity3d.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "4201"
}

data10 = {
  "eventId": random_id5,
  "auctionId": aunction_value,
  "gameSessionId": random_even_number,
  "campaignId": media_value,
  "seatId": 9000,
  "placementId": "Interstitial_Android",
  "osVersion": "11",
  "sid": "",
  "deviceModel": "SM-"+random_chars,
  "sdkVersion": 3460,
  "bundleId": packid,
  "meta": meta1 ,
  "platform": "android",
  "language": "en_GB",
  "cached": True,
  "cachedOrientation": "portrait",
  "token": token_value,
  "gdprEnabled": False,
  "optOutEnabled": False,
  "optOutRecorded": False,
  "privacy": {
    "method": "default",
    "firstRequest": True,
    "permissions": {
      "ads": True,
      "external": True,
      "gameExp": True,
      "dataLeavesTerritory": True
    }
  },
  "gameSessionCounters": {
    "adRequests": 1,
    "starts": 0,
    "views": 0,
    "startsPerTarget": {},
    "viewsPerTarget": {},
    "latestTargetStarts": {}
  },
  "networkType": 13,
  "connectionType": "cellular",
  "screenWidth": 720,
  "screenHeight": 1465,
  "deviceFreeSpace": 74887304,
  "isLoadEnabled": False,
  "legalFramework": "none",
  "agreedOverAgeLimit": "missing",
  "loadV5Support": False,
  "rai": False,
  "raiReason": "load",
  "batteryLevel": 0.97,
  "batteryStatus": 3,
  "freeMemory": 53588,
  "adFormat": "interstitial",
  "webview_version": 0,
  "aduid": "Interstitial_Android",
  "apiLevel": 30,
  "deviceMake": android_device,
  "screenDensity": 300,
  "screenSize": 268435810,
  "idfi": random_uuid,
  "advertisingTrackingId": random_adid,
  "limitAdTracking": False,
  "videoOrientation": "portrait",
  "webviewUa": user_agent,
  "placementMeta": rsmeta_value,
  "unityCreativeId": video_value
}

response10 = requests.post(url10, headers=headers10, data=json.dumps(data10))

print(response10.status_code)
time.sleep(1)

