# Role‑Based Access Control (RBAC)

The library system defines four fine‑grained roles. Permissions are expressed as **module:action** pairs.

## Roles & Allowed Actions

| Role      | Module        | Allowed actions |
|-----------|---------------|-----------------|
| **Admin** | books, members, transactions, reports | create, read, update, delete, export |
| **Librarian** | books, members, transactions, reports | create, read, update, delete, export *(except `reports:delete`)* |
| **Member** | books, members | read |
|           | transactions | create, read |
|           | reports | export |
| **Guest** | books | read |

The matrix can be queried via `GET /rbac/roles` and the permission matrix via the service layer.
