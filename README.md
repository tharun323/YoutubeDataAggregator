# YoutubeDataAggregator
**---Features---**

-Used YouTube Data API for this task of Getting the Youtube Video and Channel Stats.

-Collected data from YouTube (Meta-data of Videos and Channel) for ten channels.
 Made sure that channels have active viewership, i.e. many people watch the videos on a daily basis.

-Track the increase/decrease in the statistics of video or channel, on a timely basis. 

-Used Python-Schedule for scheduling tasks.

-Used Logger to track all the logs of the Error responses.

-Used MatPlotLib to show the Graphical view of the stats of a particular Channel/Video.

-Created RestFulAPI using DjangoRestFramework with MySQL in Backend.

-Implemented SwaggerUI for the better diplay of API-UI.

-Implemented Aggrid in the Front-end using JavaScript with Ordering and Filtering Features.

**---Installation Steps---**

-Clone the Repository in to your local machine using [https://github.com/tharun323/YoutubeDataAggregator.git](url)

-Put the repo into a folder and in the root folder install the Virtual Environment and activate it using
  `virtualenv venv` and 
   goto `venv/Scripts/` and Activate the VirtualEnvironemnt using `activate`

-Then Goto datagg folder path and run the `manage.py` file using `python manage.py runserver` after the server starts running.

-Change the MySQL backend as per your requirements, settings present in `settings.py` Also change the Logfile path in the `Logger`     dictionary in `settings.py`

-Run the Migrations using `python manage.py migrate` and 'python manage.py makemigrations`

-Install the required Python Packages using the `requirements.txt file` using command `pip install -r requirements.txt`
   (this is found in the root folder)

-Link `http://127.0.0.1:8000/youtube/` will give the SwaggerUI Template to access the RESTAPI

**---Further Steps---**

-Load the Initial Data in to the data base (Channel List with id's) using  `python manage.py loaddata initialdata`

-Individually run the functions in the `data_req.py` file both for the `channel_stats` and `video_stats' or just uncomment the part in scheduling part in the `data_req.py` 

-Now goto `127.0.0.1:8000/youtube/home` for viewing the Home page of the App.





