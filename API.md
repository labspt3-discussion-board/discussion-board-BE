# Lambda Forum API

### https://discussion-board-api-test.herokuapp.com/api/

## Endpoints

#### User Endpoints

| Method | Endpoint                 | Description                  |
|--------|--------------------------|------------------------------|
| GET    | `/users/`                | Returns a list of all users  |
| GET    | `/users/:id/`            | Returns user by id           |
| PUT    | `/users/:id/`            | Updates user by id           |
| DELETE | `/users/:id/`            | Deletes user by id           |

#### Subforum Endpoints

| Method | Endpoint                      | Description                                     |
|--------|------------------------------ |-------------------------------------------------|
| GET    | `/subforums/`                 | Returns a list of all subforums                 |
| GET    | `/subforums/:id/`             | Returns subforum by id                          |
| PUT    | `/subforums/:id/`             | Updates subforum by id                          |
| DELETE | `/subforums/:id/`             | Deletes subforum by id                          |
| GET    | `/subforums/:id/members/`     | Returns members that belong to :id subforum     |
| GET    | `/subforums/:id/discussions/` | Returns discussions that belong to :id subforum |

#### Discussion Endpoints

| Method | Endpoint                     | Description                                     |
|--------|------------------------------|-------------------------------------------------|
| GET    | `/discussions/`              | Returns a list of all discussions               |
| GET    | `/discussions/:id/`          | Returns discussion by id                        |
| PUT    | `/discussions/:id/`          | Updates discussion by id                        |
| DELETE | `/discussions/:id/`          | Deletes discussion by id                        |
| GET    | `/discussions/:id/comments/` | Returns comments that belong to :id discussion  |
| GET    | `/topdiscussions/`           | Returns discussions ordered by highest upvote   |

#### Comment Endpoints

| Method | Endpoint                 | Description                    |
|--------|--------------------------|--------------------------------|
| GET    | `/comments/`             | Returns a list of all comments |
| GET    | `/comments/:id/`         | Returns comment by id          |
| PUT    | `/comments/:id/`         | Updates comment by id          |
| DELETE | `/comments/:id/`         | Deletes comment by id          |

#### User to Subforum Endpoints

| Method | Endpoint                 | Description                                       |
|--------|--------------------------|---------------------------------------------------|
| GET    | `/usertosubforum/`       | Returns a list of all comments                    |
| POST   | `/usertosubforum/`       | Adds User and Subforum id to UserToSubforum Table |
