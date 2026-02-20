#!/bin/bash

echo "================================"
echo "PictoTongue Test Suite"
echo "================================"
echo ""

echo "Installing dependencies..."
pip install -r requirements-dev.txt

echo ""
echo "Running unit tests for Flask app..."
python -m pytest tests/test_app.py -v

echo ""
echo "Running Flask route tests..."
python -m pytest tests/test_flask_routes.py -v

echo ""
echo "Running all tests with coverage..."
python -m pytest tests/ -v --cov=app --cov-report=html

echo ""
echo "Coverage report generated in htmlcov/index.html"
