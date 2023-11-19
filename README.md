# Cumulocity Home Assistant HACS Integration 

This repository utilizes the Home Assistant Community Store (HACS) approach to integrate with the Cumulocity platform within the Home Assistant ecosystem. This is connected via the [Cumulocity REST API](https://cumulocity.com/api/core/) which is a tennant driven IOT device management platform.  

## This project is supported by [Kallipr IOT](https://kallipr.com/)

![Kallipr](https://cdn.kallipr.com/wp-content/uploads/2022/11/24132240/Kallipr-Logo-Inline-rgb-small.png)

# Getting set up

## pre-requisites 

To run this you are going to need an active installation of [Home Assistant](https://www.home-assistant.io) with HACS installed. Visit the [HACS installation](https://hacs.xyz/docs/setup/download/) page to get started with [HACS](https://hacs.xyz/docs/setup/download/). 

## Installing 

Once the pre-reqs are installed, head to the `HACS` tab in your Home Assistant and click on `Integrations`. Then Click the 3 dots in the top right and select `custom repositories`. 

Add this repository to the `custom repositories` pop-up box and select `integration` in the category dropdown. Finally click `add` follow the prompts and install.  

Once installed you will need to then configure the integration with your cumulocity sign in details. You are going to need the following: 

- `base_url` -- Cumulocity instance url 
- `tenant`   -- Cumulocity tenant id 
- `username` -- Cumulocity username
- `password` -- Cumulocity password

Enter those details into the configuration box and then submit to let the integration complete its install. 

### Things to note

To update new devices associated to the registered cumulocity account, run an initialise from the integration settings.

# Todo's

- Currently all devices associated to the login are brought in and attached with their respective measurements as Home Assistant entities. Potentially this will be swapped out for a list of devices that can be selected from. 
- Faster updates using the [Cumulocity real time updates api].(https://cumulocity.com/api/core/#section/Real-time-operations/Handshake)
- automatically update and check for new devices on existing integrations 



### This project is dedicated to Peter Howchin 
We didnt get to meet but the stories of your innovation and perseverance are an inspiration, and this ones for you 🫶