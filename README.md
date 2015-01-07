# pyRandomUser
This project give you random user access from https://randomuser.me

First, Download randomuser.py in your project and import Randomuser
```
from randomuser import Randomuser
```

To request a single random user:
```
Randomuser.generate()
```

To request multiple random user, say 5 users:
```
Randomuser.generate(5)
```

**Note :** RandomUser.me limits multiple users in one API call to 500 in one query.

To request a single male random user:
```
Randomuser.generate_male()
```

To request multiple male random user:
```
Randomuser.generate_male(5)
```

To request a single female random user:
```
Randomuser.generate_female()
```

To request multiple female random user:
```
Randomuser.generate_female()
```

To request a specific user:
```
Randomuser.generate_seed("foobar")
```