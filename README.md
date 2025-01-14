# Build an AI Slack Bot

Welcome to the **Build an AI Slack Bot** project! This project is a Django-based application designed to integrate AI-powered functionalities with Slack. The bot can handle events, respond to messages, and integrate with external APIs to provide dynamic and intelligent responses.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Slack Integration**: Seamlessly integrates with Slack APIs to handle events and send/receive messages.
- **AI Capabilities**: Leverages AI models to process and respond intelligently.
- **Event Subscriptions**: Handles Slack event subscriptions with secure endpoints.
- **Environment Management**: Uses `python-decouple` for environment-based configurations.
- **Modular Design**: Well-structured Django app with reusable components.

---

## Installation

### Prerequisites

- Python 3.12 or later
- Poetry (for dependency management)
- A Slack workspace with API credentials

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/SahilMehdiyev/Build-an-AI-Slack-Bot.git
   cd Build-an-AI-Slack-Bot
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## Configuration

### Environment Variables

This project uses `python-decouple` for environment variable management. Create a `.env` file in the root directory with the following keys:

```env
SLACK_BOT_TOKEN=<your-slack-bot-token>
SLACK_SIGNING_SECRET=<your-slack-signing-secret>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Replace `<your-slack-bot-token>` and `<your-slack-signing-secret>` with your Slack app credentials.

### Slack App Setup

1. Create a new Slack app at [Slack API](https://api.slack.com/apps).
2. Configure **Event Subscriptions**:
   - Enable events.
   - Set the Request URL to your bot endpoint (e.g., `https://<your-ngrok-url>/bot/events/`).
3. Add required **OAuth Scopes** for your app.
4. Install the app to your workspace.

---

## Usage

- Start the Django server and expose it using `ngrok`:
  ```bash
  ngrok http 8000
  ```
- Use the generated ngrok URL as the Request URL in Slack's Event Subscriptions.
- Test the bot by interacting with it in your Slack workspace.

---

## Project Structure

```plaintext
Build-an-AI-Slack-Bot/
├── bot/                # Contains bot-specific logic and event handling
├── cfehome/            # Django project settings and configurations
├── helpers/            # Helper functions and utilities
├── manage.py           # Django's command-line utility
├── README.md           # Project documentation
├── pyproject.toml      # Poetry configuration file
├── .env                # Environment variable configuration (not committed)
├── db.sqlite3          # SQLite database (for development only)
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by **Sahil Mehdiyev**. For inquiries, contact [branchsahil@gmail.com](mailto:branchsahil@gmail.com).
