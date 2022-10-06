# Author:- Anurag Gupta Email:- 999.anuraggupta@mail.com
from flask import Flask, render_template 
import pandas as pd
###-STEP 1 DOWNLOAD DATA
# See details of API at:- https://aqicn.org/api/


my_data = pd.read_csv('./prediction3.csv')

data_dict = { 
    "lat": my_data['midpoint_lat'],
    'lon': my_data['midpoint_long'],
    'aqi': my_data['Label']
}
df = pd.DataFrame(data_dict)

sending_data = [list(df['lat']),list(df['lon']),list(df['aqi'])]
app = Flask(__name__)
@app.route('/')
def home(): 
    return render_template('index.html', data = sending_data)



if __name__ == '__main__':
  app.run()