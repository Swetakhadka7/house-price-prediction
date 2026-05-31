# Use official Python image as base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python libraries
RUN pip install pandas numpy scikit-learn streamlit joblib flask

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]