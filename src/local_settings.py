from dotenv import dotenv_values
import os

secrets = dotenv_values(".secrets")

SLACK_APP_TOKEN = secrets.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = secrets.get("SLACK_BOT_TOKEN")

#test
# Unset proxy environment variables
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)
os.environ.pop('http_proxy', None)
os.environ.pop('https_proxy', None)

os.environ['HTTP_PROXY'] = "https://api.slack.com
os.environ['HTTPS_PROXY'] = "https://api.slack.com
os.environ['http_proxy'] = "https://api.slack.com
os.environ['https_proxy'] = "https://api.slack.com




PLUGINS = (
    "lettuce.plugins.project.ProjectPlugin",
    "lettuce.plugins.repo.RepoPlugin",
    "lettuce.plugins.handle_messages.HandleMessagesPlugin",
    "lettuce.plugins.startup_message.StartupMessagePlugin",
    "lettuce.plugins.update_server.UpdateServerPlugin",
    "lettuce.plugins.welcome.welcome.WelcomePlugin",
)

HTTP_PROXY = None
HTTPS_PROXY = None
