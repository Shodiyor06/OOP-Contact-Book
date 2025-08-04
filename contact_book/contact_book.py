import json
from rich.console import Console
from rich.table import Table
from contact_book.models.contact import Contact
from contact_book.services.db import DB


class ContactBook:

    def __init__(self):
        self.console = Console()
        self.db = DB()

    def print_menu(self):
        self.console.print('[bold italic yellow on red blink]\n======== Menu ========')
        self.console.print(
            '1. Add New Contact\n'
            '2. Show All Contacts\n'
            '3. Search Contact\n'
            '4. Update Contact\n'
            '5. Delete Contact\n'
            '6. Exit\n'
        )

    def add_contact(self):
        self.console.print("[bold green]Enter A New Contact Information")
        name = input("Name: ").strip().title()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()

        self.db.add_contact(name, phone, email)

    def print_contacts(self):
        table = Table(title="[bold blue]Contacts Table")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Phone", justify="right", style="green")
        table.add_column("Email", style="blue")

        for contact in self.db.get_contacts():
            table.add_row(
                contact.contact_id,
                contact.name,
                contact.phone,
                contact.email
            )

        self.console.print(table)

    def remove_contact(self):
        search = input("Search: ").strip().lower()
        if self.db.remove_contact(search):
            print("uchirildi")
            
                

    def update_contact(self):
        search = input("Search: ").lower()
        contact = self.db.get_contacts(name)
        for i in self.db.get_contacts():
            if i.name.lower() == search:
                self.console.print("[bold green]Update Contact Information")
                name = input("Name: ").strip().title()
                phone = input("Phone: ").strip()
                email = input("Email: ").strip()
                data = {
                    'name': name,
                    'phone': phone,
                    'email': email
                }
                self.db.update_contact(contact, data)
                self.console.print(f"[bold blue]Contact {i.name} yangilandi[/bold blue]")
                return

    def search_contact(self):
        search = input("Search: ").strip().lower()
        
        table = Table(title="[bold blue]Found Contacts Table")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Phone", justify="right", style="green")
        table.add_column("Email", style="blue")

        for contact in self.db.get_contacts():
            if search in contact.name.lower() or search in contact.email.lower() or search in contact.phone:
                table.add_row(
                    contact.contact_id,
                    contact.name,
                    contact.phone,
                    contact.email
                )

        self.console.print(table)

    def run(self):
        print("salom, Contact Book Projectga Xush Kelibsiz!")
        while True:
            self.print_menu()

            choice = input("> ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.print_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.remove_contact()
            elif choice == '6':
                self.console.print("[bold red]dastur tugadi[/bold red]")
                break
