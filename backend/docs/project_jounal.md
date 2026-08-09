## sprint 1

Completed:
- Created production folder structure.
- Created main.py.
- Created house_schema.py.
- Created prediction_routes.py.
- Created prediction_service.py.
- Connected API → Service architecture.

Learned:
- FastAPI application has only one app object.
- APIRouter is a mini application.
- Schema validates requests before they reach the API.
- Services contain business logic.
- Routes should only coordinate requests.

Problems Faced:
- NameError: HouseFeatures not defined.
- Fixed by importing HouseFeatures in prediction_routes.py.

Next Goal:
- Build ML Predictor Layer.


day 2----------------------------------------------------------------------------------------------------


# Sprint 3 - ML Layer Refactoring

## Goal
Move prediction logic out of main.py into a production-style architecture.

## Completed
- Created app/ml/predictor.py
- Created app/services/prediction_service.py
- Connected Route → Service → Predictor
- Loaded model only once using joblib
- Used pathlib for robust model loading
- Successfully tested POST /predict

## Bugs Fixed
- FileNotFoundError while loading house_model.joblib
- Fixed using pathlib.Path(__file__).resolve().parent

## Concepts Learned
- Separation of Concerns
- Service Layer
- ML Layer
- Loading model once
- Pydantic model_dump()
- DataFrame creation for inference

## Result
Successfully completed the first end-to-end production prediction flow.

## Next Sprint
Configuration Management (app/core/config.py)

We'll write this in your project journal later:

## Sprint 4 - Configuration Management

What we changed

Created core/config.py.
Centralized application configuration.
Removed the hardcoded model path from predictor.py.
Removed hardcoded prediction settings from prediction_service.py.
Updated main.py to read application metadata from config.py.

What I learned

The difference between configuration and business logic.
Why production applications avoid hardcoded values.
The Single Source of Truth (SSOT) principle.
The Don't Repeat Yourself (DRY) principle.
Why backend refactoring often improves architecture without changing API responses.

## sprint 5 - Logging 

Created a logger.
Configured logging.
Logged successful predictions.
Logged exceptions using logger.exception().
Understood the difference between logger.info() and logger.exception().
Tested exception handling by intentionally raising an exception.
Understood HTTP 422 vs HTTP 500.


Added proper exception handling using try-except.
Learned the difference between logger.info() and logger.exception().
Understood 200, 422, and 500 HTTP status codes.
Intentionally triggered a 500 error to verify exception handling.
Read and understood a real Python traceback.
Fixed a real bug (details → detail in HTTPException).
Verified that your API works normally after removing the test exception.
Wrote today's journal entry.
What you learned

Today t gained experience that applies to almost every backend framework:

How requests move through the backend.
Where validation happens.
How exceptions are handled.
How developers debug production issues.
Why logging is essential.

These concepts transfer to Flask, FastAPI, Django, Spring Boot, ASP.NET, Node.js, and many other backend frameworks.

## sprint 6 LOgging 

Centralized logger
✅ Console logging
✅ File logging
✅ Exception logging
✅ Execution time logging
✅ Log rotation

## spirint 7

How pytest works
✅ How TestClient works
✅ What assert does
✅ HTTP status codes (200, 404, 422, 500)
✅ How API responses are structured
✅ How to write meaningful tests

## sprint 8

First FastAPI tests
✅ TestClient
✅ HTTP status code testing (200, 422)
✅ Response validation
✅ Mocking with @patch
✅ return_value
✅ assert_called_once()
✅ Understanding why we patch where the function is used

## sprint 9

@patch
✅ return_value
✅ side_effect
✅ assert_called_once()
✅ assert_called_once_with()
✅ The concept of mocking multiple dependencies mostly theory

## sprint 10

Fixtures

@pytest.fixture
Reusable test data
DRY principle

Parameterized Tests

@pytest.mark.parametrize
One test → multiple executions
Dynamic test inputs

## sprint 11

Fixture scopes
✅ Parameterized tests
✅ conftest.py
✅ Reading pytest output
✅ Debugging common pytest errors

# sprint 12

Installed pytest-cov.
Measured code coverage.
Understood:
Stmts = executable lines.
Miss = lines never executed.
Cover = percentage of executed lines.
Learned why mocking reduces coverage in the mocked dependency.
Learned how to interpret a coverage report.
--------------------------------------------------------
Test Coverage (pytest-cov)
Reading the coverage report
Understanding:
Stmts
Miss
Cover
Why mocking affects coverage
Integration Testing
Difference between Unit vs Integration testing
Added integration_test.py
Now your project has 8 passing tests 🎉

