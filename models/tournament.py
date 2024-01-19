import json
import os


class Tournament:
    """
    A class to represent a chess tournament.

    This class handles the creation and management of a chess tournament,
    including details like name, dates, venue, rounds, players, etc.
    """

    # Default directory for saving tournament data
    DEFAULT_DIRECTORY = "/Users/waltercueva/PycharmProjects/Chess-Club-Application/data/tournaments"

    def __init__(self, filename=None, **kwargs):
        """
        Initializes a new tournament either from a JSON file or from provided arguments.

        :param filename: Filename for the JSON file to load/save tournament data.
        :param kwargs: Keyword arguments for tournament attributes.
        """
        self.filename = filename
        self.filepath = os.path.join(self.DEFAULT_DIRECTORY, filename) if filename else None
        self.tournament_data = {}

        if self.filepath and os.path.exists(self.filepath):
            self.load_from_file()
        else:
            self.tournament_data = kwargs
            if self.filepath:
                self.save()

    def load_from_file(self):
        """
        Loads tournament data from a JSON file.
        """
        with open(self.filepath, 'r') as file:
            self.tournament_data = json.load(file)

    def save(self):
        """
        Saves the tournament data to a JSON file.
        """
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, 'w') as file:
            json.dump(self.tournament_data, file, indent=4)

    def update_tournament(self, **kwargs):
        """
        Updates the tournament details with provided keyword arguments.

        :param kwargs: Keyword arguments to update tournament attributes.
        """
        self.tournament_data.update(kwargs)
        self.save()

    def __str__(self):
        return f"Tournament: {self.tournament_data.get('name', 'Unnamed')}"
