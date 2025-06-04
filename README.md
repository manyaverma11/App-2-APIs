# Application
A simple Django App HTML frontend for adding names to the database via API. It also helps in searching of entries using keywords via another API.

## Features

- Add new names with first name, last name, and education level
- Dynamically loads education options from API
- Responsive form with validation
- Clear success/error feedback

## Requirements

- Your Django API server running at `http://localhost:8000`
- API endpoints:
  - `GET /api/search/` - Returns education options
  - `POST /api/entry/` - Accepts new name entries

## API Response Formats

### Education Options (`GET /api/education/`)
```json
[
    {"id": 3, "degree": "BBA"},
    {"id": 4, "degree": "BE"}
]