-------------------------------------
#13 passed github action

Sprint 13 – Continuous Integration (GitHub Actions)
Goal

Automate testing so every code change is verified before it is merged.

Completed
Created GitHub Actions workflow.
Configured workflow to trigger on every git push.
Set up Python 3.11 in the CI environment.
Installed project dependencies from requirements.txt.
Executed the complete pytest test suite automatically.
Successfully ran all tests in GitHub Actions.
Problems Faced
1. Large model file

GitHub rejected the push because:

house_model.joblib > 100 MB

Solution

Removed the model from the repository.
Added it to .gitignore.
Modified the application to load the model only when required.
2. Module import error
ModuleNotFoundError: No module named 'app'

Cause

The GitHub Actions workflow was running from the wrong directory.

Solution

Updated the workflow so pytest runs inside the correct project directory.

3. Missing ML model during CI
FileNotFoundError:
house_model.joblib

Cause

The trained model is intentionally not stored in GitHub.

Solution

Used mocking in the integration tests so GitHub Actions does not require the real model.

4. Integration test failure

The integration test initially attempted to load the real ML model.

Solution

Patched predict_price() during the test so the API returns a fake prediction while verifying endpoint behavior.

What I Learned
Continuous Integration (CI)
GitHub Actions workflow structure
YAML syntax
GitHub-hosted runners
Automated dependency installation
Automated test execution
Why production projects mock external dependencies during CI
Difference between local testing and CI testing
Debugging CI failures using GitHub Actions logs
Result

✅ GitHub automatically runs the complete test suite on every push.

✅ All tests pass successfully.

✅ The project now has an automated Continuous Integration pipeline.


### Sprint 14 – Docker
Goal

Containerize the FastAPI application.

Completed
Created a production-ready Dockerfile.
Configured .dockerignore to exclude unnecessary files.
Built the Docker image successfully.
Ran the application inside a Docker container.
Exposed the application using port mapping (8000:8000).
Verified:
Home endpoint (/)
Swagger Docs (/docs)
OpenAPI schema (/openapi.json)
Prediction endpoint (POST /predict)
Debugged and fixed a Docker build issue caused by a missing COPY . . instruction.
Concepts Learned
Difference between Docker Image and Docker Container.
Purpose of FROM, WORKDIR, COPY, RUN, and CMD.
Docker layer caching.
Purpose of .dockerignore.
Difference between 0.0.0.0 (server bind address) and localhost (client access).
Port mapping with docker run -p host:container.
Real Debugging Experience
Investigated ModuleNotFoundError: No module named 'app'.
Verified project structure.
Added app/__init__.py.
Identified that the application source code was never copied into the image.
Fixed the issue by adding:
COPY . .
Successfully rebuilt and verified the container.

##### Sprint 15 – Database & Prediction History
Goal

Persist prediction results in a database so previous predictions can be stored and retrieved instead of existing only in memory.

Completed
Added SQLite database.
Added SQLAlchemy ORM.
Created database configuration.
Created database models.
Created Prediction model.
Added database initialization.
Created database dependency for FastAPI.
Created prediction repository.
Added save_prediction() functionality.
Saved every successful prediction to the database.
Created prediction-history service.
Added:
GET /predictions
Verified prediction records were persisted successfully.
Added created_at timestamp to prediction records.
Architecture
POST /predict
      ↓
Prediction Route
      ↓
Prediction Service
      ↓
ML Predictor
      ↓
Prediction Result
      ↓
SQLAlchemy ORM
      ↓
SQLite Database

For retrieving history:

GET /predictions
      ↓
Prediction Route
      ↓
Prediction Service
      ↓
Repository
      ↓
SQLAlchemy
      ↓
SQLite
Concepts Learned
SQLite.
SQLAlchemy.
ORM (Object Relational Mapping).
Database models.
Database sessions.
Repository pattern.
Database dependencies in FastAPI.
CRUD concepts.
Persisting ML prediction results.
Separation between service and repository layers.
Result

The application can now store prediction results permanently and retrieve previous predictions through an API endpoint.

### sprint 16 – API Response Schemas
Goal

