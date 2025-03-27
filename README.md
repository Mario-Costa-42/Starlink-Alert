# Starlink Notifier

## Overview
Starlink Notifier is an automated bot that fetches Starlink satellite visibility data from [FindStarlink](https://findstarlink.com) and posts updates on Instagram Stories when the satellites are visible in a specified location.

## Features
- Fetches real-time Starlink visibility data
- Automatically posts updates on Instagram Stories
- Customizable location settings
- Scheduled execution for continuous updates

## Requirements
- Python 3.x
- A virtual environment (recommended)
- The following Python libraries:
  - `requests`
  - `instagrapi`
  - `dotenv` (for environment variables)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Mario-Costa-42/Starlink-Alert.git
   cd Starlink-Notifier
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the bot manually:
```sh
python main.py
```

To schedule automatic execution, use a task scheduler like `cron` (Linux/macOS) or `Task Scheduler` (Windows).

## Contributing
Feel free to submit issues or contribute via pull requests!

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For any inquiries, reach out via GitHub Issues or email at `gearoftech2023@gmail.com`.

