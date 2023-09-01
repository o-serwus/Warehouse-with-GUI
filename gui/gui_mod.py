from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ModifyWindow(QDialog):
    def __init__(self, entry, database):
        super().__init__()
        self.entry = entry
        self.database = database
        self.setWindowTitle("Modify Entry")

        self.id_label = QLabel("ID: ")
        self.id_lineedit = QLineEdit()
        self.id_lineedit.setText(str(entry[0]))
        self.id_lineedit.setReadOnly(True)

        self.title_label = QLabel("Title: ")
        self.title_lineedit = QLineEdit()
        self.title_lineedit.setText(str(entry[1]))

        self.category_label = QLabel("Category: ")
        self.category_lineedit = QLineEdit()
        self.category_lineedit.setText(str(entry[2]))

        self.price_label = QLabel("Price: ")
        self.price_lineedit = QLineEdit()
        self.price_lineedit.setText(str(entry[3]))

        self.description_label = QLabel("Description: ")
        self.description_lineedit = QLineEdit()
        self.description_lineedit.setText(str(entry[4]))

        self.entry_date_label = QLabel("Entry date: ")
        self.entry_date_lineedit = QLineEdit()
        self.entry_date_lineedit.setText(str(entry[5]))

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_changes)

        layout = QVBoxLayout()
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_lineedit)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_lineedit)
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_lineedit)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_lineedit)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_lineedit)
        layout.addWidget(self.entry_date_label)
        layout.addWidget(self.entry_date_lineedit)
        layout.addWidget(self.save_button)

        self.setLayout(layout)


    def save_changes(self):
        id = int(self.id_lineedit.text())
        title = self.title_lineedit.text()
        category = self.category_lineedit.text()
        price = float(self.price_lineedit.text())
        description = self.description_lineedit.text()
        date_added = self.entry_date_lineedit.text()

        modified_entry = (id, title, category, price, description, date_added)

        self.database.modify_entry(id, modified_entry)
        self.accept()


