##Take me to a Park
## Inspiration
One of our team members was extremely enthusiastic with using Amazon Alexa, so we put our pea sized brains together and decided to create an Alexa skill that will allow bored couch potatoes to find fun and new places to explore around Michigan by using data provided by the Michigan Open Dataset
## What it does
The user speaks to the Amazon Alexa enabled device where a conversation ensues which allows Alexa to gain required information to tailor the results to a park that the user has access to.
## How we built it
We first setup the Alexa Skill through the Amazon Dev Portal. We then setup ngrok to receive https from the Alexa web service. From there we created the backend using Python3 and Ask-Flask to create a comfortable and efficient interface for the user to speak with Alexa
## Challenges we ran into
First, we needed to get our Lambda working. But we needed to get an Amazon AWS for Lambda. Unfortunately, you need a credit card for AWS. So, while thinking furiously, we overheard a fellow hacker mention the 100$ AWS credit sent to all hackers preceding the event. We quickly rushed to uncover our codes only to realize that AWS required us to be ages 18 and up...

Being the inventive, sly, and clever people we are, we swiftly fired up ngrok and found Ask-Flask and within seconds... minutes... hours... we were well on our way of producing the coolest thing since pre-cut frozen french fries.

## Accomplishments that we're proud of
- Using Alexa while completely avoiding AWS
- Making the backend in Python3 and Flask
- Writing scripts to extract data from complex data structures (Mich open data)
## What we learned
- How to setup an Alexa Skill
- How to use Flask and Ask-Flask
- How to use NGROK
- How to access Michigan Open Data
- How to use Amazon Alexa and the Amazon Echo
## What's next for Take Me To a Park
- Using other databases in the Michigan Open Data Library
- Expanding dataset to outside the Michigan area
- Allowing even more streamlined interfacing with Alexa
