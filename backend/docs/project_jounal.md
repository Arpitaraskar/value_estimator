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