Separate database models from API response structures and make API responses explicitly validated.

Completed
Created app/schemas/prediction_schema.py.
Created PredictionResponse Pydantic schema.
Defined the expected fields returned by the prediction-history API.
Added datetime validation for created_at.
Used:
model_config = ConfigDict(from_attributes=True)
Applied PredictionResponse to the /predictions endpoint.
Concepts Learned
Difference between database models and API schemas.
Pydantic response models.
Response validation.
from_attributes=True.
Why APIs should explicitly define their response structure.
Separation of database layer and API layer.
Result

The /predictions endpoint now returns data through a validated response schema instead of exposing database objects directly.

Sprint 16 – Pagination & Validation
Goal

Prevent the prediction-history endpoint from returning an unnecessarily large number of database records in a single request.

Completed

Added pagination to:

GET /predictions

Using:

skip
limit

Example:

/predictions?skip=0&limit=10

Added validation:

skip: int = Query(0, ge=0)
limit: int = Query(10, ge=1, le=100)
Validation Rules
skip >= 0
1 <= limit <= 100

Tested invalid requests:

limit=101  → 422
limit=0    → 422
skip=-1    → 422
Concepts Learned
Pagination.
Query parameters.
FastAPI Query.
Input validation.
HTTP 422 Unprocessable Entity.
Why pagination protects database performance.
Why APIs should enforce reasonable request limits.
Result

The prediction-history API now supports controlled, paginated database queries.

## Sprint 17 – Automated API Testing Expansion
Goal

Expand the automated test suite as new production features are added.

Completed

Added tests for:

Prediction endpoint.
Prediction history.
Pagination validation.
Health endpoint.
Error handling.
Integration testing.
Fixtures.
Parameterized inputs.
Rate limiting.

Test suite progressed from the earlier 8 tests to:

14 passed

before rate limiting was added.

Concepts Learned
Regression testing.
Test organization.
Testing new features without breaking existing functionality.
Using pytest as a safety net during refactoring.
### Sprint 18 – Rate Limiting
Goal

Protect the expensive ML prediction endpoint from excessive requests and prevent unnecessary model/database processing.

Completed

Installed:

slowapi

Created:

app/core/rate_limiter.py

Configured a shared limiter using the client's IP address.

Connected the limiter to FastAPI in:

app/main.py

Applied rate limiting specifically to:

POST /predict

using:

@limiter.limit("20/minute")

Added:

request: Request

to the prediction endpoint so SlowAPI can identify the client.

Rate Limit
20 requests / minute / client IP

When the limit is exceeded:

HTTP 429 Too Many Requests
Testing

Created:

tests/test_rate_limit.py

The test sends 21 prediction requests and verifies that the request exceeding the limit returns:

429
Final Test Result
15 passed
1 warning

The warning is a Starlette/httpx deprecation warning and does not cause test failure.

Concepts Learned
API rate limiting.
SlowAPI.
Middleware.
Client/IP-based request limiting.
HTTP 429 Too Many Requests.
Protecting expensive ML endpoints.
Automated testing of rate limits.
Result

The /predict endpoint is now protected against excessive requests.

## sprint 19

Project Cleanup & Test Isolation
Goal

Improve test reliability and remove unnecessary project files.

Completed
Fixed test database isolation using an in-memory SQLite database.
Overrode FastAPI's get_db dependency during tests.
Verified tests do not modify the real data/prediction.db.
Removed duplicate test files.
Removed empty explore.py.
Removed empty docker-compose.yml.
Removed unnecessary old test code while keeping learning comments.
Reduced test suite from 15 tests to 13 tests.
Verified all 13 tests pass.
Problems Faced
Tests were connected to the real database.
requirements.txt had previously been saved as UTF-16 on Windows.
Duplicate test files existed.
Empty unused files existed.
Solutions
Created a separate sqlite:// in-memory test database.
Used StaticPool and FastAPI dependency overrides.
Regenerated requirements.txt as UTF-8.
Removed duplicate and unused files.
Re-ran the complete test suite after cleanup.
Verification
Prediction history test: 1 passed
Full test suite: 13 passed
Real data/prediction.db: unchanged after testing
What I Learned
Why test isolation is important.
How FastAPI dependency overrides work.
Difference between a real application database and a test database.
How to safely clean duplicate/dead code.
Why file encoding matters for GitHub and Docker.