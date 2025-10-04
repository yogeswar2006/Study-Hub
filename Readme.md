
# 🧠 Study-Hub

**Study-Hub** is a collaborative learning platform built with the Django framework. It enables users to connect with others through topic-based discussion rooms. With a clean UI and RESTful API support, it's designed for both casual browsing and authenticated interaction.

---

## ✨ Features

### 👥 Public & Authenticated Access
- ✅ Visitors can **view rooms, topics, and messages** without logging in.
- 🔐 Authenticated users can:
  - **Login / Logout**
  - **Create new rooms**
  - **Update their own rooms**
  - **Delete their own messages**

### 💬 Room-Based Discussions
- Create and participate in **topic-specific rooms**.
- Every room has its own message thread.
- Room creators have control over room editing and message deletion.

### 🧭 Intuitive UI Layout
- 📚 **Left Sidebar** – Lists all available **topics** for easy navigation.
- 🏠 **Main Section** – Displays the **latest rooms** created by users.
- 🎨 Clean, responsive interface for both desktop and mobile devices.

### 🔍 Filter & Search Functionality
- **Filter by Topic** – Quickly view all rooms related to a selected topic.
- **Search Rooms** – Find rooms by keywords in the title or description.
- **Filter Messages** – Search inside room messages for specific content.

### 🛠️ RESTful API Integration
- Built using **Django REST Framework**.
- API Endpoints for:
  - Room creation, update, delete
  - Message creation and retrieval
  - Topic listing
  - User-based filtering

---


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yogeswar2006/Study-Hub.git
cd Study-Hub

python -m venv venv
On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

🛡️ Permissions<br>
  .🧑 Guests:<br>
       => View topics, rooms, and messages  
  .✅ Logged-in Users:<br>
       => Create rooms, post messages  
       => Edit their own rooms  
       => Delete their own messages  

📌 Tech Stack<br>
  => Backend: Django 5+, Django REST Framework

  => Frontend: HTML, CSS, JS 

  => Database: SQLite3 (for development)

  => Auth: Django built-in authentication

📜 License
This project is licensed under the MIT License.

📬 Contact
Built with ❤️ by [Yogeswar Reddy]<br>
📧 Email: yogi8247322760@gmail.com <br>
🔗 GitHub : @https://github.com/yogeswar2006



