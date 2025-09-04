import uuid

class UuidGenerator:

    def __init__(self):
        return
    
    def generate(self):
        raw_value = uuid.uuid1()
        split_raw = str(raw_value).split('-')
        return split_raw[0]