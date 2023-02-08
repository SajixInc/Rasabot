<img align="right" width="33%" src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png">



# Sample Rasa Webui Chatbot with API connection 

Rasa is an open-source machine learning framework for automated text and voice-based conversations.Understand messages, hold conversations, and connect to messaging channels and APIs.
It's incredibly powerful and is used bydevelopers worldwide to create chatbots and contextual assistants. Before we get into Installation, let's look into some simple concepts that we should know while creating a chatbot.

[![Python](https://img.shields.io/badge/Python-3.7-yellowgreen)](https://www.python.org/downloads/release/python-370/)
[![Rasa](https://img.shields.io/badge/Rasa-2.8.1-blueviolet)](https://rasa.com/)
[![Release](https://img.shields.io/badge/Release-1.0.0-blue)](http://www.gnu.org/licenses/agpl-3.0)


# ![](https://vivifyassets.s3.ap-south-1.amazonaws.com/ezgif.com-gif-maker.gif)
## Features

- Sample Bot
- Api Connectivity
- Fullscreen mode
- Show Image
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

#### Getting Started With Local Development


## Installation
* Open Visual Studio and go to Terminal and run the following command
* Firstly see your Python Version to know is it installed in your System

```bash
  python --version
```
* You need to create virtualenv it is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

```bash
  python -m venv env
```
* You need to Activate Environment once it is created use below command to cactivate it
```bash
  env/scripts/activate
```
* Once it is Activated you can Install Rasa
```bash
  pip install rasa==2.8.1
```
* After installing Rasa you can able to see Successful installed,we need to create Rasa Project
```bash
    rasa init
```
* Choose your directory where do you want to create project 
![Screenshot_20230203_024408](https://user-images.githubusercontent.com/92524410/216560304-542057f7-4297-4f4a-99a2-624edc08ecc6.png)
* You can able to see project structure of Rasa.

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
Bot as created a Basic project, now we can train our model based on the data that we have provided rasa will start to train both nlu and core model and then stores the trained model in the models folder by the following command 
```bash
  rasa train
```


* Rasa will create inital project where you can able to talk to the Bot, And it will ask you to train the Intial Bot Choose "Yes".

![image](https://user-images.githubusercontent.com/92524410/216561608-b02b5938-8198-4404-96d2-99972584c777.png)
* Model is created Successfully 
![image](https://user-images.githubusercontent.com/92524410/216568087-3b066cfb-7968-4b18-b7bc-abc9b190e649.png)

* Choose 'Yes' to talk to the Chatbot.
![image](https://user-images.githubusercontent.com/92524410/216569130-4f024f5a-3c06-4d3a-b287-97b1fa1cf7f7.png)


- To know more about the usage of the files, i surely recommend you to refer this [link](https://rasa.com/docs/rasa/2.x/)

### Connecting Chatbot to Different Channels
In rasa you can connect Chatbot to different Social platforms, you can connect using Credentials.yml.
![image](https://user-images.githubusercontent.com/92524410/216886817-46855453-a140-4a8b-a141-311e6f68d0bf.png)

To integrate our chatbot into the  web widget, we have to enable the channel integration in "Credentials.yml",
The SocketIO channel uses WebSockets and is real-time. To use the SocketIO channel, add the credentials to your credentials.yml
```bash
socketio:
 user_message_evt: user_uttered
 bot_message_evt: bot_uttered
 session_persistence: true
```
Need to create one more file in our project that's an HTML file in this file we will be integrating our bot with a web widget
and this web widget can be attached to the web project that you want.
I am renaming the HTML file as an Index.html, and using a template from rasa documentation in this template javascript code is inbuilt so the onclick operations and triggering we don't need to
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

The first two configuration values define the event names used by Rasa Open Source when sending or receiving messages over socket.io.

Restart your Rasa Open Source server to make the new channel endpoint available to receive messages. You can then send messages to HTTP://<host>:<port>/socket.io,
 replacing the host and port with the appropriate values from your running Rasa Open Source server.

### 
Now you can run these command to see the widget as be configured correctly or not
```bash
  rasa run -m models --enable-api --cors * 
```

Copy index.html file path and paste it in web browser, there you can able to see the web widget.

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

Domain.yml you can able see Slots as Longitude and Lattitude

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

after connecting all the things you need to train the Bot again using
```bash
rasa train
```
to run actions.py you need to run seperate command
```bash
rasa run actions
```
  
  <table>
  <tr>
    <td>Screen 1</td>
     <td>Screen 2</td>
     <td>Screen 3</td>
  </tr>

  <tr>
    <td><img src="https://user-images.githubusercontent.com/92524410/217488188-2408a261-e098-4637-b642-b58639f0a25b.png" width=270 height=480></td>
    <td><img src="https://user-images.githubusercontent.com/92524410/217448866-4a3db819-7033-4c32-9338-a9871c2f807d.png" width=270 height=480></td>
    <td><img src="https://user-images.githubusercontent.com/92524410/217448884-0aca13f9-cde8-473c-9a0c-64fee34fa10d.png" width=270 height=480></td>
  </tr>
 </table>
  
  

So now you have connected an Open Api in rasa Chatbot Web ui, I surely recommend to refer rasa Documents for Understanding Better [Document](https://rasa.com/docs/).
<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>
