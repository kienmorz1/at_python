# User Authentication

This project stores users in the `tasks_mgmt.User` model and uses bcrypt to
hash passwords. The password is not Django's built-in `auth.User` password:
this is a project-specific user model and a custom login endpoint.

## Password storage

The `User` model has a `password` field with a maximum length of 128
characters. Migration `0003_user_password` adds the field to the database.
Existing rows receive the migration default, an empty string; that default is
not a usable password and users must set a password before logging in.

`tasks_mgmt.utils.BcryptPasswordUtil` provides two static methods:

- `hash_password(password)` creates a salted bcrypt hash.
- `verify_password(password, hashed_password)` checks a password against its
  bcrypt hash.

Passwords are UTF-8 encoded. Bcrypt accepts at most 72 bytes, so the user and
login serializers reject longer values. A password's character count may be
less than 72 while its UTF-8 byte length is greater than 72.

The `UserSerializer` hashes passwords on user creation and password updates.
Its `password` field is write-only, so user API responses should not include
the password or its hash.

## Login endpoint

The login route is registered at `POST /api/login/`. Submit JSON containing an
email address and password:

```json
{
  "email": "person@example.com",
  "password": "your-password"
}
```

The `LoginSerializer` checks the email format and bcrypt password byte limit.
The login view should validate the serializer before reading
`validated_data`, find the user by email, and use
`BcryptPasswordUtil.verify_password` to check the submitted password. Do not
compare plaintext passwords or return stored password hashes.

## Existing accounts and migration

Apply the schema migration from the project directory:

```bash
python manage.py migrate
```

Accounts created before bcrypt hashing was added may have an empty, plaintext,
or otherwise non-bcrypt password value. Those values cannot be verified by
`verify_password`; set a new password through the user API (which hashes it)
or update the account password with `BcryptPasswordUtil.hash_password`.

## Current implementation caveat

`LoginViewSet` in `tasks_mgmt/views.py` currently includes the stored password
value in its success response. Remove that field before using the endpoint;
even a bcrypt hash is sensitive and should never be sent to API clients.
Return only non-sensitive account data, such as the user's ID and email.
