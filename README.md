# Project Title

Club Drukarnia - this is my first fully functional project of restaurant website consisting of 4 applications:
* account app- to create new users (employees), log in/ log out options, change personal details and create new menu/reservation positions.
* menu app- responsible for dynamic creation of menu (beverages, cocktails, snacks etx.) with a description and prize. 
* reservation app - for booking tables in the restaurant, with the possibility of editing the reservation as well as removing it.
* blog - (in progress).

### Installing

Make sure that you have installed [Python] before you try to run this application.

1. Clone this repository using command:

```
git@github.com:gentlemil/drukarnia-club.git
```
2. Then, go to folder named 'restaurant'.

```
cd ./restaurant
```
3. Download the project dependencies with:
```
pip install -r requirements.txt
```
4. Finally, to debug a django project run:
```
python manage.py runserver
```
with DEBUG set to True in settings.py.

5. Your application will run at [http://localhost:3000].

## Deployment

Check the final effect of my work clicking link below:
```
https://drukarnia-club.herokuapp.com/
```

## Built With

* [Python] - programming language used
* [Django] - the web framework used
* [SQLite] - database used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
