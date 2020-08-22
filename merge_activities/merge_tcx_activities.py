import file_service as fs
from lxml import etree
from tcx_activity import TCXActivity
import time

OUTPUT_DIR_NAME = 'output'
OUTPUT_FILE_NAME = f'merged_{str(int(time.time()))}.tcx'
NAME_SPACE = "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"


inputFolder = fs.get_input_dir()
inputFiles = fs.get_input_files(inputFolder)

outputFilePath = fs.get_output_file_path(inputFolder, OUTPUT_DIR_NAME, OUTPUT_FILE_NAME)

activities = []

for inputFile in inputFiles:
    tcx_activity = TCXActivity(inputFile)
    activities.append(tcx_activity)

activities.sort(key=lambda x: x.get_timestamp(), reverse=False)

distanceGap = 0

for activity in activities:
    activity.set_distance(distanceGap)
    distanceGap = activity.get_last_distance()

templateRoot = etree.parse(fs.get_template_path('template.tcx'))
templateActivity = templateRoot.getroot()[0][0]
templateActivity.append(activities[0].get_id_node())

for activity in activities:
    for lap_node in activity.get_lap_nodes():
        templateActivity.append(lap_node)

templateActivity.append(activities[0].get_creator_node())

templateRoot.write(outputFilePath)

print('wrote file: ' + outputFilePath)
