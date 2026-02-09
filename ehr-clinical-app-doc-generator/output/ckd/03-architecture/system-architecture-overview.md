# System Architecture Overview

## Components
1. **EHR Interface (Client)**:
   - Epic Hyperspace (embedded web view or native alert).
   - Cerner PowerChart (MPages).
   - SMART on FHIR App (React.js frontend).
2. **CDS Service (Middleware)**:
   - Python (FastAPI) or Node.js (NestJS).
   - Implements CDS Hooks specification (`cds-services` endpoint).
   - Handles logic execution (KDIGO rules engine).
3. **FHIR Server / Facade**:
   - Connection to EHR database via FHIR R4.
   - Read: `Observation` (Labs), `Condition` (Problem List).
   - Write: `Condition` (via `Order` or direct POST if permitted).

## Technology Stack
- **Frontend**: React, SMART Client JS Library.
- **Backend API**: Python FastAPI.
- **Data Standard**: HL7 FHIR R4.

## Integration Pattern (CDS Hooks)
1. **Trigger**: Clinician opens patient chart (`patient-view` hook).
2. **Request**: EHR sends context.
3. **Analyze**: CDS Service executes logic.
4. **Response**: CDS Service returns a "Card".
