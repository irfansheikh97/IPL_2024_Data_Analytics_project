
<br/>
<div align="center">
<a href="https://github.com/ShaanCoding/ReadME-Generator">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTTxPSNeKK3v74fXS-ESel0INzwvFKyO3nCQ&s" alt="Logo" width="80" height="80">
</a>
<h3 align="center">IPL 2024 Data Analytics</h3>
<p align="center">
Implemented detailed data analysis to identify patterns and trends, providing actionable insights for cricket enthusiasts and stakeholders.


  


</p>
</div>

## About The Project

![ipl](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRVt-u5cNJt2iPb4mEAVmT83-OPGRMoXDJTg&s)

This project involves detailed data analysis of the IPL 2024 season using Python for data scraping and Power BI for visualization. The data was collected from ESPNcricinfo website and includes match summaries, individual match statistics, and player information. The analysis helps cricket enthusiasts, analysts, and management teams to keep track of player performance and identify areas for improvement.
## Getting Started

Before running the analysis, ensure you have the following installed:
### Prerequisites

- Python (version 3.x)
- BeautifulSoup (for web scraping)
- Pandas (for data manipulation)
- Power BI (for visualization)
### Installation

Clone the repository:

1. Clone the repo
 ```git clone https://github.com/irfansheikh97/IPL_2024_Data_Analytics_project.git```

2. Install necessary Python packages:
```pip install beautifulsoup4 pandas requests```

3. Open Power BI Desktop to access the dashboard and CSV files for analysis.
## Usage

Data Sources
The data for IPL 2024 was scraped from ESPNcricinfo using Python. The following datasets were created:

- players_summary.csv: Contains player information for all players in IPL 2024.
- batting_summary.csv: Batting stats from each match.
- bowling_summary.csv: Bowling stats from each match.
- match_summary.csv: Details of each match played, including teams and match results.

Project Workflow:
1. Web Scraping
- The data was scraped using BeautifulSoup from ESPNcricinfo's IPL 2024 section.
- Key information extracted includes player stats, match summaries, and detailed match data.
2. Data Cleaning & Transformation
- After scraping, the raw data was cleaned using Python's Pandas library.
- Missing values, inconsistencies, and formatting issues were handled to ensure data quality.
- The data was then split into four CSV files: players_summary, batting_summary, bowling_summary, and match_summary.
3. Data Storage
- The cleaned data was stored in the CSV format for easy accessibility and further analysis in Power BI.

Data Cleaning & Transformation
- Handling Missing Values: Missing values were imputed or removed depending on the importance of the field.
- Data Formatting: Fields such as date, player names, and match IDs were standardized.
- Aggregating Data: Statistics were aggregated at the player and match levels for efficient analysis.

Visualization
The Power BI dashboard consists of several pages, each focusing on different aspects of player and team performance.

Pages:
1. Opener Batsmen Stats:
- Top scoring openers with metrics like average, boundary percentage, and strike rate.
2. Anchor/Middle Order Batsmen Stats:
- Performance metrics for anchor players.
3. Finishers/Lower Order Batsmen Stats:
- Analysis of players who play the finishing roles in innings.
4. All-rounder Stats:
- Players who contribute with both bat and ball, including metrics like batting average, bowling average, and wickets percentage.
5. Fast Bowlers Stats:
- Key stats like bowling average, wickets percentage, and strike rate for fast bowlers.
6. Best 11 Team:
- A selected squad of the best-performing players, designed to dominate any opposition in IPL 2024.

Features
- Comprehensive Player Analysis: Covers different player roles such as openers, middle-order batsmen, finishers, all-rounders, and fast bowlers.
- In-depth Team Comparison: Compare team performance based on player contributions.
- Customizable Dashboards: The Power BI dashboard allows for customization and further exploration of data.
- Best 11 Team: Selection of the best players based on statistical performance in IPL 2024.

Conclusion
This analysis provides valuable insights into player and team performances during IPL 2024. Cricket analysts, management teams, and fans can utilize the dashboard to track performance, spot trends, and identify areas of improvement for specific players and teams. The "Best 11" selection can serve as a strategic reference for future team formations.
