w 🏆 ChallengeTV

ChallengeTV is a fully functional web application built with Django that allows users to participate in various challenges, track their progress, and stay motivated toward personal growth and achievements.

The project focuses on building habits, discipline, and self-development through a structured challenge system.

---

## 🚀 Features

- User registration and authentication
- Browse list of available challenges
- Join and track progress in challenges
- Admin panel to manage content
- (Planned) Achievements, badges, and progress levels

---

## 🛠️ Technologies Used

- 👨‍💻 Language: Python 3
- 🧠 Framework: Django
- 🗂️ Database: SQLite
- 🎨 Frontend: HTML5, CSS3, Bootstrap 4
- ⚙️ Tools: PyCharm Professional, Git, GitHub

---

## ⚙️ Installation & Run Instructions

1. Clone the repository:

`bash
git clone https://github.com/RuslanIstamqulov/ChallengeTV.git
cd ChallengeTV







<td>
                            <select
                                class="status-select status-{{ challenge.status|slugify }}"
                                data-id="{{ challenge.id }}">
                                {% for value, label in challenge.CHANGE_STATUS %}
                                    <option value="{{ value }}" {% if challenge.status == value %}selected{% endif %}>
                                        {{ label|upper }}
                                    </option>
                                {% endfor %}
                            </select>
                        </td>
