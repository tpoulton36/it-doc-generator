import sqlite3

DATABASE = "database/projects.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            doc_type TEXT NOT NULL,
            raw_notes TEXT NOT NULL,
            generated_docs TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

def save_project(project_name, doc_type, raw_notes, generated_docs):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO projects (
            project_name,
            doc_type,
            raw_notes,
            generated_docs
        )
        VALUES (?, ?, ?, ?)
    """, (project_name, doc_type, raw_notes, generated_docs))

    connection.commit()
    connection.close()


def get_projects():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, project_name, doc_type, created_at
        FROM projects
        ORDER BY created_at DESC
    """)

    projects = cursor.fetchall()
    connection.close()

    return projects

    connection.commit()
    connection.close()

def get_project(project_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM projects
        WHERE id = ?
    """, (project_id,))

    project = cursor.fetchone()
    connection.close()

    return project

def delete_project(project_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM projects
        WHERE id = ?
    """, (project_id,))

    connection.commit()
    connection.close()