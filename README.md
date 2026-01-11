# RovMarq

RovMarq is a PySide6-based GUI application designed to coordinate and control system components through a central controller architecture.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/specapoorv/RovMarq.git
   ```

2. Navigate to the project directory:
   ```bash
   cd RovMarq
   ```

3. Install the requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

4. generate ssh-key on your laptop (to enable send feature)
   ```bash
   ssh-keygen -t ed25519
   ssh-copy-id orin@10.42.0.253
   ```
   this will create private and public key in your laptop and you are just sending it to orin so that it wont ask for password while doing scp 


---

## Running the Application

Start the main application using:
```bash
python3 main_coordinator.py
```

This launches the full GUI with backend coordination enabled.

---

## UI Development (PySide6 Designer)

### Opening the Designer
To edit the UI visually:
```bash
pyside6-designer
```

### Updating the UI Python File
After making changes in **PySide6 Designer**, regenerate the Python UI file:
```bash
pyside6-uic guiMain.ui -o frontend/gui_main_window.py
```

Always regenerate the UI file after modifying the `.ui` file, or changes will not reflect in the application.

---

## UI Testing (Without Backend Logic)

To verify the UI layout and appearance without running the full application:
```bash
python3 RovMarq/other/ui_test.py
```

This is useful for rapid iteration and layout validation.

---

## UI Design Notes

While working in PySide6 Designer, make sure to understand:
- Widget Promotion
- Proper usage of:
  - QLabel
  - QVBoxLayout / QHBoxLayout (Vertical / Horizontal Layouts)

Correct layout usage is essential for responsiveness and maintainability.

---

## Development Guidelines

Most development and modifications will typically be made in the following files:

- `bridge.py` – Interface between backend logic and GUI  
- `main_coordinator.py` – Application entry point and controller logic  
- `QMainWindow.py` – Main window logic and UI bindings  


---
