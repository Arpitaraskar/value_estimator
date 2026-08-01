# from fastapi.testclient import TestClient
# from main import app

# #create fake user who can send request to my fastapi application
# client = TestClient(app)


# def test_home():

#     #hey 1 fastAPI i am visiting the home the home page(/)""
#     response = client.get("/")
#     assert response.status_code ==200
#     assert response.json()=={"message":"welcome"}





# client - TestClient(app)

# def test_about():

#     response = client.get("/about")

#     assert response.status_code == 200
#     assert response.json() == {"name":"house predication API"}

# data={

# }

# def test_predict():

#     response = client.post("/prediction",
#                            json={
#                               " MedInc":10,
#                                "HouseAge":2,
#                                "AveRooms":2,
#                                "AveBedroom":5

                               
#                            })

#     assert response.status_code == 200
#     assert response.json()=={
#         "predicated_price":220000
#     }

#     #mocking testing practice

# @patch("app.services.prediction_service.predict_price")
# def test_predict(mock_predict):

#     mock_predict.return_value = 5

#     response = client.post("/predict",
#                            json= {
#                                "MedInc":10,
#                                "HouseAge":10
#                            })
#     assert response.status_code == 200
#     assert response.json()=={

#     "predicated_price":"$500,000"
#     }

#     mock_predict.assert_called_once_with(500,000)


    



