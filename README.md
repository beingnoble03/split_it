## split_it
IMG Winter Assignment Project made using Django. Split payments, add groups, add transactions, manage your profile
> Deployed on Heroku: [Split It | Heroku](https://noble-split-it.herokuapp.com/)

### Features of the App
1. A minimilistic design
2. A Perfect Algo that minimizes the number of transactions in a Group 
3. No Limit for the number of users in a Group 
4. Split Payments can be added as well as Individual Payments in a Group 
5. Upload Group Images and change your Profile Image as per your requirements
6. Statistics of all the transactions using ChartJS
7. Responsive design: Adjustable across all devices
8. Dashboard shows recent Transaction, Split Payments & Groups making it easy for a user to get an overview of the current situation.

### Cloudinary and Postgres Implementation
The App is linked with Postgres Database instead of the default DB SQLite3 & All the media files are handled and stored on Cloudinary. This makes App seamless and all the data stored even when the Heroku's Dyno restarts.
