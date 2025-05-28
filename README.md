# Instagram Sentiment Analysis App – Flutter Frontend

This is the Flutter frontend for the **Instagram Sentiment Analysis App**, a real-time AI-powered tool that analyzes the sentiment of Instagram profiles, brands, influencers, and hashtags. It uses a modern, responsive UI built in Flutter and connects to a Flask backend that performs NLP-based sentiment analysis using VADER.

---

## 🌟 Features

### ✅ Authentication
- Email-password signup/login
- Google Sign-In
- Session persistence using shared preferences

### ✅ User Profile
- Upload/change profile image
- View/edit name, email, and bio
- Dark/Light mode support (auto-detected)
- Logout functionality

### ✅ Sentiment Analysis
- **Profile Analysis** – Analyzes captions/comments of a profile
- **Brand Analysis** – Tracks engagement, sentiment, and PR risk
- **Influencer Analysis** – Offers sentiment breakdown, reach metrics, trendlines
- **Hashtag Analysis** – Evaluates sentiment around a given hashtag

### ✅ Visualization
- Sentiment score bars with emoji indicators
- Trendline graphs using `fl_chart`
- Tabs for Followers, Engagement, Overview, Sentiment

---

## 📁 Folder Structure

app1/
├── android/                       
│   ├── app/
│   │   └── src/
│   │       ├── debug/
│   │       ├── main/
│   │       │   └── AndroidManifest.xml    # Android app config file
│   │       └── profile/
│   ├── build.gradle
│   ├── local.properties
│   ├── settings.gradle
│   └── ...                                # Other Gradle configs
├── assets/
│   ├── fonts/
│   └── images/
│       ├── google_icon.png
│       ├── logo-zoreai.png
│       └── social_illustration.png
├── lib/
│   ├── components/
│   ├── models/
│   ├── providers/
│   ├── screens/
│   ├── services/
│   │   └── instagram_service.dart
│   ├── themes/
│   │   ├── settings_screen.dart
│   │   └── themes.dart
│   ├── widgets/
│   └── main.dart                        # App entry point
├── linux/
├── macos/
├── windows/
├── web/
├── test/
│   └── widget_test.dart
├── pubspec.yaml
├── .gitignore
├── analysis_options.yaml
├── README.md

## ⚙️ Getting Started

### Prerequisites

- Flutter SDK
- Android Studio or VS Code
- Python 3 with Flask, VADER, Instaloader

### Steps

1. Install dependencies:
   flutter pub get

### Run the app:
flutter run

### ### Prerequisites

- Flutter SDK installed
- Android Studio or VS Code
- Python 3.x for backend (Flask)
- Instaloader & VADER installed in backend