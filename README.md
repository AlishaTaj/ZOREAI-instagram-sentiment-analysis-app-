# Instagram Sentiment Analysis App 

This is the **Flutter frontend** of the Instagram Sentiment Analysis App. It connects to a **Flask backend** that performs real-time sentiment analysis using VADER, the Instagram Graph API, and SQLite. 

The app allows users to analyze Instagram profiles, brands, influencers, and hashtags. It includes user authentication, clean dashboards, and visual sentiment reports.

---

## Key Technologies

- **Frontend:** Flutter (Dart)
- **Backend:** Flask (Python), SQLite
- **APIs & Tools:** Instagram Graph API, Instaloader, VADER
- **Charts & UI:** fl_chart, Shared Preferences, Provider

---

## Features

### User Authentication
- Login/signup with email and password
- Google Sign-In (OAuth)
- Session persistence using shared preferences

### User Profile
- Upload and update profile photo
- View/edit name, email, and bio
- Light/Dark mode (auto-detected)
- Logout functionality

### Sentiment Analysis Modules
- **Profile Analysis**: Analyze recent captions and comments
- **Brand Analysis**: Track brand sentiment, engagement, PR risk
- **Influencer Analysis**: View sentiment breakdown, reach, brand deals, and trendlines
- **Hashtag Analysis**: Analyze public hashtags for sentiment and virality

### Visualizations
- Sentiment bars with basic visual indicators
- Trendline charts using `fl_chart`
- Tabs for Overview, Followers, Engagement, and Sentiment
- PR risk indicators and brand health scores

---

## Folder Structure
app1/
├── lib/
│ ├── components/ # Reusable UI elements
│ ├── models/ # Data models
│ ├── providers/ # State management
│ ├── screens/ # Screens for each feature
│ ├── services/ # Backend API calls
│ ├── themes/ # Theme files
│ ├── widgets/ # Custom widgets
│ └── main.dart # App entry point
├── assets/ # Fonts and images
├── android/ # Android-specific config
├── pubspec.yaml # Flutter packages


---

## How to Run the App

### Requirements

- Flutter SDK installed
- Android Studio or Visual Studio Code
- Python 3.x
- Flask, Instaloader, VADER (for backend)


## Planned Features

- PDF export for reports
- Clustering and tagging of hashtags
- Real-time Graph API data updates
- UI improvements based on user feedback

---

## Maintainer

**Alisha Taj**  
Computer Science Student – Bengaluru, India  
Email: alishataj72@gmail.com  
LinkedIn: [linkedin.com/in/alisha-taj](https://linkedin.com/in/alisha-taj)  
Instagram (Tech): [instagram.com/alisha.codes](https://instagram.com/alisha.codes)

