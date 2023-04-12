

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> <img src="https://user-images.githubusercontent.com/92524410/217502426-8454bf20-7da8-4536-a049-a6bb7e96b09a.png" width="180"/> 

<h1 font-size="50px" align="center">Sample RASA Chatbot with Web UI & API Connectivity</h1>

RASA is an open-source machine learning framework for automated text and voice-based conversations. Understand messages, hold conversations, and connect to messaging channels and APIs.
It's incredibly powerful and is used by developers worldwide to create chatbots and contextual assistants. Before we get into Installation, let's look into some simple concepts that we should know while creating a chatbot.
<div align="center">
  
  <img src="https://img.shields.io/badge/Python-3.7-yellowgreen" />
    <img src="https://img.shields.io/badge/Rasa-2.8.1-blueviolet" />
    <img src="https://img.shields.io/badge/Release-1.0.0-blue" />
  </div>
  
<div align="center">
 <img  src="https://vivifyassets.s3.ap-south-1.amazonaws.com/ezgif.com-gif-maker.gif" />
  
</div>



## Features

- Sample Bot
- API Connectivity
- Fullscreen mode
- Show Image(Display Immage)
- Change Chatbot Avatar


## Development Environment (Local)
#### System Requirements
💻 Supported Os:
* Ubuntu (18.04/20.04)
* Windows
* Mac Os
* CentOS (7/8)
* Red Hat Enterprise Linux

⚙️Hardware Requirements:

###### Minimum Requirements
* Dual Core CPU / Quad Core CPU
* 8 GB RAM/ 16 GB RAM
* 20 GB / 50 GB Free Disk Space

💡 Before you begin, make sure you have the following installed:
- Python - 3.7.5
- Visual Studio
- Git

