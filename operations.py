import sys
from DatabaseIO import DatabaseIO


class ShapeDatabase:
    """
    Class representing a shape database.
    """
    def __init__(self):
        """
        Initialize the ShapeDatabase with an empty database and an error message.
        """
        self.db = []
        self.error_message = "Error: Database file not loaded or is empty, please load a detabase file"

    def load(self, file):
        """Load shapes from a file into the database."""
        print(f"loading <<{file}>>")
        self.db.extend(DatabaseIO.read(file))

    def to_set(self):
        """Convert the current database to a set, removing any duplicates."""
        if not self.db_exist():
            return None
        else:
            print("converting current database in memory to a set")
            old_size = len(self.db)
            self.db = list(set(self.db))
            new_size = len(self.db)
            duplicates = old_size - new_size
            print("conversion successful")
            print(f"{duplicates} duplicate(s) were found and removed")
            return self.get_db()

    def save(self, file_path):
        """Save the current database to a file."""
        if not self.db_exist():
            return None
        else:
            database = DatabaseIO(self.db.copy())
            database.save(file_path)

    def print_db(self):
        """Print all shapes in the database."""
        if not self.db_exist():
            return None
        else:
            print("printing database...")
            for data in self.db:
                print(data.print())

    def summary(self):
        """Print summary statistics of the database."""
        if not self.db_exist():
            return None
        else:
            stats = self.getstats()
            print("printing the database statistics")
            for key, value in stats.items():
                print(f"{key}: {value}")

    def details(self):
        """Print details of all shapes in the database."""
        if not self.db_exist():
            return None
        else:
            print(f"printing the database details")
            for data in self.db:
                print(DatabaseIO.format_data(data))

    @staticmethod
    def quit_program():
        """Terminate the program."""
        print("terminating the program")
        sys.exit(0)

    def getstats(self):
        """Return a dictionary of shape statistics from the database."""
        print(f"processing the database...")
        stats = {"Circle(s)": 0, "Ellipse(s)": 0, "Rhombus(es)": 0, "Shape(s)": 0}
        name_to_key = {
            "Shape": "Shape(s)",
            "Circle": "Circle(s)",
            "Ellipse": "Ellipse(s)",
            "Rhombus": "Rhombus(es)"
        }
        for data in self.db:
            name = data.__class__.__name__
            if name in name_to_key:
                stats[name_to_key[name]] += 1
            else:
                print(f"Unknown shape type: {name}")
        return stats

    def db_exist(self):
        """
        Check if the database exists (contains shapes).
        """
        return len(self.db) > 0

    def get_db(self):
        """
        Get a copy of the current database.
        """
        return self.db.copy()

    def get_message(self):
        """
        Get the last error message.
        """
        return self.error_message


DB = ShapeDatabase()


class LoadOperation:
    @staticmethod
    def execute(query):
        DB.load(query[1])


class ToSetOperation:
    @staticmethod
    def execute(query):
        if DB.to_set() is None:
            print(DB.get_message())


class SaveOperation:
    @staticmethod
    def execute(query):
        if DB.save(query[1]) is None:
            print(DB.get_message())


class PrintDatabaseOperation:
    @staticmethod
    def execute(query):
        if DB.print_db() is None:
            print(DB.get_message())


class SummaryOperation:
    @staticmethod
    def execute(query):
        if DB.summary() is None:
            print(DB.get_message())


class DetailsOperation:
    @staticmethod
    def execute(query):
        if DB.details() is None:
            print(DB.get_message())


class QuitOperation:
    @staticmethod
    def execute(query):
        DB.quit_program()
