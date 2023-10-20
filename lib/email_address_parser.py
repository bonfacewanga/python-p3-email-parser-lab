import re

class EmailAddressParser:
    def __init__(self, addresses_string):
        self.addresses_string = addresses_string

    def parse(self):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        extracted_addresses = re.findall(email_pattern, self.addresses_string)

        unique_addresses = sorted(set(extracted_addresses))
        return unique_addresses