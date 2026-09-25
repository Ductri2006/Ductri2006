<p>
  <img src="assets/house-of-ductri.svg" width="100%" alt="Nguyen Duc Tri. AI Engineer." />
</p>

# Nguyen Duc Tri

I work on machine learning and the software around it: preparing data, evaluating models, and integrating AI into applications with clear API and access boundaries.

## Selected work

### Telco Churn / Model development

A joint coursework study of customer churn using the IBM Telco dataset.

- Logistic Regression from scratch with a numerical gradient check, compared with scikit-learn.
- Stratified train/test split, training-only scaling, and five-fold cross-validation.
- ROC and precision–recall analysis, validation-based threshold selection, and feature contributions.

Python · NumPy · pandas · scikit-learn

[Repository](https://github.com/Ductri2006/Telco-Customer-Churn-Duy-Tri) · [Experiment notebook](https://github.com/Ductri2006/Telco-Customer-Churn-Duy-Tri/blob/master/logistic_regression_telco_churn.ipynb)

### CalTrack / Multimodal integration

Food-photo analysis in a Flutter calorie tracker. Shared project, presented through my fork of the [upstream codebase](https://github.com/trangkhanh-ai/Calories-Tracking-App).

- The ASP.NET Core backend compresses images, calls Gemini, and parses a structured nutrition estimate.
- Provider credentials stay on the server; meal diaries are backed by the API.


Flutter · Dart · ASP.NET Core · Gemini · PostgreSQL

[My fork](https://github.com/Ductri2006/Calories-Tracking-App) · [Inference service](https://github.com/Ductri2006/Calories-Tracking-App/blob/main/backend/src/CaloriesTracking.Infrastructure/Services/GeminiFoodAnalysisService.cs) · [Demo](https://calories-tracking-app-ten.vercel.app/)

### Advisora / AI in application workflows

A consulting CRM portfolio project with an access-controlled case-summary workflow.

- Organization and staff-access checks precede context construction.
- Context uses selected case data and bounded text previews, excluding raw files and storage paths.
- Mock and optional external providers; summary outcomes feed an activity log.

TypeScript · React · Express · Prisma · PostgreSQL

[Repository](https://github.com/Ductri2006/Consulting-crm-system) · [Context & access logic](https://github.com/Ductri2006/Consulting-crm-system/blob/main/server/src/modules/ai/ai.service.ts)

## Engineering approach

- Separate training, validation, and test decisions.
- Inspect errors and threshold trade-offs, not accuracy alone.
- Treat model output as one part of a system with contracts, permissions, and failure paths.

---

<sub>THE HOUSE OF DUCTRI</sub>
