 IMDb Movie Data Analysis (Python + Pandas)

This project analyzes and visualizes data from the IMDb Top 1000 Movies dataset using **Python**, **Pandas**, **Seaborn**, and **Matplotlib**. It focuses on data cleaning, exploratory analysis, and visual storytelling.

---

📁 Dataset

- **Source**: IMDb Top 1000 Movies
- **Format**: CSV
- **Columns**:
  - `Title`, `Genre`, `Director`, `Actors`
  - `Year`, `Runtime (Minutes)`, `Rating`, `Votes`
  - `Revenue (Millions)`, `Metascore`

---
⚙️ Features / Tasks Completed

 Data Cleaning
- Renamed columns for easier access
- Filled missing values using median:
  - `Revenue`
  - `Metascore`
 Exploratory Analysis & Visualizations
- **Top 10 highest-rated movies**
- **Scatter plot:** Revenue vs IMDb Rating (Top 10)
- Added labels and color-coded points for better readability

---

 Technologies Used

| Tool         | Purpose                         |
|--------------|----------------------------------|
| `pandas`     | Data loading, cleaning, analysis |
| `matplotlib` | Plotting & charts                |
| `seaborn`    | Statistical visualizations       |
| `git`        | Version control & branching      |
| `GitHub`     | Remote repo & collaboration      |

---

 Sample Output

 Top 10 Movies by IMDb Rating

| Title                    | Rating | Revenue (M) |
|--------------------------|--------|-------------|
| The Dark Knight          | 9.0    | 534.9       |
| Inception                | 8.8    | 292.6       |
| ...                      | ...    | ...         |

 📈 Rating vs Revenue Plot (Top 10)

 A scatter plot showing how IMDb ratings relate to box office revenue. Each point is annotated with the movie title.

---
📂 Project Structure
project/
├── data/
│ └── IMDB-Movie-Data.csv
├── day_24_analysis.py
├── README.md
└── .gitignore



