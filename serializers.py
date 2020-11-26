import messages as msg
import pickle
import csv
import json


class Serializers:
    def __init__(self, format=None):
        if format.upper() not in ('JSON', 'PICKLE', 'CSV'):
            raise ValueError(msg.MSG_INCORRECT_DATA_FORMAT)

        self.format = format
        if self.format == 'JSON':
            self.load = self._load_json
            self.save = self._save_json
        elif self.format == 'PICKLE':
            self.load = self._load_pickle
            self.save = self._save_pickle
        elif self.format == 'CSV':
            self.load = self._load_csv
            self.save = self._save_csv

    def _load_json(self, file=None, **kwargs):
        if file is None:
            raise ValueError(msg.MSG_INCORRECT_FILE_NAME)
        with open(file, 'rt') as f:
            return json.load(f)

    def _save_json(self, file, data, **kwargs):
        with open(file, 'wt') as f:
            return json.dump(data, f, **kwargs)

    def _load_pickle(self, file=None, **kwargs):
        if file is None:
            raise ValueError(msg.MSG_INCORRECT_FILE_NAME)
        with open(file, 'rb') as f:
            return pickle.load(f)

    def _save_pickle(self, file, data, **kwargs):
        with open(file, 'wb') as f:
            return pickle.dump(data, f, **kwargs)

    def _load_csv(self, file=None, **kwargs):
        if file is None:
            raise ValueError(msg.MSG_INCORRECT_FILE_NAME)
        with open(file, 'rt') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_MINIMAL)
            data = {}
            for row in reader:
                data[row[0]] = row[1]
            return data

    def _save_csv(self, file, data, **kwargs):
        with open(file, 'wt') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            for name, value in data.items():
                writer.writerow([name, value])

    def load(self, file, **kwargs):
        pass

    def save(self, file, data, **kwargs):
        pass
