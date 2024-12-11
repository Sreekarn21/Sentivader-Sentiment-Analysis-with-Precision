# Sentivader: Sentiment Analysis with Precision

Sentivader is a machine learning project that leverages the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool. This application processes input CSV files containing text data, analyzes the sentiment of the content, and generates a PDF report with the results.

## Features
- **CSV Input**: Accepts CSV files as input containing text data for analysis.
- **VADER Sentiment Analysis**: Uses the VADER library to evaluate the sentiment of text (positive, neutral, negative).
- **PDF Output**: Generates a PDF report summarizing sentiment scores and classifications.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Required Python libraries (listed in `requirements.txt`):
  - `pandas`
  - `matplotlib`
  - `nltk`
  - `reportlab`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sreekarn21/Sentivader-Sentiment-Analysis-with-Precision.git
   cd Sentivader-Sentiment-Analysis-with-Precision
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the VADER lexicon:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Usage
1. Place your input CSV file in the project directory.
2. Run the script with the path to your CSV file:
   ```bash
   python sentiment_analysis.py <input_file.csv>
   ```
3. The output PDF report will be saved in the project directory.

## File Structure
- `sentiment_analysis.py`: Main script for processing the input and generating the output.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Project documentation.

## Example
Input CSV:
| Text                       |
|----------------------------|
| "I love this product!"     |
| "It's okay, could be better." |
| "Absolutely terrible service." |

Generated PDF:
- **Positive**: 1
- **Neutral**: 1
- **Negative**: 1

## Future Enhancements
- Support for additional sentiment analysis models.
- Interactive dashboard for sentiment visualization.
- Multi-language sentiment analysis.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [VADER Sentiment Analysis Tool](https://github.com/cjhutto/vaderSentiment)
- Python community for extensive library support.

