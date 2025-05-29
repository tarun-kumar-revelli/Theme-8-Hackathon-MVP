# API Documentation for CyberSecure Learn

## Overview
This document provides an overview of the API endpoints available in the CyberSecure Learn application. The API is built using FastAPI and serves as the backend for the secure coding tutor.

## Base URL
```
http://localhost:8000
```

## Endpoints

### 1. Analyze Code
- **Endpoint:** `/analyze`
- **Method:** `POST`
- **Description:** Accepts user-submitted code and returns vulnerabilities, explanations, and suggestions for secure alternatives.
- **Request Body:**
  ```json
  {
    "code": "string",
    "language": "string"
  }
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "vulnerabilities": [
        {
          "type": "string",
          "description": "string",
          "suggestion": "string"
        }
      ],
      "fixed_code": "string"
    }
    ```
  - **400 Bad Request**
    ```json
    {
      "detail": "string"
    }
    ```

### 2. Health Check
- **Endpoint:** `/health`
- **Method:** `GET`
- **Description:** Checks the health status of the API.
- **Response:**
  - **200 OK**
    ```json
    {
      "status": "healthy"
    }
    ```

## Usage Examples

### Analyze Code Example
**Request:**
```http
POST /analyze HTTP/1.1
Content-Type: application/json

{
  "code": "user_code_here",
  "language": "python"
}
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "vulnerabilities": [
    {
      "type": "SQL Injection",
      "description": "The code is vulnerable to SQL injection.",
      "suggestion": "Use parameterized queries."
    }
  ],
  "fixed_code": "fixed_code_here"
}
```

### Health Check Example
**Request:**
```http
GET /health HTTP/1.1
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "healthy"
}
```

## Conclusion
This API documentation outlines the key endpoints for the CyberSecure Learn application. For further details on implementation and usage, please refer to the source code and comments within the project files.