## split_it
IMG Winter Assignment Project made using Django. Split payments, add groups, add transactions, manage your profile.

### How to access Split It?
> Deployed on Heroku: [Split It | Heroku](https://noble-split-it.herokuapp.com/)

OR If you want to run it locally follow these steps:

 - Clone this repository
 - Move to the cloned repository in your machine using cd command
 - Make sure you have python installed on your machine
 - Create a virtual environment using pipenv. To install pipenv run the following command `pip install pipenv`
 - Now initiat the virtual environment using `pipenv shell`
 - Once the virtual environment has been activated, install all the required packages given in the requirements.txt file by using the following command `pip install Django asgiref backports.zoneinfo certifi cloudinary dj-database-url gunicorn Pillow psycopg2-binary six sqlparse urllib3 whitenoise`
 - After installing all the packages, run this command `python manage.py runserver`
 - Now, you can access Split It running at `http://localhost:8000/`

### Features of the App
1. A minimilistic design
2. A Perfect Algo that minimizes the number of transactions in a Group 
3. No Limit for the number of users in a Group 
4. Split Payments can be added as well as Individual Payments in a Group 
5. Upload Group Images and change your Profile Image as per your requirements
6. Statistics of all the transactions using ChartJS
7. Responsive design: Adjustable across all devices
8. Dashboard shows recent Transaction, Split Payments & Groups making it easy for a user to get an overview of the current situation.

### Note
Be sure to add all group members at once when creating a group. This is done to ensure all past split payments are not altered when a new member is added.

### Cloudinary and Postgres Implementation
The App is linked with Postgres Database instead of the default DB SQLite3 & All the media files are handled and stored on Cloudinary. This makes App seamless and all the data stored even when the Heroku's Dyno restarts.

### Some Screenshots
![Statistics on Dashboard Page](https://lh3.googleusercontent.com/g3y9eyclcP3j1yTN3EWR8doyXtC6fZE7wMKSfVNyf-2MEt2kJJad9xx6tHVFEBSoq6wyyTn8Kjan9tmqB8HFX8p7US87E0C8rFvQf6jlZtt3yRiwfCjCaMwoBnzjdoI37QJxafqZjUWvCSskQBDMViEnUhVyc7h95ml21NKKdeJglQtdYbHcJZQ4XwqOxOQghshuL-aAxyxSsatA7KVAQlSMVb7ASgKzli1R-UkwYYxmcCCgD56J6GWAAwbvDWnPtfWQJTt8AgW12F1KdXpyHgGgufP-Pckjtfjw4-18FK8OZBp7FL3NrmADH78AosiPjfstKa1RtEJ45DasUvQzNHBTDmqoEfzFhVzvJpCT8tT_I01Dxfp2_rnp1UapitijThUUSYYigABc5e3N54euaRBvYH0-cWRLqdetc2VVl0cIBaPM0roKTlK1W4jn9bDfr49xCxXovM92-NMyqVTe7J2VJ0cX7oL--LWx1Od2nLnp5kT3bU23bWGRQuWpAidxpnq7ShKH8JGaE5XD7bUk_pszq72kz6MDc5v6UfBmsUbsPqyKdXDClaVLCsWpdSBATqh8_bhivy4QhipANot0OnkbkxVw8LjbZgMpidudk3ijl_bu4iIUhHUIxGU8pNLSpqQi3qpLYnRg8KyDSxGKd-TQHVX1lRv2qgjcFz_VUXxtswvo2t5PRaA6-phIFlk5prOWfvLrY27avKsDQxLcmwGQWSie_K4kg8-gCwoYUWVdscsQfpTeL3STI6z2HRLp8fVu-ZY4DRJHe4Gdm9bEFcBPE8udwQyFbQ=w1818-h870-no?authuser=0)

![Profile Page](https://lh3.googleusercontent.com/xInIxHISBYitH0Bw9H7UAE9cxsV7Xyb81FFS_mD-s9FVoCJ8ALPs1DTzza4eNucQXMPfaNggX-yZg4P58Bk_243ocYbvIgnmjlt3W2TwID-olMxObJdwunrDwJyOH1rJhGweiFFxHhCJjP3m06mJSXBw5IXAo1LZbzqF8DpjIRzybZ2wABBVUNbeJTsxsDgnqqQcT_0RMady-vxwuAHF6A5b3UUse75Dv6OCDYB01Yg91ZSYrN8hXBDe2Af7dvlSNRxmMoSRUUPwrxMsIZQnHacv5dWombh6nLGHemp2EZfCYR2kh-kAmfsnJHy7ZRlaiTZBJ6hQfHWvoDxL8EpehYQ9M0jmy1_wlyQtKOTDlRY7PHCjF6M8QwhyW6r_SNfqZBqszSLQjQQNS8eKKaqeKGN1Z42BDpvdjximHD_NV_loRNgzZbJWGuxOtBxZfUGKBZUc3DmpDGJ081N9Iey7jppjyGf_ejC0iuxvbd9wj-jSjHzxRSf4538DRg4U9JxIlMT2oR1Wr09HAUlFq2WWjRMkvvWmM_G_YjEO02gTs7VAcfkYSSOTFiM6DPIdqTbDRLvR-BrlJ6dELFnjc1haJS7Pksx5QD4GjLDNnWhMj8sltUdeRMq9w_gdCMHLnEuvRCLRJC2WV1tkqETt9Y03s4R1k996rV49LR_fJMOdlJ_BaXT4iVUYu2Que3kkQTKihVMCicXI1Pd1h9v7QLWXPE21WkxB1NTA_uRZ7xaQZieTgmW8WS5PrpYMHkoS4ZtD58KSonIZXk86tkJBcSX74irFuDVJlu3fyw=w1834-h912-no?authuser=0)

![Groups Page](https://lh3.googleusercontent.com/AKEL2fnYjXTogNSK2HEZrqtWPuUC_LdNMH2lFXAq8fcAbKbgwsdQMWwkYbHRIULaxvmWlDYkwFbF1Mxfe8iFqceBYX0BNJhOlFecBQ5CrNPHPIEP65S0aWNjnoVnZdudr7LHW3YThiWIuh0Qq9reEFOQWpHeM-ec58MZ7-1ZFONnzmlLXE0H2KaL4aJ0uEa-kPQrMZ-oV0FZXDYjmrwaqto_9Yxf1YuyOZawRACg4XMh9-HCq-iJ2U8u2QJd2LrgAVUrpMCxoqA-qvnMlyQYu974S9_REoNVlF7XPr52qCGLAeOrSxA5QkbbQPyA11CqC-pteLwPkdabhKCoulUWsEUVMlzhZiHbXEj3mIHOUUjVsG67_auIuzBoEE5uaoZGmHUliQMEhu6dGCGjyilrtt_X2FoOOU4hSCss3Notbww8LM7Rh87mfYAbrwE5MNfk8OEwy2a3b-6e-zyjhpHrQNAIcyI98XHXw59qD6bBJ7_pKL7_k-LptSIMMuoY7chNZd3C9crmwZf2bG31hUJH10XcUm5PeYXsoPY-GGvsXm2WdeTK0ivb4__uxryg20M0lUuRydTgMrb8scAggUln1xqTjPX7OAUr5epz0zD0s4UdLwvDYBum8LxVbhORRBqkRBBx2ycC7SMipYBe46sv0dxFj2zLbMFEJfAxyYBuBpXL3CBMANQi-iYqjuJPWZ-BYIbOIxthz23WUG-Kyj2w65zctdR9UIRfGenEnyBdPbwLa9F0xgplNQxUY8ezzRuTgXVvdz6AzvH8v8IXvFuCIDaJDIn3muifbw=w1836-h915-no?authuser=0)

![Group Details Page](https://lh3.googleusercontent.com/vLDSL_2qjEgcHooq4Z2wh8WDA9KOak0yeJnrB-X1KDrKJ7VWIRr4wKkXDw9DL64mGt-GbPCU2WLAR-OYjGmFRvPxXwjq7KmD_6QmW7umo1ebJjp4SLcGc9o7EsxK7Wv0xtaDIT-U7QxeC9usRlhuv26YurcLBSxYrGnATQr60cm7e1N4ne7FgytQLR5TB5vKai7_0Bnjkzz2uYIl4G4jmEx14HfVwyzGpktCHXVjsf59poP4nfCPIbvf4x8hnk9agEqi9oBrMshOk8VqBMy1c-g8R3sW99Ap8nFu0l1snoBYz4td9EXb7gu7LClLrHNSb7NkgCwKxcAlae7MgpqOhNlUfBt0aTeXBOcBZPAEDw6fN80e1cXkCgt3k-dMOow6Q3GyA52x3c7HUaIcgDCvve_FFXPGYoRiJOaK82R6flIKGgCQ2p4CaSpvuxt3G_an871DFYBL8iHqF-Jx8SCsmh4_2a7XvABwXskzZMKtLVmYwJahaGeAPBog84fJlWoc9qF_wOxG4sr8tVvQZLK-Gc3qngs61dPHC--S1yb7_GN0FvJEPdq7faVhCA15n4OGpmpNP4-4aN23SxpjqbS7nh1mtoWZksZb4TjZFqWUMAjBBdCxOdsmUT4tIZoagOt-U-CLtNgx6wxK3xpdL_MU9pmJWff0uDbGlPOEnQRbkRSksxUQC8eSHr6z1JLOlx9UE9yiL4gqtZ0dbTiwJ8eeYYkUShuvFx30hH0RCkwyDAeuDMz1zJW3XN3PN6BDCaZdSk8kw5Gun50epvMomj3YW9gDKiUssMtHfQ=w1637-h920-no?authuser=0)
