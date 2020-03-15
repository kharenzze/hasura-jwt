## Init

Install hasura CLI [link](https://hasura.io/docs/1.0/graphql/manual/hasura-cli/install-hasura-cli.html#install-hasura-cli)

Run migrations:

```
cd hasura
hasura migrate apply
```

## Development

In order to run console:

```
cd hasura
hasura console
```

## Steps and decisions

* Disable console and use CLI, since it's better in order to work with migrations [link](https://hasura.io/docs/1.0/graphql/manual/migrations/new-database.html)

* [nginx template](https://github.com/agarzon/nginx-config)