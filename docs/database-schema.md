# Database Schema

## Overview

VoiceAgent Studio is a multi-tenant SaaS platform.

Each business has:

- Its own users
- Own uploaded documents
- Own AI Voice Agents
- Own conversations
- Own analytics

All businesses share the same application while their data remains isolated.

---

# Database Tables

## Users

Purpose:

Stores user accounts.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| full_name | VARCHAR(100) | User name |
| email | VARCHAR(255) | Unique email |
| password_hash | TEXT | Encrypted password |
| role | VARCHAR(20) | Owner/Admin |
| created_at | TIMESTAMP | Created time |
| updated_at | TIMESTAMP | Last update |

Relationship

One User → Many Businesses

---

## Businesses

Purpose

Stores each company.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| owner_id | UUID | References Users.id |
| business_name | VARCHAR(255) | Business name |
| industry | VARCHAR(100) | Restaurant, Construction, Clinic |
| phone_number | VARCHAR(30) | Business phone |
| email | VARCHAR(255) | Contact email |
| website | TEXT | Business website |
| timezone | VARCHAR(50) | Timezone |
| created_at | TIMESTAMP | Created |
| updated_at | TIMESTAMP | Updated |

Relationship

One Business

↓

Many Documents

Many Voice Agents

Many Conversations

Many Integrations

---

## Documents

Purpose

Stores uploaded business files.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| business_id | UUID | References Businesses.id |
| file_name | VARCHAR(255) | Uploaded filename |
| file_type | VARCHAR(20) | PDF DOCX TXT CSV |
| storage_path | TEXT | Storage location |
| status | VARCHAR(20) | Uploaded Processing Ready |
| uploaded_at | TIMESTAMP | Upload time |

---

## DocumentChunks

Purpose

Stores text chunks generated from uploaded files.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| document_id | UUID | References Documents.id |
| chunk_number | INTEGER | Order |
| content | TEXT | Text chunk |
| embedding_id | TEXT | Vector reference |
| token_count | INTEGER | Tokens |

---

## VoiceAgents

Purpose

Stores AI voice agents.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| business_id | UUID | References Businesses.id |
| agent_name | VARCHAR(100) | Agent name |
| greeting | TEXT | Greeting message |
| language | VARCHAR(20) | English |
| llm_model | VARCHAR(50) | GPT Model |
| voice_provider | VARCHAR(50) | ElevenLabs |
| is_active | BOOLEAN | Active |

---

## Conversations

Purpose

Stores every phone call.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| business_id | UUID | Business |
| voice_agent_id | UUID | Voice Agent |
| customer_phone | VARCHAR(30) | Phone number |
| started_at | TIMESTAMP | Start |
| ended_at | TIMESTAMP | End |
| duration_seconds | INTEGER | Duration |
| status | VARCHAR(20) | Completed Escalated |

---

## Messages

Purpose

Stores conversation transcript.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| conversation_id | UUID | Conversation |
| sender | VARCHAR(20) | User AI |
| message | TEXT | Message |
| timestamp | TIMESTAMP | Time |

---

## Integrations

Purpose

Stores external connections.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| business_id | UUID | Business |
| provider | VARCHAR(50) | Google Calendar |
| access_token | TEXT | Encrypted |
| refresh_token | TEXT | Encrypted |
| status | VARCHAR(20) | Connected |

---

## Appointments

Purpose

Stores bookings.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| business_id | UUID | Business |
| customer_name | VARCHAR(255) | Customer |
| phone | VARCHAR(30) | Phone |
| appointment_time | TIMESTAMP | Scheduled |
| status | VARCHAR(20) | Booked Cancelled Completed |

---

## Analytics

Purpose

Stores daily metrics.

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary Key |
| business_id | UUID | Business |
| total_calls | INTEGER | Total |
| successful_calls | INTEGER | Successful |
| escalated_calls | INTEGER | Human transfer |
| avg_duration | INTEGER | Seconds |
| report_date | DATE | Date |

---

# Entity Relationship

Users

↓

Businesses

├── Documents

│ └── DocumentChunks

├── VoiceAgents

├── Conversations

│ └── Messages

├── Integrations

├── Appointments

└── Analytics