# Prettify JSON

The module takes raw single-line json-file and returns it in convinient visual form.

# Quickstart

Clone this repo and you are ready!

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>
[
    {                                                                                                                                                                                                                  
        "Cells": {                                                                                                                                                                                                     
            "Address": "Ленинградский проспект, дом 78, корпус 1",                                                                                                                                                     
            "AdmArea": "Северный административный округ",                                                                                                                                                              
            "ClarificationOfWorkingHours": null,                                                                                                                                                                       
            "District": "район Аэропорт",                                                                                                                                                                              
            "IsNetObject": "нет",                                                                                                                                                                                      
            "Name": "Магазин FANAGORIA",                                                                                                                                                                               
            "OperatingCompany": null,                                                                                                                                                                                  
            "PublicPhone": [                                                                                                                                                                                           
                {                                                                                                                                                                                                      
                    "PublicPhone": "(985) 704-07-14"                                                                                                                                                                   
                }                                                                                                                                                                                                      
            ],                                                                                                                                                                                                         
            "TypeService": "реализация продовольственных товаров",                                                                                                                                                     
            "WorkingHours": [                                                                                                                                                                                          
                {                                                                                                                                                                                                      
                    "DayOfWeek": "понедельник",                                                                                                                                                                        
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                },                                                                                                                                                                                                     
                {                                                                                                                                                                                                      
                    "DayOfWeek": "вторник",                                                                                                                                                                            
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                },                                                                                                                                                                                                     
                {                                                                                                                                                                                                      
                    "DayOfWeek": "среда",                                                                                                                                                                              
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                },                                                                                                                                                                                                     
                {                                                                                                                                                                                                      
                    "DayOfWeek": "четверг",                                                                                                                                                                            
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                },                                                                                                                                                                                                     
                {                                                                                                                                                                                                      
                    "DayOfWeek": "пятница",                                                                                                                                                                            
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                },                                                                                                                                                                                                     
                {                                                                                                                                                                                                      
                    "DayOfWeek": "суббота",                                                                                                                                                                            
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                },                                                                                                                                                                                                     
                {                                                                                                                                                                                                      
                    "DayOfWeek": "воскресенье",                                                                                                                                                                        
                    "Hours": "09:00-23:00"                                                                                                                                                                             
                }                                                                                                                                                                                                      
            ],
            "geoData": {                                                                                                                                                                                               
                "coordinates": [                                                                                                                                                                                       
                    37.51327551663874,                                                                                                                                                                                 
                    55.80605922806669                                                                                                                                                                                  
                ],                                                                                                                                                                                                     
                "type": "Point"                                                                                                                                                                                        
            },                                                                                                                                                                                                         
            "global_id": 171714466                                                                                                                                                                                     
        },                                                                                                                                                                                                             
        "Id": "78277b32-5752-42f3-8bc9-653809490e3f",                                                                                                                                                                  
        "Number": 800                                                                                                                                                                                                  
    },                                                                                                                                                                                                                 
       
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
