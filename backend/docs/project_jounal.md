# House Value Estimator — Project Journal

A day-by-day build log of a FastAPI + ML house price prediction service, from first endpoint to production deployment on Render with Docker and Git LFS.

---

## Sprint 1 — Project Structure & First API

**Completed**
- Created production folder structure.
- Created `main.py`.
- Created `house_schema.py`.
- Created `prediction_routes.py`.
- Created `prediction_service.py`.
- Connected API → Service architecture.

**Learned**
- A FastAPI application has only one `app` object.
- `APIRouter` is a mini application.
- Schemas validate requests before they reach the API.
- Services contain business logic.
- Routes should only coordinate requests.

**Bugs Fixed**
- `NameError: HouseFeatures not defined` — fixed by importing `HouseFeatures` in `prediction_routes.py`.

**Next Goal:** Build the ML Predictor layer.

---

## Sprint 2 — ML Layer Refactoring

**Goal:** Move prediction logic out of `main.py` into a production-style architecture.

**Completed**
- Created `app/ml/predictor.py`.
- Created `app/services/prediction_service.py`.
- Connected Route → Service → Predictor.
- Loaded the model only once using `joblib`.
- Used `pathlib` for robust model loading.
- Successfully tested `POST /predict`.

**Bugs Fixed**
- `FileNotFoundError` while loading `house_model.joblib` — fixed using `pathlib.Path(__file__).resolve().parent`.

**Concepts Learned**
- Separation of Concerns.
- Service layer vs. ML layer.
- Loading a model once.
- `Pydantic` `model_dump()`.
- Building a DataFrame for inference.

**Result:** Completed the first end-to-end production prediction flow.

---

## Sprint 3 — Configuration Management

**Completed**
- Created `core/config.py`.
- Centralized application configuration.
- Removed the hardcoded model path from `predictor.py`.
- Removed hardcoded prediction settings from `prediction_service.py`.
- Updated `main.py` to read application metadata from `config.py`.

**Learned**
- The difference between configuration and business logic.
- Why production applications avoid hardcoded values.
- Single Source of Truth (SSOT) principle.
- Don't Repeat Yourself (DRY) principle.
- Why backend refactoring often improves architecture without changing API responses.

---

## Sprint 4 — Logging & Exception Handling

**Completed**
- Created and configured a logger.
- Logged successful predictions.
- Logged exceptions using `logger.exception()`.
- Added proper exception handling with try/except.
- Intentionally triggered a 500 error to verify exception handling.
- Read and understood a real Python traceback.
- Fixed a real bug (`details` → `detail` in `HTTPException`).
- Verified the API works normally after removing the test exception.

**Learned**
- Difference between `logger.info()` and `logger.exception()`.
- HTTP 200 vs. 422 vs. 500.
- How requests move through the backend.
- Where validation happens.
- How exceptions are handled and debugged in production.
- Why logging is essential.
- These concepts transfer to Flask, FastAPI, Django, Spring Boot, ASP.NET, Node.js, and other backend frameworks.

---

## Sprint 5 — Centralized Logging

**Completed**
- [x] Centralized logger
- [x] Console logging
- [x] File logging
- [x] Exception logging
- [x] Execution time logging
- [x] Log rotation

---

## Sprint 6 — Intro to Pytest

**Learned**
- How `pytest` works.
- How `TestClient` works.
- What `assert` does.
- HTTP status codes (200, 404, 422, 500).
- How API responses are structured.
- How to write meaningful tests.

---

## Sprint 7 — First FastAPI Tests

**Completed**
- [x] `TestClient`
- [x] HTTP status code testing (200, 422)
- [x] Response validation
- [x] Mocking with `@patch`
- [x] `return_value`
- [x] `assert_called_once()`
- [x] Understanding why we patch where the function is *used*

---

## Sprint 8 — Mocking Deep Dive

**Completed**
- [x] `@patch`
- [x] `return_value`
- [x] `side_effect`
- [x] `assert_called_once()`
- [x] `assert_called_once_with()`
- [x] Concept of mocking multiple dependencies (theory)

---

## Sprint 9 — Fixtures & Parameterized Tests

**Fixtures**
- `@pytest.fixture`
- Reusable test data
- DRY principle

