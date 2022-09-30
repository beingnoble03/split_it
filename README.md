## split_it
Expenses management app made using Django. Split payments, add groups, add transactions, manage your profile.

### How to access Split It?
> Deployed on Heroku: [Split It | Heroku](https://noble-split-it.herokuapp.com/)

OR If you want to run it locally follow these steps:

 - Clone this repository
 - Move to the cloned repository in your machine using cd command
 - Make sure you have python installed on your machine
 - Create a virtual environment using pipenv. To install pipenv run the following command `pip install pipenv`
 - Now initiat the virtual environment using `pipenv shell`
 - Once the virtual environment has been activated, install all the required packages given in the requirements.txt file by using the following command `pip3 install -r requirements.txt`
 - After installing all the packages, run this command `python manage.py runserver`
 - Now, you can access Split It running at `http://localhost:8000/`

### Features of the App
1. A minimilistic design
2. A Perfect Algo that minimizes the number of transactions in a Group 
3. Upload Group Images and change your Profile Image as per your requirements
4. Responsive design: Adjustable across all devices 
5. Statistics of all the transactions using ChartJS
6. Dashboard shows recent Transaction, Split Payments & Groups making it easy for a user to get an overview of the current situation.
7. Split Payments can be added as well as Individual Payments in a Group
8. A detailed Statistics Panel on Dashboard that gives all the important data in a singla tab.

### Note
Be sure to add all group members at once when creating a group. This is done to ensure all past split payments are not altered when a new member is added.

### Cloudinary and Postgres Implementation
The App is linked with Postgres Database instead of the default DB SQLite3 & All the media files are handled and stored on Cloudinary. This makes App seamless and all the data stored even when the Heroku's Dyno restarts.

### Some Screenshots

Statistics on Dashboard Page

![Statistics on Dashboard Page](https://i.ibb.co/Qvvt3g0/Screenshot-from-2022-03-18-17-08-12.png)

Profile Page

![Profile Page](https://i.ibb.co/wQXwf0t/Screenshot-from-2022-03-18-18-52-43.png)

Groups Page

![Groups Page](https://i.ibb.co/CvgdjfS/Screenshot-from-2022-03-18-19-00-10.png)

Group Details Page

![Group Details Page](https://i.ibb.co/x3QGJrf/Screenshot-from-2022-03-18-19-04-20.png)
