import random


class CSV:
    """
    CSV class for reading, transforming, and exporting CSV data to JSON.
    """

    def __init__(self, in_file, out_file):
        """
        Initializes a CSV instance.

        Args:
        in_file (str): The input CSV file path.
        out_file (str): The output JSON file path.
        """
        self.in_file = in_file
        self.out_file = out_file
        self.headers = []
        self.data = []

    def read(self):
        """
        Reads the CSV file and extracts headers and data.

        Returns:
        None
        """
        with open(self.in_file, 'r', encoding='utf-8') as file:
            content = file.readlines()
            self.headers = content[0].strip().split(',')

            self.data = [line.strip().split(',') for line in content[1:]]

    def transform(self):
        """
        Transforms CSV data into JSON format.

        Returns:
        str: JSON content representing the transformed data.
        """
        self.read()
        json_content = "{\n  \"Buecher\": [\n"

        for row in self.data:
            json_content += '    {\n'
            for i in range(len(self.headers)):
                header = self.headers[i].strip(' ')
                title = row[i].strip(' "')

                if header == 'Veröffentlichungsjahr':
                    header = 'Veroeffentlichungsjahr'

                json_content += f'     "{header}": "{title}",\n'

            if 'ISBN' not in self.headers:
                isbn = f'     "ISBN": "{random.randint(1000000000, 9999999999)}",\n'
                json_content += isbn

            if 'Bewertung' not in self.headers:
                bewertung = f'     "Bewertung": "{random.uniform(1.0, 5.0):.1f}"\n'
                json_content += bewertung

            json_content += '    },\n'

        json_content = json_content.rstrip(',\n') + '\n  ]\n}\n'
        return json_content

    def export(self):
        """
        Exports the transformed data to a JSON file.

        Returns:
        None
        """
        content = self.transform()
        with open(self.out_file, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    """
    Main function to demonstrate CSV to JSON transformation.

    Returns:
    None
    """
    csv = CSV('../data/data.csv', '../data/data.json')
    csv.export()


if __name__ == '__main__':
    main()
