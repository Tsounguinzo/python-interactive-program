from Shapes import Shape, Circle, Rhombus, Ellipse


class DatabaseIO:
    """
    Class for reading and saving shape data to a file.
    """
    def __init__(self, db):
        """
        Initializes the DatabaseIO with the given shape database.
        """
        self.shapeDB = db

    @staticmethod
    def read(file_path):
        """
        Reads shape data from a file and returns a generator of shape objects.
        """
        try:
            line_count = 0
            error_count = 0
            shape = ShapeFactory()
            with open(file_path, "r") as shapeDB:
                print(f"processing <<{file_path}>>")
                for line in shapeDB:
                    line_count += 1
                    data = line.strip().split(' ')
                    try:
                        yield shape.create_shape(data)
                    except ValueError:
                        error_count += 1
                        print(f"Error: Invalid {data[0].capitalize()} on line {line_count}: {line.strip()}")

            print(f"Processed {line_count} row(s), {line_count - error_count} shape(s) added, {error_count} error(s).")

        except FileNotFoundError:
            print(f'The file {file_path} does not exist.')
        except PermissionError:
            print(f'Insufficient permissions to read the file {file_path}.')
        except IsADirectoryError:
            print(f'The path {file_path} is a directory, not a file.')
        except OSError as e:
            print(f'An OS error occurred while trying to read the file {file_path}: {str(e)}')

    def save(self, file_path):
        """ Writes formatted shape data to a file. """
        print(f"saving database to <<{file_path}>>")
        try:
            with open(file_path, "w") as db:
                row_count = 0
                for data in self.shapeDB:
                    row_count += 1
                    fdata = DatabaseIO.format_data(data)
                    print(fdata, file=db)

            print(f"saved {row_count} row(s) in <<{file_path}>>")

        except FileNotFoundError:
            print(f'The file {file_path} does not exist.')
        except PermissionError:
            print(f'Insufficient permissions to write to the file {file_path}.')
        except IsADirectoryError:
            print(f'The path {file_path} is a directory, not a file.')
        except OSError as e:
            print(f'An OS error occurred while trying to write to the file {file_path}: {str(e)}')

    @staticmethod
    def format_data(data):
        """ Formats shape data into a string for writing to a file. """
        class_name = data.__class__.__name__
        if class_name == "Shape":
            return f"{str(class_name).lower()}"

        elif class_name == "Circle":
            return f"{str(class_name).lower()} {int(data.radius)}"

        elif class_name == "Ellipse":
            return f"{str(class_name).lower()} {int(data.semi_minor)} {int(data.semi_major)}"

        elif class_name == "Rhombus":
            return f"{str(class_name).lower()} {int(data.diagonal1)} {int(data.diagonal2)}"


class ShapeFactory:
    """
    Factory class for creating shape objects.
    """
    def __init__(self):
        """
        Initializes the ShapeFactory with valid shape names.
        """
        self.valid_names = ["shape", "rhombus", "circle", "ellipse"]

    def create_shape(self, data):
        """
        Creates a shape object based on the given data.
        """
        if not self.isvalid(data):
            raise ValueError(f'Invalid data: {data}')

        data_name = data[0]
        if data_name == "shape":
            return Shape()
        elif data_name == "rhombus":
            return Rhombus(data[1], data[2])
        elif data_name == "ellipse":
            return Ellipse(data[1], data[2])
        else:
            return Circle(data[1])

    def isvalid(self, data):
        """
        Checks if the given data is valid for creating a shape object.
        """
        data_name = data[0]
        if data_name in self.valid_names:
            if data_name == "shape":
                return len(data) == 1
            if data_name == "rhombus" or data_name == "ellipse":
                return len(data) == 3 and int(data[1]) > 0 and int(data[2]) > 0
            if data_name == "circle":
                return len(data) == 2 and int(data[1]) > 0
        else:
            return False
