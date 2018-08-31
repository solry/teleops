# teleops

Telegram bot application

## Structure

#### 1. TeleWebHook
Responsibilities:
 - Receiving updates (messages) from Telegram API services
 - Passing this messages to `TeleEngine`
  
#### 2. TeleEngine
Responsibilities:
 - Receiving updates from `TeleWebHook`
 - Perform authentication of users
 - Call external scripts
 - Leveraging `TeleDatabaseTools` for logging, authentication and other control
 
#### 3. TeleDatabaseTools
Collection of tools that used by `TeleEngine` to interact with `TeleDatabase`

#### 4. TeleDatabase
PostgreSQL Database that contains information about users, they privileges, commands, etc.

#### 5. TeleManager
Django Web Framework Application that allows you to manage users and they privileges.
`TeleManager` interacts with `TeleDatabase`

## Plan

- [ ] Creation of interacting scheme for 5 main elements
- [ ] Choose platform for `TeleWebHook` web server:
  - CherryPy
  - Django
- [ ] Choose way of interaction of `TeleManager` application and `TeleDatabase`:
  - Django Api
  - Python Class based 
- [ ] Figure out distribution method:
  - Docker Container:
    - Single container with `TeleEngine`, `TeleDatabase`, `TeleWebHook`, `TeleManager`
    - 3 Dedicated container:
      - `TeleWebHook`, `TeleEngine`, `TeleDatabaseTools`
      - `TeleDatabase`
      - `TeleManager`
- [ ] Code `TeleWebHook`
- [ ] Code `TeleDatabaseTools`
- [ ] Code `TeleEngine`
- [ ] Code `TeleManager`
- [ ] Code distribution model