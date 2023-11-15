

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/TechStack-VivifyHealthcare.png" align="right" width="250"/> <img src="https://user-images.githubusercontent.com/92524410/217502426-8454bf20-7da8-4536-a049-a6bb7e96b09a.png" width="180"/> 

# Boolean-data-true/false-handling-from-api-with-intents


The release of [**Rasa Chatbot** ](https://github.com/vivifyhealthcare/Rasabot/edit/7-boolean-data-truefalse-handling-from-api-with-intents/README.md) with Api integration for Boolean-data-true/false-handling-from-api-with-intents at [**Vivify Healthcare** ](https://vivifyhealthcare.com/)  is part of the company's research and development efforts to find the best technology stack that is both sustainable and affordable.
The company constantly looks for ways to improve its offerings and stay ahead of the curve in the highly competitive healthcare industry. Utilizing the leading and open-source platform for transforming; how people interact with people/organizations through extensible conversational AI via RASA, Vivify Healthcare aims to deliver a top-notch user experience while keeping costs low and maintaining stability, security, and compliance.

Repository https://github.com/vivifyhealthcare/Rasabot/edit/7-boolean-data-truefalse-handling-from-api-with-intents/README.md

Handling boolean data and defining how true and false values are handled in the context of API intents.


# Benfits of Boolean

Clarity and Expressiveness: By using boolean values in your API intents, you make the purpose and expected behavior of the API endpoint clear and intuitive. Developers and users can easily understand the intent behind the request, such as turning a feature Yes (true) or No (false).

Simplified and Consistent API Design: Boolean values simplify the design of your API by reducing the need for complex input parameters or multiple endpoints to handle different scenarios. It promotes a more consistent and straightforward API structure.

Reduced Cognitive Load: When developers work with your API, they don't need to remember specific parameter names or values for various actions. Using boolean values simplifies the decision-making process, reducing cognitive load.

# Procedure to boolean data true or false handling

**Intents:** Make sure to train your chatbot with examples of user messages that correspond to these intents. The training data should cover various ways users might express these intentions.

**Responses:** Customize the responses for each intent to make your bot's interactions more engaging and informative. You can add text, images, buttons, or other content to your responses.

**Slots:** Slots are crucial for storing and tracking user-provided information throughout the conversation. Depending on the conversation flow, you may need to fill and use slots within your dialogue management.

**Forms:** Forms help in structured data collection from the user. You should define the validation rules for slots in your forms and specify how to activate and deactivate them during the conversation flow.

**Actions:** Implement the custom logic for your actions. These actions can include making API calls, database operations, or other business logic based on the collected information or user interactions.

# Rules:

In Rasa, rules are used to define specific conversation flows and dictate how the chatbot should respond to certain user intents or conditions. Rules provide a structured way to handle conversations in a more deterministic manner compared to machine learning-based intent recognition. Here's what you can do with rules in a Rasa bot:

# How to convert to Boolean in rasa

**Boolean Data:** Boolean data is a data type that represents one of two values: true or false. It's commonly used to represent binary decisions, such as yes/no. In programming, boolean data is often used for conditional statements and logic.

**True and False Values:** In the context of boolean data, "true" represents a positive or affirmative condition, and "false" represents a negative or negative condition. For example, "thease details are correct" can be represented as either "true" (yes) or "false" (no).

**API Intents:** APIs (Application Programming Interfaces) can define various intents to specify the actions or operations they support. An intent represents the purpose of a request made to the API, allowing developers to interact with the API based on specific intentions.

**Handling Boolean Data with API Intents:**
When you're designing API endpoints or requests that involve boolean data, you can define intents that correspond to the actions you want to perform with that data.

# Boolean-data-truefalse-handling-from-api-with-intents

Handling boolean data and defining how true and false values are handled in the context of API intents.

# Benfits of Boolean

**Clarity and Expressiveness:** By using boolean values in your API intents, you make the purpose and expected behavior of the API endpoint clear and intuitive. Developers and users can easily understand the intent behind the request, such as turning a feature Yes (true) or No (false).

**Simplified and Consistent API Design:** Boolean values simplify the design of your API by reducing the need for complex input parameters or multiple endpoints to handle different scenarios. It promotes a more consistent and straightforward API structure.

**Reduced Cognitive Load:** When developers work with your API, they don't need to remember specific parameter names or values for various actions. Using boolean values simplifies the decision-making process, reducing cognitive load.

# Procedure to boolean data true or false handling

## domain.yml

**Intents:** Make sure to train your chatbot with examples of user messages that correspond to these intents. The training data should cover various ways users might express these intentions.

**Responses:** Customize the responses for each intent to make your bot's interactions more engaging and informative. You can add text, images, buttons, or other content to your responses.

**Slots:** Slots are crucial for storing and tracking user-provided information throughout the conversation. Depending on the conversation flow, you may need to fill and use slots within your dialogue management.

**Forms:** Forms help in structured data collection from the user. You should define the validation rules for slots in your forms and specify how to activate and deactivate them during the conversation flow.

**Actions:** Implement the custom logic for your actions. These actions can include making API calls, database operations, or other business logic based on the collected information or user interactions.

## rules.yml:

In Rasa, rules are used to define specific conversation flows and dictate how the chatbot should respond to certain user intents or conditions. Rules provide a structured way to handle conversations in a more deterministic manner compared to machine learning-based intent recognition. Here's what you can do with rules in a Rasa bot:

# How to convert to Boolean in rasa

## actions.py

**Boolean Data:** Boolean data is a data type that represents one of two values: true or false. It's commonly used to represent binary decisions, such as yes/no. In programming, boolean data is often used for conditional statements and logic.

**True Values and False Values:** In the context of boolean data, "true" represents a positive or affirmative condition, and "false" represents a negative or negative condition. For example, "thease details are correct" can be represented as either "true" (yes) or "false" (no).

**API Intents:** APIs (Application Programming Interfaces) can define various intents to specify the actions or operations they support. An intent represents the purpose of a request made to the API, allowing developers to interact with the API based on specific intentions.

**Handling Boolean Data with API Intents:**
When you're designing API endpoints or requests that involve boolean data, you can define intents that correspond to the actions you want to perform with that data.

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/endpoint+tech+re.png">

If you want to run RASA chat bot you have to clone the repository and you have to replace what you designed the endpoint.

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/boolen+buttons+tech.png">


When we have click the yes/no button it will show in "is this correct" field as a true/false. 

"
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/get+data+final.png">

Till now what we have to give the data we have to use that data for the post as wells as get to visual. When we have to enter all the details it will ask "IS THIS CORRECT" filed, there it shows "YES/NO" value. When we have to choose "YES" value then the data shows "TRUE" as well as if we choose "NO" value then the data shows "FALSE".


<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>
