# 🎙️ VoiceAgent Studio

An AI-powered Voice Agent platform built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

The goal of this project is to build a production-ready platform where businesses can upload knowledge documents, create AI voice agents, and interact with customers using Retrieval-Augmented Generation (RAG) and Large Language Models.

---

# 🚀 Current Progress

## ✅ Phase 1 - Project Setup

- FastAPI Backend
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Database Migrations
- Swagger UI
- Layered Project Architecture

---

## ✅ Phase 2 - Authentication

Implemented secure JWT Authentication.

### Features

- User Registration
- User Login
- Password Hashing (bcrypt)
- JWT Token Generation
- OAuth2 Authentication
- Protected Routes
- Current Logged-in User Endpoint

### APIs

```
POST   /users/register
POST   /users/login
GET    /users/me
```

---

## ✅ Phase 3 - Business Management

Businesses can manage their own AI workspace.

### Features

- Create Business
- Get Business
- Update Business
- Delete Business
- Business Ownership Validation
- JWT Protected APIs

### APIs

```
POST    /businesses/
GET     /businesses/
GET     /businesses/{business_id}
PUT     /businesses/{business_id}
DELETE  /businesses/{business_id}
```

---

## ✅ Phase 4 - Document Management (Metadata)

Implemented complete CRUD operations for business documents.

Currently stores document metadata inside PostgreSQL.

### Features

- Create Document
- Get Document
- List Documents
- Update Document
- Delete Document
- Business Ownership Validation

### APIs

```
POST    /documents/
GET     /documents/business/{business_id}
GET     /documents/{document_id}
PUT     /documents/{document_id}
DELETE  /documents/{document_id}
```

---

# 🏗️ Project Architecture

```
Client
   │
   ▼
FastAPI API
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

---

# 📁 Project Structure

```
backend/
│
├── alembic/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── requirements.txt
└── .env
```

---

# 🛠️ Technology Stack

## Backend

- FastAPI
- Python 3.11
- SQLAlchemy
- Alembic
- Pydantic

## Database

- PostgreSQL

## Authentication

- JWT
- OAuth2
- Passlib
- bcrypt

## Documentation

- Swagger UI
- OpenAPI

## Version Control

- Git
- GitHub

---

# 🔐 Authentication Flow

```
Register
      │
      ▼
Store User
      │
      ▼
Login
      │
      ▼
Generate JWT
      │
      ▼
Swagger OAuth2
      │
      ▼
Protected APIs
```

---

# 🗄️ Database Tables

Current tables

- users
- businesses
- documents
- conversations
- messages

---

# ✅ Completed Features

- JWT Authentication
- OAuth2 Integration
- User Registration
- User Login
- Current User Endpoint
- Business CRUD
- Document CRUD
- SQLAlchemy ORM
- PostgreSQL Integration
- Alembic Migrations
- Repository Pattern
- Service Layer
- API Documentation using Swagger

---

# 🚧 Roadmap

## Phase 5 - File Upload

- Upload PDF
- Upload DOCX
- Upload TXT
- Local File Storage
- AWS S3 Integration

---

## Phase 6 - RAG Pipeline

- Text Extraction
- Chunking
- Embeddings
- Vector Database
- Semantic Search
- Retrieval-Augmented Generation

---

## Phase 7 - Voice Agent

- Speech-to-Text
- LLM Integration
- Text-to-Speech
- Real-time Voice Conversation

---

## Phase 8 - Analytics

- Call Logs
- Conversation History
- Business Dashboard
- Usage Analytics

---

# ▶️ Running the Project

## Clone Repository

```bash
git clone https://github.com/kodumurisandeep14/voiceagent-studio.git
```

---

## Backend

```bash
cd backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
alembic upgrade head
```

Start the server

```bash
uvicorn app.main:app --reload
```

---

# 📚 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 👨‍💻 Author

**Sandeep Kodumuri**

GitHub:
https://github.com/kodumurisandeep14

---

# 📄 License

This project is developed for educational purposes and as a portfolio project demonstrating modern AI backend development using FastAPI, PostgreSQL, and Retrieval-Augmented Generation (RAG).
