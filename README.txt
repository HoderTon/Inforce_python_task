[base address: http://localhost:8000]
1. Creating restaurant
    Endpoint: "/api/create_restaurant" (POST)
    Payload: name

2. Uploading menu for restaurant (There should be a menu for each day)
    Endpoint: "api/menus" (POST)
    Payload: Menu name, Dishes, Restaurant, Day

3. Getting current day menu
    Endpoint: "menus/most_voted" (GET)

4. Getting results for the current day
    Endpoint: "menus/today_menus" (GET)

5. Employees will vote for the menu
    Endpoints: "api/menus" (GET)
               "api/menus/<menu id>/vote" (POST)
    # each employee can vote only once for one menu

* Checkout particular menu (GET) or delete (DELETE) it
    Endpoint: "menus/<menu id>" (GET/DELETE)