[**Check Installation Requirement for RASA** ](https://rasa.com/docs/rasa-enterprise/1.0.x/installation-and-setup/requirements/)
## Getting Started With Local Development


## Installation
* Open Visual Studio and go to Terminal and run the following command
* First check your Python Version installed in your System

```bash
  python --version
```
* You need to create Virtual Environment which is used to manage Python packages for certain project.Using Virtual Environment Avoids installing Python packages globally.

```bash
  python -m venv env
```
* You need to Activate Environment once which is created use below command to activate it
```bash
  env/scripts/activate
```
* Once it is Activated you can Install RASA
```bash
  pip install rasa==2.8.1
```
* After installing RASA you are able to see the Message 'Successful installed'.
* Create a RASA Project 
```bash
    rasa init
```
* Choose your directory where do you want to create project 
![Screenshot_20230203_024408](https://user-images.githubusercontent.com/92524410/216560304-542057f7-4297-4f4a-99a2-624edc08ecc6.png)
* You can able to see project structure of RASA.

![image alt >](https://vivifyassets.s3.ap-south-1.amazonaws.com/image+(1).png)


* **nlu.yml:**
This file contains the possible messages from the user and the corresponding intent. This file is used for creating the intent classification model. Whenever the user inputs a message, the classification model automatically classifies the intent of the message.
* **Stories.yml:**
It contains different possible sample interactions between the user and the chatbot. With this sample, the bot will get an idea about what would be the possible reply for user input.
* **Domain.yml:**
This file contains different bot responses list all the intents and entities used while creating the nlu.yml file.
* **Actions.py:**
This is the python file to run the custom actions. This file can be used for an API call or database querying. When the action is "action_hello" the above code will execute and dispatches the text "Hello" as a reply.
* **Training:**
Bot as created a Basic project, now we can train our model based on the data that we have provided. RASA will start to train both nlu and core model and then stores the trained model in the models folder by the following command
```bash
  rasa train
```

* RASA will create inital project where you can able to talk to the Bot, When it will ask you to train the Intial Bot: Choose "Yes".

![image](https://user-images.githubusercontent.com/92524410/216561608-b02b5938-8198-4404-96d2-99972584c777.png)
* Model is created Successfully 
![image](https://user-images.githubusercontent.com/92524410/216568087-3b066cfb-7968-4b18-b7bc-abc9b190e649.png)

* Choose 'Yes' to talk to the Chatbot.
![image](https://user-images.githubusercontent.com/92524410/216569130-4f024f5a-3c06-4d3a-b287-97b1fa1cf7f7.png)


- To know more about the usage of the files, i surely recommend you to refer to [RASA Docs](https://rasa.com/docs/rasa/2.x/)

### Connecting Chatbot to Different Channels
In RASA you can connect Chatbot to different Channels using Credentials.yml.
![image](https://user-images.githubusercontent.com/92524410/216886817-46855453-a140-4a8b-a141-311e6f68d0bf.png)

To integrate chatbot into the  web widget, we have to enable the channel integration in "Credentials.yml".
Here we are using SocketIO channel which uses WebSockets in real-time. To use the SocketIO channel, use below Credentials to your credentials.yml
```bash
socketio:
 user_message_evt: user_uttered
 bot_message_evt: bot_uttered
 session_persistence: true
```
Need to create one more file in our project that's an HTML file in this file we will be integrating our bot with a web widget
and this web widget can be attached to the web project that you want.
I am renaming the HTML file as an Index.html, and using a template from RASA documentation in this template javascript code is inbuilt so the onclick operations and triggering we don't need to
write the logic everything is done by rasa.

There are Two widget Ui's you can use any of these Ui's
Paste this Code in Index.html
### Widget 1
```bash
<div id="rasa-chat-widget" data-websocket-url="https://localhost:5005/"></div>
<script src="https://unpkg.com/@rasahq/rasa-chat" type="application/javascript"></script>
```
### Widget 2
```bash
  <html>
  <head>
    <meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0"/>
    <style>
      .rw-conversation-container .rw-header{background-color:hsl(250, 69%, 61%);}
      .rw-conversation-container .rw-messages-container .rw-message .rw-client{background-color: hsl(250, 69%, 61%);}
      .rw-launcher{background-color: hsl(250, 69%, 61%);}
      .rw-conversation-container .rw-reply{background-color: hsl(250, 69%, 61%); border: 1px solid hsl(250, 69%, 61%);}
  </style>
  </head>
    <body>
        <script>!(function () {
            let e = document.createElement("script"),
              t = document.head || document.getElementsByTagName("head")[0];
            (e.src =
              "https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.js"),
              (e.async = !0),
              (e.onload = () => {
                window.WebChat.default(
                  {
                    customData: { language: "en" },
                    socketUrl: "http://localhost:5005/",
                    title: 'Lifeeazy',
                    subtitle: 'Say hi and get started!',
                    initPayload: '/greet',
                    profileAvatar: "https://img.icons8.com/fluency/344/chatbot.png",
                    openLauncherImage: "./assets/svg/comment.svg",
                    closeImage: "./assets/svg/down.svg",
                    showMessageDate: true,
                    inputTextFieldHint: "Type 'Hi' to start the conversation",
                    embedded: true,
                  },
                  null
                );
              }),
              t.insertBefore(e, t.firstChild);
          })();
          localStorage.clear();
          </script>
    </body>
</html>
```

The first two configuration value defines the event names used by RASA Open Source when sending or receiving messages over [socket.io].

Restart your RASA server to make the new channel endpoint available to receive messages. You can then send messages to ```http://<host>:<port>/```,
replacing the host (i.e. localhost) and port (i.e. 5005 - its a default port for rasa) 
  
 ![image](https://user-images.githubusercontent.com/92524410/217512457-83a8bc9a-859e-4de8-b164-5d34ce089553.png)

### 
Now you can run these command  and Copy file path of index.html and paste it in web browser to see the chat widget
```bash
  rasa run -m models --enable-api --cors * 
```

<div align="center"/>
    <img src="https://user-images.githubusercontent.com/92524410/217515656-648fd520-bd2f-4a89-926d-952060e1ecf7.png" />
    <img src="https://user-images.githubusercontent.com/92524410/217448866-4a3db819-7033-4c32-9338-a9871c2f807d.png" />
 </div>


## Integration of Open API's in Rasa
To integrate any logical operations in rasa, we need to use Actions.py file

<p align="center">
<img src="https://user-images.githubusercontent.com/92524410/216952029-0b84e798-1499-4f79-8f82-f93be0e47c7d.png"/>
</p>
Here we are using open Api's https://apisetu.gov.in/directory/api/cowin/

* Create a new file main.py and paste below code, i was making a Get call here using Lattitude and Longitude values passed by the user in Bot.

```bash

import requests

def Dose_Availability_Lon_Lat(Lattitude,Longitude):
    api="https://cdn-api.co-vin.in/api/v2/appointment/centers/public/findByLatLong?lat={}&long={}".format(Lattitude,Longitude)
    return main_task(api)

def main_task(api):
    response=requests.get(api)
    data=response.json()['centers']
    output="*"*30
    # print(data)
    for area in data:
        output+="  Hospital Name:" + area['name'] + "*"*30 +"\n"
        output+='''\
pincode: {}
state_name: {}
district_name : {}
block_name : {}
'''.format(area['pincode'],area['state_name'],area['district_name',
area['block_name'])
            output+="*"*30
    return output
```
User input Values are stored using [Slots](https://rasa.com/docs/rasa/domain/).

with Domain.yml you can able to see Slots as Longitude and Lattitude

```bash
slots:
  lattitude:
    type: rasa.shared.core.slots.TextSlot
    initial_value: null
    auto_fill: true
    influence_conversation: true
  longitude:
    type: rasa.shared.core.slots.TextSlot
    initial_value: null
    auto_fill: true
    influence_conversation: true
```
and the connection between slots and the actions.py was done in stories.yml and rules.yml

```bash
  - rule: Activate location form
  steps:
  - intent: location
  - action: slot_location_form
  - active_loop: slot_location_form

- rule: Submit location form
  condition:
  # Condition that form is active.
  - active_loop: slot_location_form
  steps:
  # Form is deactivated
  - action: slot_location_form
  - active_loop: null
  - slot_was_set:
    - requested_slot: null
  # The actions we want to run when the form is submitted.
  - action: action_location_submit
```

after connecting all the things you need to train the Bot again
```bash
rasa train
```
to run actions.py you need to run actions command in seperate terminal
```bash
rasa run actions
```
  
  <table>

  <tr>
    <td><img src="https://user-images.githubusercontent.com/92524410/217488188-2408a261-e098-4637-b642-b58639f0a25b.png" width=270 height=480></td>
    <td><img src="https://user-images.githubusercontent.com/92524410/217448866-4a3db819-7033-4c32-9338-a9871c2f807d.png" width=270 height=480></td>
    <td><img src="https://user-images.githubusercontent.com/92524410/217448884-0aca13f9-cde8-473c-9a0c-64fee34fa10d.png" width=270 height=480></td>
  </tr>
 </table>
  
  

**So now you have connected an Open API in RASA Chatbot Web UI.
For more details releated to RASA you can always refer to the latest documents and releases on Rasa.com or [Rasa Docs](https://rasa.com/docs/rasa/)**






## <h1>Customized Google Search Engine By Using RASA</h1>



<img src="https://kvliveblog.files.wordpress.com/2013/02/make-google-default-search-engine-icon.png" align="right" height=100 width="250">


<img src="https://user-images.githubusercontent.com/92524410/217502426-8454bf20-7da8-4536-a049-a6bb7e96b09a.png"
align="left" height =100 width="180" >


<br>
<br>
<br>
<br>




<div padding-top=100px><h2 align="left">About Google search engine:</h2></div>


 Google Search Engine was launched in 1998 and quickly became the most popular search engine in the world due to its accuracy, speed, and ease of use. The most popular search engine is Google, but there are many others, such as Bing, Yahoo, and DuckDuckGo.
Google Search Engine is a search engine developed and operated by Google. It is a web-based search tool that allows users to find information on the World Wide Web.


## Advantages of Google search engine:
  * Results are measurable
  * Helps to Grow Your Small Business
  * get fast website Traffic and conversions
  * You can search whatever you want
  * Google provides better and easier results


## features of Google search engine:
  * Query processing
  * Search filters
  * Personalization
  * Advertising    
    

## How To Create gooogle search engine account:
    first we need to create google search engine account 
use this link to create google search engine account : 
[Click Here](https://programmablesearchengine.google.com)

After created account successfully. It will show like this 
    
  <img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/vasu/search+engine.png">

Then open the search engine it looks like this

  <img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/SE+ID+2.png">

Their is an "overview" option at the left side of the page. Their is name like "search features" option in that search features their is an "sites to search" in that option we have to add our required "web sites" to get the Result.

  <img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/vasu/sites+to+search.png">


## How To Generate API Key:
    To generate the API Key we need to refer the Documentation.
Documentation Link: 
    [Click Here](https://developers.google.com/custom-search/docs/overview)

After open the Documentation go to "Using REST" at the left bottom of the page.

 <img src= "https://vivifyassets.s3.ap-south-1.amazonaws.com/vasu/API+Key.png">


Their is a JSON API URI in  "Making a request" that is the API Key.


It's Looks like this : https://www.googleapis.com/customsearch/v1?key=INSERT_YOUR_API_KEY&cx=017576662512468239146:omuauf_lfve&q=lectures


To Access this API Key we need to provide three keys:

* API Key
* Programmable search engine ID
* Query


* API Key : To generate an API Key  go to the "Introduction" at  the left bottom of the page of google documentation. 
                Their is a Button like "Get a Key" click on it and it will generate the Key. 
      
   <img src= "https://vivifyassets.s3.ap-south-1.amazonaws.com/vasu/Introduction.png">

* Programmable search engine ID : we can find the search engine ID in the account which is already created before.           

   <img src= "https://vivifyassets.s3.ap-south-1.amazonaws.com/SE+ID+2.png">
    
* Query : query is nothing but it's our requirement. we have to enter our query regarding our problem.



Place the Above keys in this API (https://www.googleapis.com/customsearch/v1?key=( API Key)&cx=( programmable search engine ID)=(Query))


    Now we are successfully generated the API.


After successfully generate the API Use this API in RASA.

## How to use the API in RASA

After successfully installation of RASA. 

If Any doubts about installation of RASA refer this Documentation [Click Here](https://rasa.com/docs/rasa/2.x/installation)


Create one Python file in that .py file use this API.

Here is an Example code for how to use the API in .py file

    import requests
    import webbrowser
    import json

    def get_details(query):
        Api = 'https://www.googleapis.com/customsearch/v1?key=(API Key)&cx=(programmable search engine ID)={}'.format(query)
        response = requests.get(url=Api)
        print(response)
        count=response.json()['queries']['request'][0]['count']
        title=response.json()['items'][0]['link']
        print(title)
        print(count)
        message=""
        if count<5:
            for i in range(count):
                link=response.json()['items'][i]['link']
                title=response.json()['items'][i]['title']
                link1 = link + '\n'
                message +='['+title+']'+'('+link1+')' + '\n' + '\n'
            return message

        else:
            for i in range(5):
                link=response.json()['items'][i]['link']
                title=response.json()['items'][i]['title']
                link1 = link + '\n'
                message +='['+title+']'+'('+link1+')' + '\n' + '\n'
            return message


## Commands to Run the code:
This command is used to train the models.

    rasa train

This command is used to run the models.

    rasa run --enable-api --cors "*"

This command is used to run the actions.

    rasa run actions
    
    
<b>Note</b>: rasa run actions are run in separate "powershell"


<b>Note</b>: Copy file path of index.html and paste it in web browser to see the chat widget

## Output:

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/vasu/output.png">


<b>Note</b>: Here is the Top 5 links from the Google.


<hr>

<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>