**Parameterized Tests**
- `@pytest.mark.parametrize`
- One test → multiple executions
- Dynamic test inputs

---

## Sprint 10 — Fixture Scopes & Pytest Config

**Completed**
- [x] Fixture scopes
- [x] Parameterized tests
- [x] `conftest.py`
- [x] Reading pytest output
- [x] Debugging common pytest errors

---

## Sprint 11 — Test Coverage & Integration Testing

**Completed**
- Installed `pytest-cov`.
- Measured code coverage.
- Added `integration_test.py`.
- Project now has **8 passing tests**.

**Learned**
- `Stmts` = executable lines.
- `Miss` = lines never executed.
- `Cover` = percentage of executed lines.
- Why mocking reduces coverage in the mocked dependency.
- How to interpret a coverage report.
- Difference between unit and integration testing.

---

## Sprint 12 — Continuous Integration (GitHub Actions)

**Goal:** Automate testing so every code change is verified before it's merged.

**Completed**
- Created a GitHub Actions workflow.
- Configured the workflow to trigger on every `git push`.
- Set up Python 3.11 in the CI environment.
- Installed project dependencies from `requirements.txt`.
- Executed the full pytest suite automatically.
- Successfully ran all tests in GitHub Actions.

**Problems Faced & Solutions**

| # | Problem | Cause | Solution |
|---|---------|-------|----------|
| 1 | GitHub rejected the push — `house_model.joblib` > 100 MB | Large model file | Removed model from repo, added to `.gitignore`, loaded model only when required |
| 2 | `ModuleNotFoundError: No module named 'app'` | Workflow running from the wrong directory | Updated workflow to run pytest from the correct project directory |
| 3 | `FileNotFoundError: house_model.joblib` | Model intentionally not stored in GitHub | Mocked the model in integration tests |
| 4 | Integration test tried to load the real model | Same as above | Patched `predict_price()` so the API returns a fake prediction while verifying endpoint behavior |

**Learned**
- Continuous Integration (CI) concepts.
- GitHub Actions workflow structure and YAML syntax.
- GitHub-hosted runners.
- Automated dependency installation and test execution.
- Why production projects mock external dependencies during CI.
- Difference between local testing and CI testing.
- Debugging CI failures using GitHub Actions logs.

**Result**
- [x] GitHub automatically runs the full test suite on every push.
- [x] All tests pass successfully.
- [x] Automated CI pipeline in place.

---

## Sprint 13 — Docker

**Goal:** Containerize the FastAPI application.

**Completed**
- Created a production-ready `Dockerfile`.
- Configured `.dockerignore` to exclude unnecessary files.
- Built the Docker image successfully.
- Ran the application inside a Docker container.
- Exposed the application via port mapping (`8000:8000`).
- Verified `/`, `/docs`, `/openapi.json`, and `POST /predict`.
- Debugged and fixed a build issue caused by a missing `COPY . .` instruction.

**Concepts Learned**
- Docker Image vs. Docker Container.
- Purpose of `FROM`, `WORKDIR`, `COPY`, `RUN`, and `CMD`.
- Docker layer caching.
- Purpose of `.dockerignore`.
- `0.0.0.0` (server bind address) vs. `localhost` (client access).
- Port mapping with `docker run -p host:container`.

**Debugging Story**
- Investigated `ModuleNotFoundError: No module named 'app'`.
- Verified project structure and added `app/__init__.py`.
- Found the application source code was never copied into the image.
- Fixed by adding `COPY . .`, then rebuilt and verified the container.

---

## Sprint 14 — Database & Prediction History

**Goal:** Persist prediction results so previous predictions can be stored and retrieved instead of existing only in memory.

**Completed**
- Added SQLite database + SQLAlchemy ORM.
- Created database configuration, models, and a `Prediction` model.
- Added database initialization and a database dependency for FastAPI.
- Created a prediction repository with `save_prediction()`.
- Saved every successful prediction to the database.
- Created a prediction-history service and `GET /predictions`.
- Added a `created_at` timestamp to prediction records.
- Verified records persist correctly.

**Architecture**

```
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
```

```
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
```

**Concepts Learned**
- SQLite, SQLAlchemy, ORM (Object Relational Mapping).
- Database models and sessions.
- Repository pattern.
- Database dependencies in FastAPI.
- CRUD concepts.
- Persisting ML prediction results.
- Separation between service and repository layers.

