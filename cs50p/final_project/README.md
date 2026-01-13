# CIS Tech Market Insights
### Video Demo:  <URL HERE>
### Description:
A Python application that fetches and analyzes job vacancies from the HeadHunter (hh.ru) API. The tool helps job seekers understand market trends by providing insights into job requirements, locations, industries, and required skills through interactive visualizations and reports.

## Features

- **Interactive Job Search**: Select job roles and locations from available options
- **Data Fetching**: Asynchronously fetches job vacancies and descriptions from hh.ru API
- **Market Analysis**: Provides summaries of:
  - Top 5 cities with job opportunities
  - Top 5 industries
  - Work experience requirements
  - Professional roles distribution
  - Employment types (full-time, part-time, etc.)
  - Work formats (remote, office, hybrid)
- **Skills Analysis**: Extracts and counts required skills from job descriptions
- **Visualizations**:
  - Interactive dashboard with 6 charts (pie charts and bar charts)
  - Word cloud visualization of required skills
  - PDF report combining all visualizations

## Requirements

- Python 3.7+ (Python 3.11+ recommended for `asyncio.TaskGroup` support)
- HeadHunter API access token

### Python Dependencies

- `aiohttp` - Asynchronous HTTP client
- `asyncio` - Asynchronous I/O (built-in)
- `matplotlib` - Data visualization
- `numpy` - Numerical operations
- `wordcloud` - Word cloud generation
- `fpdf` - PDF generation
- `python-dotenv` - Environment variable management

## Installation

1. Clone or download this repository

2. Install required packages:
```bash
pip install aiohttp matplotlib numpy wordcloud fpdf python-dotenv
```

3. Create a `.env` file in the project root directory:
```env
ACCESS_TOKEN=your_hh_ru_api_access_token_here
```
To obtain an access token: please refer to the [HeadHunter API documentation](https://github.com/hhru/api).


## Usage

Run the main script:
```bash
python "project.py"
```

### Workflow

1. **Dictionary Fetching**: The application fetches available job roles and locations from the API
2. **User Selection**:
   - Select one or more location IDs (comma-separated, e.g., `1,2,3`)
   - Select one or more job role IDs (comma-separated)
3. **Data Collection**: The application fetches all matching vacancies
4. **Analysis**: Summary statistics are displayed in the console
5. **Visualization** (optional): Choose whether to generate charts and PDF report


## Testing

The project includes unit tests in `test_project.py`. The tests use `pytest` and `unittest.mock` for mocking.

### Running Tests

Install pytest if not already installed:
```bash
pip install pytest pytest-mock
```

Run the tests:
```bash
pytest test_project.py
```

### Test Coverage

The test suite includes:
- **`test_validated_input`**: Tests input validation for single and multiple IDs, including error handling for invalid inputs
- **`test_get_areas`**: Tests area filtering (removes "Other regions") and sorting
- **`test_get_roles`**: Tests role filtering (only "Information technology" category)

## API Rate Limiting

The application respects API rate limits by:
- Using semaphores to limit concurrent requests (30 requests per second)
- Implementing 1.1-second pauses between batches of requests
- Using asynchronous requests for efficient data fetching

## Output Files

### Console Output
- Summary statistics for all analyzed categories
- Top 10 most required skills

### Generated Files (if visualization is requested)
- `summary/charts.png`: Dashboard with 6 charts showing market analysis
- `summary/word_cloud.png`: Visual representation of required skills
- `summary/summary.pdf`: Combined PDF report with all visualizations
