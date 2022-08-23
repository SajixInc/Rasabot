import smtplib

import requests


def Dose_Availability_Lon_Lat(Lattitude,Longitude):
    api="https://cdn-api.co-vin.in/api/v2/appointment/centers/public/findByLatLong?lat={}&long={}".format(Lattitude,Longitude)
    return main_task1(api)

def Dose_Availability_District(district_id,date):
    api="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_id,date)
    return main_task(api)

def Dose_Availability_Pincode(pincode, date):
    api ="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode,date)

    return main_task(api)



def main_task1(api):
    response=requests.get(api)
    data=response.json()['centers']
    output="*"*30
    # print(data)
    for area in data:
        # if area['available_capacity']>0:
            # for (field,value) in area.items():
            #     print(field,':',value)
            # else:
            # print(area["pincode"])
            output+="  Hospital Name:" + area['name'] + "*"*30 +"\n"
            output+='''\
pincode: {}
state_name: {}
district_name : {}
block_name : {}

'''.format(area['pincode'],area['state_name'],area['district_name'],
                             area['block_name'])
            output+="*"*30
    return output



def main_task(api):
    response=requests.get(api)
    data=response.json()['sessions']
    output="*"*30
    for area in data:
        if area['available_capacity']>0:
            # for (field,value) in area.items():
            #     print(field,':',value)
            # else:
            output+="  Hospital Name:" + area['name'] + "*"*30 +"\n"
            output+='''\
Address: {}
Pincode: {}
available_capacity_dose1 : {}
available_capacity_dose2 : {}
available_capacity : {}
min_age_limit: {}
Time Slots: {}

'''.format(area['address'],area['pincode'],area['available_capacity_dose1'],area['available_capacity_dose2'],
                             area['available_capacity'],area['min_age_limit'],str(area['slots'])[1:-1])
            output+="*"*30
    return output

def send_email(email,message):
    host = "smtp.gmail.com"
    port = 587

    connection=smtplib.SMTP(host,port)
    connection.starttls()

    username="innovateyourself2build@gmail.com"
    with open("creds.txt") as file:
        password=file.read()
    connection.login(username,password)

    receiver=email
    subject="Test Email"
    # message="This is a test email for demo. Ashish Saini"

    body='''\
From: {}
Subject:{}

{}'''.format(username,subject,message)

    connection.sendmail(username,receiver,body)
    connection.quit()

# Dose_Availability_Pincode("530051","31-03-2021")

# send_email("innovateyourself2build@gmail.com",'test mail')
print(Dose_Availability_District(512,"08-08-2022"))
# print(Dose_Availability_Lon_Lat(17.68,83.21))


# def prime_number(num):
#     flag = False
#
#     # prime numbers are greater than 1
#     if num > 1:
#         # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#                 # if factor is found, set flag to True
#                 flag = True
#                 # break out of loop
#                 break
#     elif num == 2:
#         Flag = True
#     # check if flag is True
#     if flag:
#         return False
#     else:
#         return True
#
#
# def prime_numbers(l, n):
#     x = []
#
#     for i in range(l, n-1 ):
#         if prime_number(i) == True:
#             x.append(i)
#             # print(i)
#             break
#     # print('*****')
#
#     for j in range(n-1, l-1,-1):
#         # print(j)
#         if prime_number(j) == True:
#             x.append(j)
#             break
#     return x
#
#
# def out(t):
#     l, r = input().split()
#     # x = set([prime(i) for i in range(int(l), int(r) + 1) if i != None]).difference({None})
#     # tuple(filter(prime, range(int(l), int(r) + 1)))
#     # print(x)
#     # print(max(x), min(x))
#     x = prime_numbers(int(l), int(r) + 1)
#     # print(x)
#     print(max(x) - min(x)) if len(x) >= 2 else print(0) if len(x) == 1 else print(-1)
#
#
# def main():
#     t = int(input())
#     if t >= 1 and t <= 10:
#         tuple(map(out, range(t)))
#
#
# # print(prime(999997))
# main()