**Result:** The app can now store predictions permanently and retrieve history through an API endpoint.

---

## Sprint 15 — API Response Schemas

**Goal:** Separate database models from API response structures and make responses explicitly validated.

**Completed**
- Created `app/schemas/prediction_schema.py`.
- Created a `PredictionResponse` Pydantic schema.
- Defined the expected fields for the prediction-history API.
- Added datetime validation for `created_at`.
- Used `model_config = ConfigDict(from_attributes=True)`.
- Applied `PredictionResponse` to the `/predictions` endpoint.

**Concepts Learned**
- Difference between database models and API schemas.
- Pydantic response models and response validation.
- `from_attributes=True`.
- Why APIs should explicitly define their response structure.
- Separation of database layer and API layer.

**Result:** `/predictions` now returns data through a validated response schema instead of exposing database objects directly.

---

## Sprint 16 — Pagination & Validation

**Goal:** Prevent the prediction-history endpoint from returning too many records in a single request.

**Completed**
- Added pagination to `GET /predictions` using `skip` and `limit`.
  - Example: `/predictions?skip=0&limit=10`
- Added validation:
  ```python
  skip: int = Query(0, ge=0)
  limit: int = Query(10, ge=1, le=100)
  ```

**Validation Rules**
- `skip >= 0`
- `1 <= limit <= 100`

**Tests**
- `limit=101` → 422
- `limit=0` → 422
- `skip=-1` → 422

**Concepts Learned**
- Pagination and query parameters.
- FastAPI `Query`.
- Input validation and HTTP 422 Unprocessable Entity.
- Why pagination protects database performance.
- Why APIs should enforce reasonable request limits.

**Result:** The prediction-history API now supports controlled, paginated queries.

---

## Sprint 17 — Automated API Testing Expansion

**Goal:** Expand the test suite as new production features are added.

**Completed** — added tests for:
- Prediction endpoint
- Prediction history
- Pagination validation
- Health endpoint
- Error handling
- Integration testing
- Fixtures
- Parameterized inputs
- Rate limiting

**Result:** Test suite grew from 8 tests to **14 passed** (before rate limiting was added).

**Concepts Learned**
- Regression testing.
- Test organization.
- Testing new features without breaking existing functionality.
- Using pytest as a safety net during refactoring.

---

## Sprint 18 — Rate Limiting

**Goal:** Protect the expensive ML prediction endpoint from excessive requests.

**Completed**
- Installed `slowapi`.
- Created `app/core/rate_limiter.py`.
- Configured a shared limiter using the client's IP address.
- Connected the limiter to FastAPI in `app/main.py`.
- Applied `@limiter.limit("20/minute")` to `POST /predict`.
- Added `request: Request` to the prediction endpoint so SlowAPI can identify the client.

**Rate Limit:** 20 requests / minute / client IP → exceeding it returns `HTTP 429 Too Many Requests`.

**Testing**
- Created `tests/test_rate_limit.py`.
- Sent 21 prediction requests and verified the 21st returns `429`.
- **Final result: 15 passed, 1 warning** (a harmless Starlette/httpx deprecation warning).

**Concepts Learned**
- API rate limiting and middleware.
- Client/IP-based request limiting.
- HTTP 429 Too Many Requests.
- Protecting expensive ML endpoints.
- Automated testing of rate limits.

---

## Sprint 19 — Project Cleanup & Test Isolation

**Goal:** Improve test reliability and remove unnecessary project files.

**Completed**
- Fixed test database isolation using an in-memory SQLite database.
- Overrode FastAPI's `get_db` dependency during tests.
- Verified tests don't modify the real `data/prediction.db`.
- Removed duplicate test files, empty `explore.py`, and empty `docker-compose.yml`.
- Removed unnecessary old test code while keeping learning comments.
- Reduced test suite from 15 tests to 13 (all passing).

**Problems & Solutions**

| Problem | Solution |
|---|---|
| Tests were connected to the real database | Created a separate `sqlite://` in-memory test database using `StaticPool` and FastAPI dependency overrides |
| `requirements.txt` saved as UTF-16 on Windows | Regenerated as UTF-8 |
| Duplicate/unused files existed | Removed them |

