
# When using JWT authentication, the client side stores the token and attaches it to every request
# Authorization: Bearer <access token>

* Register
    Endpoint: "/auth/register/" (POST)
    Payload: username, password, password2

* Login
    Endpoint: "/auth/login/" (POST)
    Payload: username, password

    # In response you'll get refresh and access tokens which will grand you access to api endpoints
    # Access token expires in 5min, then you'll need to get new one using refresh token "/auth/login/refresh".

* Refresh
    Endpoint: '/auth/login/refresh/' (POST)
    Payload: refresh
    # Refresh token expires in 24 hours. If you won't use it during this time - you'll need to login again.

1. Creating restaurant
    Endpoint: "/api/create_restaurant" (POST)
    Payload: name

2. Creating menu for restaurant (There should be a menu for each day)
    Endpoint: "/api/menus" (POST)
    Payload: 1) menu_name (any text),
             2) dishes (any text),
             3) restaurant (indicate id of existing restaurant),
             4) day (first 2 characters, as "Mo", 'Tu' et c.)



3. Getting current day menu
    Endpoint: "/api/menus/most_voted" (GET)

4. Getting results for the current day
    Endpoint: "/api/menus/today_menus" (GET)

5. Employees will vote for the menu
    Endpoints: "/api/menus" (GET)
               "/api/menus/<menu id>/vote" (POST)
    # each employee can vote only once for one menu

* Checkout particular menu (GET) or delete (DELETE) it
    Endpoint: "/api/menus/<menu id>" (GET/DELETE)




