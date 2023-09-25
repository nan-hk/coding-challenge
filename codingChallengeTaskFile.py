import pandas as pd
import os
import re
import datetime

folderPath = './'
videoPath = folderPath + 'Videos/'

# main function
def main():
    timestamps, labels = readCSVFile()
    df = readFileAndCreateDataFrame(timestamps,labels)
    df.to_csv('./result.csv', index=False)

def readCSVFile():
    df = pd.read_csv(folderPath + 'label_data.csv', encoding="ISO-8859-1")
    header = df.columns.tolist()
    firstColumn = df[header[0]]
    secondColumn = df[header[1]]
    return firstColumn, secondColumn

def calculateMinuteToSec(start, end):
    sec = 0
    startDate = datetime.datetime.strptime(start,
                               '%Y%m%d%H%M%S')
    endDate = datetime.datetime.strptime(end,
                               '%Y-%m-%d %H:%M:%S')
    duration = str(endDate - startDate)
    for value in duration.split(':'):
        sec = 60 * sec + int(value)
    return sec

def sortAscendingOrder(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            if array[j]['video'][6:-4] > array[j + 1]['video'][6:-4]:

                # swapping elements if elements are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

def createDataFrame(loca, vid, first, second, seconds):
    data = {'timestamp': first, 'label': second, 'location': loca, 'video_file': vid, 'seconds_into': seconds}
    df = pd.DataFrame(data)
    return df


def readFileAndCreateDataFrame(timestamps, labels):
    locations = []
    video_files = []
    videos_dict= []
    seconds_into = []
    
    subfolders = os.listdir(folderPath + 'Videos')
    for subfolder in subfolders:
        for root,dirs,filenames in os.walk(videoPath + subfolder):
            # save video and folder name as dict
            for file in filenames:
                video_dict = {}
                video_dict['video'] = file
                video_dict['location'] = subfolder
                videos_dict.append(
                    video_dict
                )
    sortedDictArray = sortAscendingOrder(videos_dict)
    
    for index, value in enumerate(sortedDictArray):
            
        if index < len(sortedDictArray) - 1:    
            cur_element = value['video'][6:-4]
            next_element = sortedDictArray[index + 1]['video'][6:-4]
            
            for file in timestamps:
                labeledTimestamp = re.sub('\ |\:|\-', '', str(file))
                # check labeled timestamp is within first video timestamp and second video timestamp
                if labeledTimestamp>= cur_element and labeledTimestamp< next_element:
                    locations.append(value['location'])
                    video_files.append(value['video'])
                    seconds_into.append(calculateMinuteToSec(cur_element, file))
                else:
                    pass
        else:
            for file in timestamps:
                labeledTimestamp = re.sub('\ |\:|\-', '', str(file))
                # check the record is greater than the last video or not 
                # (for not losing the data which timestamp is greater than the last video)
                if labeledTimestamp>= next_element:
                    locations.append(value['location'])
                    video_files.append(value['video'])
                    seconds_into.append(calculateMinuteToSec(cur_element, file))
    df = createDataFrame(locations, video_files, timestamps, labels, seconds_into)
    return df                 

if __name__=="__main__":
    main()