# flask-project-structure


# Install package
You need install package at first.
```
pip3 install -r requirement.txt
```

# Create MongoDb at local

```
docker-compose up -d
```
# Add Command in manage.py
You can add any command in manage.py .
Also can see all command from this command.

```
python manage.py
```

# How do run service
```
python manage.py runserver
```

Service will startup, port is 5000.

## List of Routes
<table>
    <tr>
        <td>Request</td>
        <td>Endpoint</td>
        <td>Detail</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>http://localhost:5000/users/</td>
        <td>Get all users.(todo)</td>
    </tr>
</table>