# teleops

Telegram bot application

## Structure

#### 1. NGINX
 - Receiving updates (messages) from Telegram API services on port 8443
 - Passing this messages to `TeleEngine`
 - Listening on port 443 to proxying to TeleManager Django web APP
 
#### 2. TeleManager
 - Receiving Telegram updates from `NGINX`
 - Passing Telegram messages to `TeleBot`
 - Django Web App that allows:
  - Manage TeleOps user's accounts
  - 
 
#### 3. TeleBot
 - Receiving Telegram messages from `TeleManager`
 - Perform authentication of users
 - Sending task to `TeleEngine` according to arrived message
 - Receiving task results from `TeleEngine`
 - Sending messages back to Telegram Users
 - Leveraging Python for logging, authentication and other control
  
#### 4. TeleEngine
 - Receiving tasks from `TeleBot`
 - Sending results to `TeleEngine`
 
#### 4. TeleDatabase
PostgreSQL with two databases:
 - `telemanager` DB: contains information about users, they privileges, commands, etc.
 - `teleapp` DB (optional): application data.

#### 5. TeleManager
Django Web Framework Application that allows you to manage users and they privileges.
`TeleManager` interacts with `TeleDatabase`

## Plan

- [X] Creation of interacting scheme for 5 main elements:
![alt text](https://github.com/solry/teleops/blob/master/files/schema/main-schema.png)
- [X] Choose platform for web server:
  - CherryPy
  - **NGINX + gunicorn + Django**
  > **NGINX + gunicorn + Django** was choosen as the web server platform due to:
  > - recommended production environment
- [X] Choose way of interaction of `TeleManager` application and `TeleDatabase`:
  - **Django ORM**
  - Python Class based 
  > **Django ORM** has been choosen due to convenience.
- [X] Figure out distribution model:
  - Docker Container:
    - Single container with `TeleManager`, `TeleBot`, `TeleEngine`, `TeleDatabase`
    - **2 Dedicated container**:
      - `TeleManager`, `TeleBot`, `TeleEngine`
      - `TeleDatabase`
  - Single application, which requires the user to install the database and application on the machine barely
  
  > **2 Dedicated container** was chosen as distribution model due to:
  > - Learning of Docker objectives
  > - Fast deployment
  > - Microsegmentation
- [ ] Create template for NGINX config
- [ ] Code `TeleManager`
- [ ] Code `TeleBot`
- [ ] Code `TeleEngine`
- [ ] Code distribution (images, docker-compose)