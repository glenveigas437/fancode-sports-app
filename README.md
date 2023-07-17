# Fancode Sports App

The App is built using **Python** and **Flask**

### Get Started

After cloning the repository
1) Create a Virtual Environment by running the command
```python3 -m venv fancode_sports_venv```

2) Activate the Virtual Environment by running the command
```source fancode_sports_venv/bin/activate```

3) Install the required libraries
```pip3 install -r requirements.txt```

4) Run all the migrations
```flask db upgrade```
```flask db migrate```

5) Run the Application
```python3 app.py```

The application runs on ```localhost:3000```

The running application 
<img width="1440" alt="Screenshot 2023-07-17 at 2 47 07 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/be087c98-3f43-4def-aa09-8f1df7b54a2f">

### Module Sport
1) POST
<img width="1440" alt="Screenshot 2023-07-17 at 2 56 23 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/d00bfa2f-7259-4f4e-9b91-a26e38bd858b">


2) GET
<img width="1440" alt="Screenshot 2023-07-17 at 2 50 16 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/aa2cad62-f2a7-4d76-b393-4439109e5fad">



### Module Tour
1) POST
<img width="1440" alt="Screenshot 2023-07-17 at 2 58 03 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/d49d4583-65a8-4662-aadb-3782ddfcd25b">

2) GET
<img width="1440" alt="Screenshot 2023-07-17 at 2 58 22 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/a5ed2218-783a-41f5-8664-6ba1d22b443c">



### Module Match
1) POST
<img width="1440" alt="Screenshot 2023-07-17 at 3 02 59 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/bfd9da63-5836-4d0a-835f-968c79b3c26a">

2) GET
<img width="1440" alt="Screenshot 2023-07-17 at 3 03 46 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/19083d2d-4e36-4026-9367-7a1e947dfdba">

3) Get All Matches of a Tour
Select the name of a Tour and it returns all the matches of that tour

<img width="1440" alt="Screenshot 2023-07-17 at 3 05 23 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/7d54f549-d496-47f1-9d88-93b1ec88c5cc">

4) Get all Sports, All Tours, All Matches
<img width="1440" alt="Screenshot 2023-07-17 at 3 07 14 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/5ba27990-898a-4bc6-85a0-140a5fbcacdd">



### Module News
1) Add News
<img width="1440" alt="Screenshot 2023-07-17 at 3 09 06 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/f980d755-2318-448d-8a90-212e9dbc575f">

2) Get news by Sport or Get news by Tour or Get News by match
Enter the match id, tour id or sport id and all relevant info with respect to the match, tour or sport is returned.
<img width="1440" alt="Screenshot 2023-07-17 at 3 10 11 PM" src="https://github.com/glenveigas437/fancode-sports-app/assets/31877827/ec874ab7-4d5a-4b68-a8c7-bb3ef2d9e956">


In order to reduce the latency of returning large amount of data I have made use of Pagination.


###  Run Tests
Create a new mysql db named ```test_db```

Run a particular test with the command
```ENV=Testing python3 -m unittest tests.news.test_news```

### Running the Docker file

1) Run the command
```docker build -t fancode-sports-app:latest .```
```docker run -d -p 3000:3000 fancode-sports-app```

The app will be running on localhost:3000


## Important
While running the app on your local system change the value of ```DB_HOST = localhost``` and while running the docker image change the value to ```host.docker.internal```
The base.sql file is the original file provided with this assignment and all the migrations are included in it.














