# Init db
```bash
flask db init
```

# Create migration
```bash
flask db revision -m "add_transaction"
```
Then edit on migration on `/migrations/versions/XXX_add_transaction.py`

# Upgrade/downgrade migration
```bash
flask db upgrade <revision>
# or
flash db downgrade <revision>
```

# See migration history
```bash
flask db history
```
