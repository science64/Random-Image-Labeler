__author__ = "Süleyman Bozkurt"
__version__ = "1.0.0"
__maintainer__ = "Süleyman Bozkurt"
__email__ = "sbozkurt.mbg@gmail.com"
__date__ = '23.03.2022'

import glob
import random
import pandas as pd
import os
from datetime import datetime
import shutil

def main():
    print('[*] Random Image labeler started!')

    columns = ["Image Original Name", "Image Random Name"]

    out_df = pd.DataFrame(columns=columns)

    try:
        images = glob.glob('./Images/*.jpg') + glob.glob('./Images/*.png') + glob.glob('./Images/*.tif') + glob.glob('./Images/*.tiff') + glob.glob('./Images/*.jpeg')

        randomNumberList = random.sample(range(1,len(images)+1), len(images))

        now = datetime.now()

        num = 0
        for image in images:
            imageTemp = image.split('\\')[1]
            imageName, imageExtension = os.path.splitext(imageTemp)
            imageExtension_with_dot = '.' + str(imageExtension[1:])
            shutil.copy(image,f'./RandomName/{randomNumberList[num]}{imageExtension_with_dot}')

            cache = {
                "Image Original Name": imageName,
                "Image Random Name": randomNumberList[num],
            }

            out_df = out_df.append(cache, ignore_index=True)
            num += 1

        out_df.to_excel(f'output_{now.strftime("%d%m%Y")}.xlsx', index=False)

        print('[*] Finished! Check "RandomName" folder for renamed images!')

    except Exception as e:
        print(f'[*] Error: {e}')

if __name__ == '__main__':
    main()
    input('[*] Press any key to quit!')
