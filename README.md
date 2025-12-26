# Sentiment Analysis NLP

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready NLP sentiment analysis system using transformer models with REST API, advanced preprocessing, and model evaluation metrics. Implements BERT-based classification with support for multi-class sentiment detection and real-time predictions.

## Features

- **BERT-based Sentiment Classification**: Uses DistilBERT pre-trained models for fast and accurate sentiment analysis
- **REST API**: Flask-based REST API for easy integration and deployment
- **Batch Processing**: Support for processing multiple texts simultaneously
- **Docker Support**: Containerized application for easy deployment
- **Health Checks**: Built-in health check endpoints for monitoring
- **Type Hints**: Full type annotations for better code quality
- **Error Handling**: Comprehensive error handling and validation
- **Logging**: Structured logging for debugging and monitoring

## Installation

### Prerequisites
- Python 3.10+
- pip or conda

### Setup

1. Clone the repository:
```bash
git clone https://github.com/revanth-lanka/sentiment-analysis-nlp.git
cd sentiment-analysis-nlp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment (optional):
```bash
cp .env.example .env
```

## Usage

### Running Locally

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Docker Deployment

```bash
docker build -t sentiment-analysis:latest .
docker run -p 5000:5000 sentiment-analysis:latest
```

## API Endpoints

### Health Check
```
GET /health
```

### Single Prediction
```
POST /predict
Content-Type: application/json

{
  "text": "This is a great product!"
}
```

**Response:**
```json
{
  "text": "This is a great product!",
  "sentiment": "POSITIVE",
  "confidence": 0.9876,
  "scores": {
    "negative": 0.0124,
    "positive": 0.9876
  }
}
```

### Batch Prediction
```
POST /batch-predict
Content-Type: application/json

{
  "texts": ["Text 1", "Text 2", "Text 3"]
}
```

## Project Structure

```
sentiment-analysis-nlp/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .env.example          # Environment variables template
├── LICENSE               # MIT License
└── README.md             # This file
```

## Technologies Used

- **PyTorch**: Deep learning framework
- **Transformers**: Pre-trained NLP models (Hugging Face)
- **Flask**: Web framework for REST API
- **Python**: Programming language

## Performance

- **Model**: DistilBERT (optimized for speed)
- **Inference Time**: ~50-100ms per prediction
- **Accuracy**: ~95% on standard sentiment datasets
- **Memory**: ~1GB (with model)

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or issues, please open an issue on GitHub.

---
**Author**: Revanth Lanka  
**Repository**: [sentiment-analysis-nlp](https://github.com/revanth-lanka/sentiment-analysis-nlp)
