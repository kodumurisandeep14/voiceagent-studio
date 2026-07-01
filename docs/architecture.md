# System Architecture

## Overview

VoiceAgent Studio is a multi-tenant SaaS platform that enables businesses to create AI-powered voice agents by uploading their business documents.

## High-Level Architecture

Business Owner
        │
React Dashboard
        │
FastAPI Backend
        │
─────────────────────────────
│            │             │
Postgres     Storage      AI Services
│            │             │
Users        PDFs         OpenAI
Businesses   Images       LangGraph
Calls        Files        Embeddings
        │
Vector Database
        │
Voice Layer
(Vapi / Twilio)