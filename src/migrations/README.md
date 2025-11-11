---

## 🧭 Alembic Migration Command Guide

Alembic is used to handle **database schema migrations** in our project.
Below are the most commonly used commands during development.

---

### ⚙️ **Setup & Initialization**

**1️⃣ Create Alembic environment (done once per project):**

```bash
alembic init migrations
```

> This creates a `migrations/` folder containing env scripts and version files.

---

### 🧱 **Creating Migrations**

**2️⃣ Generate a new migration (auto-detect model changes):**

```bash
alembic revision --autogenerate -m "add user table"
```

> This compares your SQLAlchemy models with the current DB schema and generates a migration file in `migrations/versions/`.

**3️⃣ Create an empty migration (manual SQL/DDL changes):**

```bash
alembic revision -m "manual migration"
```

---

### 🚀 **Applying Migrations**

**4️⃣ Apply all migrations up to latest (head):**

```bash
alembic upgrade head
```

**5️⃣ Apply up to a specific version:**

```bash
alembic upgrade <revision_id>
```

> You can find `<revision_id>` in your migration file name or via `alembic history`.

---

### 🔙 **Reverting Migrations**

**6️⃣ Roll back the last migration:**

```bash
alembic downgrade -1
```

**7️⃣ Roll back to a specific version:**

```bash
alembic downgrade <revision_id>
```

**8️⃣ Roll back everything (to base):**

```bash
alembic downgrade base
```

---

### 🔍 **Inspection & Debugging**

**9️⃣ Show current DB version:**

```bash
alembic current
```

**🔟 Show migration history (all revisions):**

```bash
alembic history
```

**11️⃣ Show latest revision(s):**

```bash
alembic heads
```

**12️⃣ Show the current branch (if multiple heads exist):**

```bash
alembic branches
```

---

### 🧩 **Miscellaneous**

**13️⃣ Stamp the database with a specific version (without running migrations):**

```bash
alembic stamp head
```

> Useful when syncing DB state manually after schema reset.

**14️⃣ Check generated SQL (dry run, no execution):**

```bash
alembic upgrade head --sql
```

---

### 🧠 **Pro Tips**

* Always verify generated migrations before committing:

  ```bash
  alembic revision --autogenerate -m "description"
  ```

  Then open the new file in `migrations/versions/` and check all `op.create_table`, `op.add_column`, etc.
* Use clear, descriptive messages for each migration:

  ```bash
  alembic revision --autogenerate -m "add role and group relationship tables"
  ```
* Keep your models and database always in sync to avoid merge conflicts.

---
