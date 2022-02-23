# We want to allow main.py to create an instance of this class for each profile it wants to track
class TwitterProfileScraper:

    """
    Docstring placeholder
    """
    name = ''
    twitter_user_url = ''

    def __init__(self, name, twitter_username):
        """
        Docstring placeholder
        """
        # Add checks for args
        self.name = name
        self.twitter_user_url = 'https://twitter.com/' + twitter_username
