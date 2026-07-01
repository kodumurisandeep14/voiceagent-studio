# API Design

## Overview

VoiceAgent Studio exposes REST APIs that allow the frontend, voice providers, and third-party integrations to communicate with the backend.

Base URL

```
http://localhost:8000/api/v1
```

Authentication

- JWT Bearer Token
- Protected endpoints require authentication.

---

# Authentication APIs

## Register User

**POST**

```
/auth/register
```

### Request

```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "Password123"
}
```

### Response

```json
{
  "id": "uuid",
  "message": "User registered successfully"
}
```

---

## Login

**POST**

```
/auth/login
```

### Request

```json
{
  "email": "john@example.com",
  "password": "Password123"
}
```

### Response

```json
{
  "access_token": "jwt_token",
  "token_type": "Bearer"
}
```

---

## Get Current User

**GET**

```
/auth/me
```

### Response

```json
{
  "id": "uuid",
  "full_name": "John Doe",
  "email": "john@example.com"
}
```

---

# Business APIs

## Create Business

**POST**

```
/businesses
```

### Request

```json
{
  "business_name": "ABC Construction",
  "industry": "Construction",
  "phone_number": "+1-555-555-5555",
  "email": "info@abc.com",
  "website": "https://abc.com",
  "timezone": "America/New_York"
}
```

### Response

```json
{
  "id": "uuid",
  "message": "Business created successfully"
}
```

---

## Get All Businesses

**GET**

```
/businesses
```

---

## Get Business Details

**GET**

```
/businesses/{business_id}
```

---

## Update Business

**PUT**

```
/businesses/{business_id}
```

---

## Delete Business

**DELETE**

```
/businesses/{business_id}
```

---

# Document APIs

## Upload Document

**POST**

```
/documents/upload
```

### Form Data

```
business_id

file
```

### Response

```json
{
  "document_id": "uuid",
  "status": "uploaded"
}
```

---

## Get Documents

**GET**

```
/documents
```

---

## Delete Document

**DELETE**

```
/documents/{document_id}
```

---

## Process Document

**POST**

```
/documents/{document_id}/process
```

Purpose

- Extract text
- Chunk document
- Generate embeddings
- Store vectors

---

# Knowledge Base APIs

## Search Knowledge Base

**POST**

```
/knowledge/search
```

### Request

```json
{
  "business_id": "uuid",
  "query": "What are your business hours?"
}
```

### Response

```json
{
  "answer": "We are open Monday through Friday from 9 AM to 6 PM."
}
```

---

# Chat APIs

## Ask AI

**POST**

```
/chat
```

### Request

```json
{
  "business_id": "uuid",
  "message": "Do you serve vegan pizza?"
}
```

### Response

```json
{
  "response": "Yes, we have three vegan pizza options."
}
```

---

## Conversation History

**GET**

```
/chat/history/{conversation_id}
```

---

# Voice APIs

## Voice Webhook

**POST**

```
/voice/webhook
```

Purpose

Receives incoming calls from Twilio or Vapi.

---

## Start Voice Session

**POST**

```
/voice/start
```

---

## End Voice Session

**POST**

```
/voice/end
```

---

# Conversation APIs

## Get Conversations

**GET**

```
/conversations
```

---

## Get Conversation Details

**GET**

```
/conversations/{conversation_id}
```

---

## Delete Conversation

**DELETE**

```
/conversations/{conversation_id}
```

---

# Appointment APIs

## Create Appointment

**POST**

```
/appointments
```

### Request

```json
{
  "business_id": "uuid",
  "customer_name": "Jane Smith",
  "phone": "+1-555-123-4567",
  "appointment_time": "2026-07-15T10:00:00"
}
```

---

## Get Appointments

**GET**

```
/appointments
```

---

## Cancel Appointment

**PUT**

```
/appointments/{appointment_id}
```

---

# Analytics APIs

## Dashboard Statistics

**GET**

```
/analytics/dashboard
```

### Response

```json
{
  "total_calls": 150,
  "successful_calls": 140,
  "failed_calls": 10,
  "average_duration": 245
}
```

---

## Call Analytics

**GET**

```
/analytics/calls
```

---

## Conversation Analytics

**GET**

```
/analytics/conversations
```

---

# Integration APIs

## Connect Google Calendar

**POST**

```
/integrations/google-calendar
```

---

## Connect Gmail

**POST**

```
/integrations/gmail
```

---

## Connect Twilio

**POST**

```
/integrations/twilio
```

---

## Connect Stripe

**POST**

```
/integrations/stripe
```

---

# Admin APIs

## Get Platform Statistics

**GET**

```
/admin/statistics
```

---

## Get All Users

**GET**

```
/admin/users
```

---

## Get All Businesses

**GET**

```
/admin/businesses
```

---

## Health Check

**GET**

```
/health
```

Response

```json
{
  "status": "healthy"
}
```

---

# API Response Format

## Success

```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {}
}
```

## Error

```json
{
  "success": false,
  "message": "Validation failed",
  "errors": []
}
```

---

# HTTP Status Codes

| Status Code | Meaning |
|--------------|---------|
| 200 | Success |
| 201 | Resource Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# API Versioning

Current Version

```
/api/v1
```

Future versions

```
/api/v2
/api/v3
```

---

# Future APIs

- Email Notifications
- SMS Notifications
- AI Prompt Management
- Voice Customization
- AI Model Selection
- Workflow Automation
- Multi-language Support
- Webhooks
- Billing & Subscription
- Team Member Management