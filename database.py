import sqlite3

def connect_db():
    """Create contacts table if it doesn't exist."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_contact(name, phone, email, address):
    """Add a new contact to the database."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)", 
                       (name, phone, email, address))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Phone number must be unique!")
    conn.close()

def view_contacts():
    """Retrieve all contacts."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def search_contact(search_term):
    """Search for contacts by name or phone."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", 
                   ('%' + search_term + '%', '%' + search_term + '%'))
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def update_contact(contact_id, name, phone, email, address):
    """Update contact details."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?", 
                   (name, phone, email, address, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    """Delete a contact by ID."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

# Initialize the database
connect_db()
