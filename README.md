# releasepilot-ai

AI-powered release governance platform using autonomous agents to deliver explainable software release decisions.

## Problem

Release decisions are manual and fragmented.

## Solution

ReleasePilot AI uses autonomous agents to analyze:

- Defects  
- Test Results  
- Release Metrics  

and produce:  
- GO  
- CONDITIONAL GO  
- NO GO  

recommendations.

## Environment Variables

The project requires a `.env` file to be created in the `backend` directory for configuration. Below is an example of the required `.env` file:

```dotenv
GEMINI_API_KEY=k
