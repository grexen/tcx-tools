from lxml import etree
from datetime import datetime

NAME_SPACE = 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'


class TCXActivity:

    def __init__(self, tcx_file):
        tree = etree.parse(tcx_file)
        root = tree.getroot()
        self.activity_node = root.find(f'.//{{{NAME_SPACE}}}Activity')
        self.distance = self.get_last_distance()

    def get_timestamp(self):
        id_element = self.activity_node.find(f'.//{{{NAME_SPACE}}}Id')
        time_object = datetime.strptime(id_element.text, '%Y-%m-%dT%H:%M:%S.%fZ')
        return time_object.timestamp()

    def get_last_distance(self):
        return float(self.activity_node.xpath('ns:Lap/ns:Track/ns:Trackpoint/ns:DistanceMeters', namespaces={'ns': NAME_SPACE})[-1].text)

    def set_distance(self, distance_to_add):
        for element in self.activity_node.xpath('ns:Lap/ns:Track/ns:Trackpoint/ns:DistanceMeters', namespaces={'ns': NAME_SPACE}):
            element.text = str(float(element.text) + distance_to_add)

    def get_lap_nodes(self):
        return self.activity_node.findall(f'.//{{{NAME_SPACE}}}Lap')

    def get_id_node(self):
        return self.activity_node.find(f'.//{{{NAME_SPACE}}}Id')

    def get_creator_node(self):
        return self.activity_node.find(f'.//{{{NAME_SPACE}}}Creator')

