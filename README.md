# 🍬 Sweet Shop Management System (Django + Bootstrap + TDD)

A fully functional Django-based web application to manage a Sweet Shop using **Test-Driven Development (TDD)** principles.  
Includes features like adding, deleting, searching, sorting, purchasing, and restocking sweets — all tested and frontend-ready with Bootstrap.

---

## 🚀 Features

- ✅ Add new sweets
- ✅ Delete sweets
- ✅ Search by name, category, or price range
- ✅ Sort sweets by name, price, or quantity
- ✅ Purchase sweets with stock validation
- ✅ Restock sweets with quantity checks
- ✅ Clean Bootstrap frontend (no JS required)
- ✅ Django test cases for all core features
- ✅ Ready for free deployment (Render.com)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML + Bootstrap 5
- **Database:** SQLite3
- **Testing:** Django `TestCase`
- **Hosting:** Render (Free)

---

## 📂 Project Structure
sweetshop_project/
├── shop/
│ ├── templates/shop/
│ │ ├── add_sweet.html
│ │ ├── confirm_delete.html
│ │ ├── purchase_sweet.html
│ │ └── restock_sweet.html
│ ├── tests.py
│ ├── views.py
│ ├── urls.py
│ ├── models.py
│ └── forms.py
├── sweetshop_project/
│ ├── settings.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
├── Procfile
└── README.md


---

## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DaxMistry27/Incubyte_Task.git
cd Incubyte_Task
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run development server
```bash
python manage.py runserver
```

### Running Tests
```bash
python manage.py test
```

## Deploy
- Go to https://render.com
- Create new Web Service → Connect GitHub repo

- Build Command: pip install -r requirements.txt
- Start Command: gunicorn sweetshop_project.wsgi:application
- 🎉 You’re now live on the internet!

📸 UI Screenshots

### Adding Sweets
<img width="592" height="972" alt="image" src="https://github.com/user-attachments/assets/aae587de-d0ac-4fe0-b442-0e884cd95229" />

### Searching sweets based on name & price
<img width="592" height="875" alt="image" src="https://github.com/user-attachments/assets/f3e03a53-58f7-44a4-a771-6900c00717dc" />

### Sorting sweets
<img width="592" height="972" alt="image" src="https://github.com/user-attachments/assets/18ad613c-57b1-48f0-8dfd-619895961900" />

### Deleting sweets
<img width="561" height="198" alt="image" src="https://github.com/user-attachments/assets/f1f07b13-1e2c-4beb-b945-5d8557a0c382" />

### Purchase Sweet
<img width="726" height="424" alt="image" src="https://github.com/user-attachments/assets/f214267e-9198-4eb5-8049-952dad390e1c" />

### Restock Sweet
<img width="722" height="393" alt="image" src="https://github.com/user-attachments/assets/233c7a73-5328-49ca-967a-44468a282a88" />


### Deployment on render : 🔗 https://sweetshop-uulm.onrender.com/add/

👤 Author
- Dax Mistry
- 📧 Email: daxmistry83@gmail.com
- 🌐 GitHub: https://www.github.com/DaxMistry27



