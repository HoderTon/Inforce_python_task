
# When using JWT authentication, the client side stores the token and attaches it to every request

* Register
    Endpoint: "/auth/register/" (POST)
    body: username, password, password2

* Login
    Endpoint: "/auth/login/" (POST)
    body: username, password (as a dict)

    # In response you'll get refresh and access tokens which will grand you access to api endpoints
    # Access token expires in 5min, then you'll need to get new one using refresh token "/auth/login/refresh".

* Refresh
    Endpoint: '/auth/login/refresh/' (POST)
    body: refresh
    # Refresh token expires in 24 hours. If you won't use it during this time - you'll need to login again.

1. Creating restaurant
    Endpoint: "/api/create_restaurant" (POST)
    Payload: name

2. Uploading menu for restaurant (There should be a menu for each day)
    Endpoint: "/api/menus" (POST)
    Payload: menu_name, dishes, restaurant, day

3. Getting current day menu
    Endpoint: "/menus/most_voted" (GET)

4. Getting results for the current day
    Endpoint: "/menus/today_menus" (GET)

5. Employees will vote for the menu
    Endpoints: "/api/menus" (GET)
               "/api/menus/<menu id>/vote" (POST)
    # each employee can vote only once for one menu

* Checkout particular menu (GET) or delete (DELETE) it
    Endpoint: "/menus/<menu id>" (GET/DELETE)




