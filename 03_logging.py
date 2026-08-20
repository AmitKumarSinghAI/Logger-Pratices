import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("employee.log")

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):

        self.first = first
        self.last = last

        logger.info(
            f"Created employee: {self.fullname}"
        )

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp1 = Employee("Amit", "Singh")
emp2 = Employee("John", "Smith")
