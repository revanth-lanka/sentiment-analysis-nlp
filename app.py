"""Flask REST API for Sentiment Analysis using BERT-based transformer models."""

import torch
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load pre-trained BERT model
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

LABELS = ["NEGATIVE", "POSITIVE"]


def preprocess_text(text: str) -> str:
    """Clean and preprocess input text."""
    text = text.lower().strip()
    return text


def predict_sentiment(text: str) -> Dict:
    """Predict sentiment for given text using BERT model."""
    try:
        processed_text = preprocess_text(text)
        inputs = tokenizer(processed_text, return_tensors="pt", truncation=True, max_length=512)
        
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
        
        probabilities = torch.softmax(logits, dim=1).squeeze()
        prediction = torch.argmax(logits, dim=1).item()
        
        confidence = probabilities[prediction].item()
        
        return {
            "text": text,
            "sentiment": LABELS[prediction],
            "confidence": round(confidence, 4),
            "scores": {
                "negative": round(probabilities[0].item(), 4),
                "positive": round(probabilities[1].item(), 4)
            }
        }
    except Exception as e:
        logger.error(f"Error in sentiment prediction: {str(e)}")
        raise


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "sentiment-analysis-api"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    """Predict sentiment for provided text."""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Missing required field: text"}), 400
        
        text = data['text']
        if not isinstance(text, str) or len(text.strip()) == 0:
            return jsonify({"error": "Text must be a non-empty string"}), 400
        
        result = predict_sentiment(text)
        return jsonify(result), 200
    
    except Exception as e:
        logger.error(f"Error in /predict endpoint: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    """Batch predict sentiment for multiple texts."""
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({"error": "Missing required field: texts"}), 400
        
        texts = data['texts']
        if not isinstance(texts, list) or len(texts) == 0:
            return jsonify({"error": "Texts must be a non-empty list"}), 400
        
        results = []
        for text in texts:
            if isinstance(text, str) and len(text.strip()) > 0:
                result = predict_sentiment(text)
                results.append(result)
        
        return jsonify({"predictions": results}), 200
    
    except Exception as e:
        logger.error(f"Error in /batch-predict endpoint: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
