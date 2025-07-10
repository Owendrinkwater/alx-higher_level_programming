# 0x0E. SQL - More queries

## 📚 Description

This project is part of the ALX Higher Level Programming curriculum.

It builds upon the basics of SQL to explore more advanced topics such as:
- Creating and managing MySQL users and privileges
- Working with constraints like `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, and `UNIQUE`
- Extracting and manipulating data using multiple tables
- Using `JOIN`, `UNION`, and subqueries to retrieve data
- Understanding relational database design through normalization and ER modeling

All tasks use MySQL 8.0 on Ubuntu 20.04 LTS.

---

## 🧠 Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

---

## 🛠️ Requirements

- MySQL 8.0 (tested on `8.0.25-0ubuntu0.20.04.1`)
- All files executed on Ubuntu 20.04 LTS
- SQL files must:
  - Start with a comment describing the task
  - Use `--` for single-line comments
  - Use **UPPERCASE** for SQL keywords
  - End with a new line
- Allowed editors: `vi`, `vim`, `emacs`
- All SQL queries tested with:
  ```bash
  cat <filename>.sql | mysql -hlocalhost -uroot -p <database_name>

