# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:24:07 2022

@author: Benjamin Culver
"""

#script returns user demographics with names starting with A, B, or C

import requests
import requests_cache
import csv

#establishes cache for API requests
requests_cache.install_cache('demographics', backend='sqlite', expire_after=600)

#header from API documentation here https://apidocs.healthjump.com/#usage
header_auth={'Content-Type':'application/x-www-form-urlencoded'}
data_auth={'email':'sandbox@healthjump.com', 'password':'R-%Sx?qP%+RN69CS'}

#get token
response_auth=requests.post('https://api.healthjump.com/authenticate',  headers=header_auth, data=data_auth)  
token=response_auth.json()


#get demographics
headers={"Authorization": "Bearer {}".format(token['token']), 'Version':'3.0', 'secretkey':'yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g', 'params':'first_name starts with A or B or C'}
demo_url='https://api.healthjump.com/hjdw/SBOX02/demographic'
response=requests.get(demo_url, headers=headers)

if (response.status_code==200):
    'Request made successfully!'
else:
    'Error ' +str(response.status_code)+' with request!'

if response.from_cache:
    print('Request retrieved from cache')
    
results=response.json()


#Wasn't able to determine how to filter names from the Healthjump API docs (only based on ID/date), so I did it post-request.
filtered_results=[]

for result in results['data']:
    if result['first_name'] in ['Patient_A', 'Patient_B', 'Patient_C']:
        filtered_results.append(result)
        
#Loops through pagination until next_page_url becomes NoneType, in this example the sample API only returns 24 items so loop never executes
while(results['next_page_url']):
    response=requests.get(results['next_page_url'], headers=headers)
    results=response.json()
    for result in results['data']:
        if result['first_name'] in ['Patient_A', 'Patient_B', 'Patient_C']:
            filtered_results.append(result)
            
#write list of returned dicts to a csv file
output=open('demographics_ABC.csv', "w")
dict_write=csv.DictWriter(output, filtered_results[0].keys())
dict_write.writeheader()
dict_write.writerows(filtered_results)
output.close()
