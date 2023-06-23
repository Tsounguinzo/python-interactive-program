from operations import LoadOperation, ToSetOperation, SaveOperation, PrintDatabaseOperation, \
    SummaryOperation, DetailsOperation, QuitOperation

OPERATIONS_LIST = ["LOAD", "TOSET", "SAVE", "PRINT", "SUMMARY", "DETAILS", "QUIT"]


class ShapeDBApp:
    """
    Main application class for the Shape Database app.
    """

    def __init__(self):
        """
        Initializes the ShapeDBApp with the available operations.
        """
        self.operations = {
            "LOAD": LoadOperation,
            "TOSET": ToSetOperation,
            "SAVE": SaveOperation,
            "PRINT": PrintDatabaseOperation,
            "SUMMARY": SummaryOperation,
            "DETAILS": DetailsOperation,
            "QUIT": QuitOperation
        }

    def execute_query(self, query):
        """
        Executes the given query by identifying the operation and calling its execute method.
        """
        query_parts = query.strip().split(' ')
        operation_name = query_parts[0].upper()

        if operation_name not in OPERATIONS_LIST:
            print("Invalid Operation")
            return

        operation = self.operations.get(operation_name)
        if not operation:
            print("Invalid Operation")
            return

        try:
            if len(query_parts) == 1 and operation_name in {"LOAD", "SAVE"}:
                raise ValueError("File name required for LOAD/SAVE operation")
            elif len(query_parts) == 1 and operation_name not in OPERATIONS_LIST:
                raise ValueError("Only the LOAD/SAVE operation requires an argument")
            elif len(query_parts) == 2 and operation_name not in {"LOAD", "SAVE"}:
                raise ValueError("Invalide Operation")
            elif len(query_parts) > 2 or len(query_parts) <= 0:
                raise ValueError("Invalide Operation")
            else:
                operation.execute(query_parts)
        except ValueError as ve:
            print(ve)

    def print_operations(self):
        """
        Prints the available operations to the console.
        """
        for operation in OPERATIONS_LIST:
            if operation in {"LOAD", "SAVE"}:
                print(f"{operation} <<file>>")
            else:
                print(operation)

    def run(self):
        """
        Runs the ShapeDBApp by printing operations and executing queries in a loop.
        """
        self.print_operations()
        while True:
            query = input("Enter your operation: ")
            self.execute_query(query)


if __name__ == '__main__':
    app = ShapeDBApp()
    app.run()
