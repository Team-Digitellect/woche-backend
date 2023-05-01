## Database Setup
- psql -U <username> -d <database_name> -f woche.sql
- psql -U postgres -f woche.sql

## Endpoints Documentations
Route: `/auth/signup`
>Method: POST
>Parameters:
```
{
    "username":" ",
    "email":" ",
    "password":" "
}
```

Route: `/auth/login`
>Method: POST
>Parameters:
```
{
    "email":" ",
    "password":" "
}
```

Route: `/api/table`
>Method: GET
>Parameters: 
 - N/A
>Response: All tables for that user

Route: `/api/table/create`
>Method: POST
>Parameters:
```
{
    "table_name":"my Table"
}
```
>Response:
```
{
    "data": {
        "id": "fcb4bb0b-1b2f-46f2-aacb-69ff0859918e",
        "name": "my Table",
    },
    "message": "Table created successfully"
}
```

Route: `/api/table/tableid`
    - To add items to a particular table
>Method: POST
>Parameters:
```
{
    "name":"Rice",
    "type":"FoodStuff"
}
```
>Response:
```
{
    {
        "id": "1c9057fa-1482-406a-9794-91554e633083",
        "name": "Rice",
        "table_id": "fcb4bb0b-1b2f-46f2-aacb-69ff0859918e",
        "type": "FoodStuff"
    },

    "success": true
}
```

Route: `/api/table/tableid`
    - To get a particular table data
>Method: POST
>Parameters: N/A
>Response:
```
{
    "Table": {
        "id": "fcb4bb0b-1b2f-46f2-aacb-69ff0859918e",
        "name": "my Table"
    },
    "items": [
        {
            "id": "1c9057fa-1482-406a-9794-91554e633083",
            "name": "Rice",
            "table_id": "fcb4bb0b-1b2f-46f2-aacb-69ff0859918e",
            "type": "FoodStuff"
        },
        {
            "id": "3759fc2b-d5ab-4071-8af9-cc9e4f5f0e6c",
            "name": "beans",
            "table_id": "fcb4bb0b-1b2f-46f2-aacb-69ff0859918e",
            "type": "FoodStuff"
        }
    ],
    "success": true
}
```
Route: `/api/table/tableid/item/itemid`
    - To update an item name
>Method: PUT
>Parameters:
```
{
    "name":"Palm oil"
}
```
>Response:
```
{
    "message": "Item name updated successfully",
    "success": true
}
```

