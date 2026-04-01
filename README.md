# Hands-On AST (Astronomical Source Type) Classification

A complete exploratory data analysis and tutorial for astronomical object classification between **galaxies** and **stars** using photometric and morphological features.

## Project Overview

This project provides hands-on experience in:
- **Data exploration & quality assessment**
- **Descriptive statistical analysis**
- **Multi-dimensional visualization techniques**
- **Class comparison and effect-size estimation**
- **Feature relationships through correlation and pairwise analysis**

## Dataset

The `tutorial_data.txt` file contains **10,000 astronomical objects** with **balanced classes**:
- **5,000 Galaxies (GALAXY)**
- **5,000 Stars (STAR)**

### Key Features

**Structural features** (morphological):
- `FWHM`: Full-Width Half-Maximum (point-spread function size)
- `A`, `B`: Semi-major and semi-minor axes
- `KrRadDet`: Kron radius detection parameter
- `RA`, `Dec`: Celestial coordinates
- `ID`: Object identifier

**Photometric features** (multi-band magnitudes):
- `uJAVA_auto`, `F378_auto`, `F395_auto`, `F410_auto`, `F430_auto` (UV/optical)
- `g_auto`, `F515_auto`, `r_auto`, `F660_auto`, `i_auto`, `F861_auto`, `z_auto` (optical/infrared)

## Project Structure

```
.
├── README.md                          # This file
├── main.py                            # Entry point script
├── setup.py                           # Package setup
├── pyproject.toml                     # Project configuration
├── config/
│   └── config.json                    # Configuration settings
├── data/
│   └── tutorial_data.txt              # Main dataset (10,000 objects)
└── src/
    ├── notebooks/
    │   └── descriptive_analyses.ipynb # Complete EDA notebook
    └── utils/
        └── config_loader.py           # Configuration utilities
```

## Analysis Notebook

The main analysis is in `src/notebooks/descriptive_analyses.ipynb` and includes:

### 1. **Data Loading & Inspection**
- Dataset shape and column overview
- First 5 rows preview

### 2. **Data Quality Checks**
- Missing values assessment
- Duplicate row detection
- Class balance confirmation

### 3. **Descriptive Statistics**
- **Global summaries**: mean, std, quantiles for all 18 numeric features
- **Class-wise statistics**: mean, median, std, min, max for key morphological features (FWHM, A, B, KrRadDet)
- **Quantile analysis**: 1st, 5th, 25th, 50th, 75th, 95th, 99th percentiles
- **Effect-size ranking**: Standardized mean differences (Cohen's-d style) to identify most separable features

### 4. **Visual Analysis**
- **Histogram overlays** by class for FWHM, A, B, KrRadDet (with KDE)
- **Boxplots** comparing class distributions per feature
- **Scatter plot**: FWHM vs. A across classes
- **Correlation heatmap**: 8-feature correlation structure
- **Pairplot** (sampled): relationships between 6 key features

### 5. **Key Findings**
- **KrRadDet**, **FWHM**, **A**, and **B** show the strongest separation between classes
- Stars are more compact (lower FWHM, A, B, KrRadDet values)
- Galaxies show higher morphological diversity
- Clear class-wise distinctions in optical magnitudes (g, r, i, z)

## Running the Analysis

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- pandas, numpy, matplotlib, seaborn

### Option 1: Run the Notebook
```bash
cd src/notebooks
jupyter notebook descriptive_analyses.ipynb
```

### Option 2: Execute from Python
```bash
python main.py
```

## Key Insights

| Feature      | STAR Mean | GALAXY Mean | Effect Size |
|--------------|-----------|-------------|-------------|
| FWHM         | 1.03      | 3.10        | -1.91       |
| A            | 2.23      | 4.20        | -1.79       |
| B            | 2.10      | 2.94        | -1.34       |
| KrRadDet     | 1.08      | 1.43        | -2.88       |

**Interpretation**: Negative values indicate metrics are higher in galaxies, reflecting their extended morphology compared to point-like stars.

## Dependencies

See `pyproject.toml` or install with:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

## License

See LICENSE file for details.