**Verification**
- [x] Prediction history test: 1 passed
- [x] Full test suite: 13 passed
- [x] Real `data/prediction.db`: unchanged after testing

**Learned**
- Why test isolation matters.
- How FastAPI dependency overrides work.
- Difference between a real application database and a test database.
- How to safely clean duplicate/dead code.
- Why file encoding matters for GitHub and Docker.

**Result**
- [x] Tests isolated from the real database
- [x] 13 tests passing
- [x] Duplicate/unused files removed
- [x] `requirements.txt` encoding issue resolved
- [x] Local and remote `main` synchronized

---

## Sprint 20 — Auth, CI & Final Local Verification

**Completed**
- [x] 16/16 tests passing locally
- [x] API authentication tested
- [x] Integration testing isolated from `.joblib`
- [x] Rate limiting tested
- [x] Pagination tested
- [x] Prediction history tested
- [x] CI workflow configured
- [x] API key stored as a GitHub Secret
- [x] `.env` remains local
- [x] No `.joblib` committed
- [x] Git working tree clean, in sync with GitHub

---

## Sprint 21 — Docker Hardening & Verification

**Completed**
- [x] Docker image builds successfully
- [x] `.env` not included in the image
- [x] `.joblib` files not included in the image
- [x] Model mounted separately and loaded lazily
- [x] API key passed through environment variables
- [x] Wrong/missing API key → 401, correct key → 200
- [x] `/`, `/docs`, `/health` all work
- [x] Prediction works inside Docker
- [x] Tests pass locally: 16/16
- [x] CI already configured

**Debugging Notes**
- Docker dependency installation issue.
- Docker image build issue.
- Docker container startup verification.
- Model availability inside Docker.
- API authentication verification.
- UTF-16 encoding problem.
- Git binary-file detection problem.
- Git line-ending configuration.

---

## Sprint 22 — Production Deployment & ML Model Fix

**Objective:** Deploy the House Value Estimator API to Render using Docker, and fix the production `/predict` endpoint.

### 1. Docker + Render Deployment

Successfully deployed the FastAPI app to Render using Docker. Verified:
- Docker container starts successfully.
- Uvicorn runs on Render's dynamic `$PORT`.
- `/` → 200 OK, `/health` → 200 OK, `/docs` → 200 OK.
- Swagger/OpenAPI loads correctly.

Docker command updated to support Render's dynamic port:

```bash
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

This allows:
- Local Docker → port 8000
- Render → automatically uses Render's `$PORT`

### 2. Production `/predict` Error

Initially returned `500 Internal Server Error`. Render logs showed:

```
FileNotFoundError: [Errno 2] No such file or directory:
'/app/app/ml/house_model.joblib'
```

The FastAPI app was working, but the ML model wasn't available inside the Render Docker container.

### 3. Root Cause

`house_model.joblib` (~145 MB) was excluded via `.gitignore` because GitHub's normal file size limit made committing it directly inappropriate.

```
Local machine → model exists
     ↓
.gitignore excluded it
     ↓
GitHub didn't contain it
     ↓
Render couldn't download it
     ↓
Docker didn't contain it
     ↓
/predict → FileNotFoundError
```

### 4. Solution — Git LFS

```bash
git lfs version
# git-lfs/3.6.1

git lfs track app/ml/house_model.joblib
```

This created `backend/.gitattributes`:

```
app/ml/house_model.joblib filter=lfs diff=lfs merge=lfs -text
```

- Removed both model files from `.gitignore`.
- `house_model.joblib` is now managed by Git LFS.
- The small `house_features.joblib` stays in regular Git.

### 5. Verification

```bash
git lfs ls-files
# 97b5974f74 * backend/app/ml/house_model.joblib

git commit -m "fix: track ML model with Git LFS"
git commit -m "chore: allow ML model files"
git push origin main
# Uploading LFS objects: 100% (1/1), 145 MB
```

### 6. Final Production Test

Render automatically rebuilt from the new commit. After redeployment:

**`POST /predict` → 200 OK**

The production API successfully loaded the ML model and generated a prediction.

### Final Architecture

```
GitHub
   ↓
Git LFS
   ↓
145 MB ML model
   ↓
Render
   ↓
Docker build
   ↓
FastAPI
   ↓
Random Forest model
   ↓
POST /predict
   ↓
200 OK
```