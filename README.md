# Discord Bot for Role Management and Fun

This Python script is designed to create a bot using the Discord API for role management and fun interactions. The bot can perform various actions, including displaying a list of available commands and emotes, managing roles, generating memes, and responding to reactions. Below is a detailed documentation of the script:

## Required Libraries

Before running this script, ensure that you have the following libraries installed:

- `discord`: This library is used for interacting with the Discord API.
- `asyncio`: Asyncio is used for asynchronous operations.
- `configparser`: Used for reading configuration data from the `config.ini` file.
- Other Python libraries like `json` and `datetime` for various functions.

## Configuration File

The script reads configuration values (such as the bot's token and prefixes) from a `config.ini` file. Make sure to create this file and populate it with the required data.

## Bot Initialization

The script initializes the Discord bot with the specified token and sets up event handlers to respond to messages and reactions. The bot's token is read from the `config.ini` file.

## Message Handling

The script defines an `on_message` event handler that responds to user messages with various functionalities:

- **Help Command**: Responds to messages starting with the bot's prefix followed by "help" (e.g., `y!help`) by sending an embedded list of available commands and their descriptions.

- **Emotes Command**: Responds to messages starting with the bot's prefix followed by "emotes" (e.g., `y!emotes`) by sending an embedded list of available emotes and their usage.

- **Memes Command**: Responds to messages starting with the bot's prefix followed by "memes" (e.g., `y!memes`) by sending an embedded list of available memes and their descriptions.

- **Roles Command**: Responds to messages starting with the bot's prefix followed by "roles" (e.g., `y!roles`) by sending an embedded list of available roles that users can self-assign.

- **Meme Generator**: Allows users to generate memes using various templates and text inputs.

- **GIF Interactions**: Allows users to trigger fun GIF interactions with mentions.

- **Context Command**: Responds to messages starting with the bot's prefix followed by "dar-contexto" by providing context to the conversation with an embedded GIF.

- **Shipp Command**: Allows users to "ship" two mentioned users for fun interactions.

## Reaction Handling

The script defines an `on_reaction_add` event handler that responds to reactions added to messages:

- **Role Assignment**: When a user reacts to a message with a specific emoji (e.g., a role emoji), the bot assigns the corresponding role to the user.

