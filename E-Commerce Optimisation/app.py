from fastapi import FastAPI, HTTPException, UploadFile, File, status
import pandas as pd
from io import StringIO
from tabs.bonus_computer_vision import (
    predict_product_category,
    load_product_categorisation_model,
    search_similar_products,
)
from tabs.bonus_sentiment_analysis import get_vader_score, load_vader
from tabs.bonus_personalized_email import generate_personalized_email_h2o
from tabs.bonus_ai_chatbot import get_recommendation
from demand_forecast.demand_forecasting import load_model_and_predict

app = FastAPI(
    title="Passion8", description="Ecommerce Analysis and Optimization", version="0.1.0"
)


@app.post("/bonus/analyse_sentiment", tags=["Bonus"])
async def analyse_sentiment(review: str):
    try:
        model = load_vader()
        score = get_vader_score(review, model)
        if score >= 0.5:
            return {"sentiment": "Positive"}
        elif score <= -0.5:
            return {"sentiment": "Negative"}
        else:
            return {"sentiment": "Neutral"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.post("/bonus/classify_product", tags=["Bonus"])
async def classify_product_image(file: UploadFile):
    try:
        model = load_product_categorisation_model()
        product_category = predict_product_category(model, file.file.read())
        return {"product_category": product_category}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.post("/bonus/search_similar_products", tags=["Bonus"])
async def search_similar_products_endpoint(file: UploadFile, number_of_products: int):
    try:
        similar_products = search_similar_products(file.file.read(), number_of_products)
        similar_products_link = [i[0] for i in similar_products]
        return {"similar_products": similar_products_link}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.post("/bonus/generate_personalized_email", tags=["Bonus"])
async def generate_personalized_email(user_id: int):
    try:
        email_content = generate_personalized_email_h2o(user_id)
        return {"email_content": email_content}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.post("/bonus/get_product_recommendation", tags=["Bonus"])
async def get_product_recommendation(user_query: str):
    try:
        chat_session_id = None
        recommendation = get_recommendation(chat_session_id, user_query)
        return {"recommendation": recommendation}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.post("/grpb/demand_forecast", tags=["Demand Forecast"])
async def predict_sales(
    test_data: UploadFile = File(...), trained_model_file: UploadFile = File(...)
):
    try:
        # Load test data
        test_df = pd.read_csv(StringIO((await test_data.read()).decode("utf-8")))

        # Save the model file temporarily to use it
        model_path = "/tmp/model.txt"
        with open(model_path, "wb") as f:
            f.write(await trained_model_file.read())

        # Load model and make predictions
        predictions_df = load_model_and_predict(model_path, test_df)

        # Return predictions as JSON
        return {"predictions": predictions_df.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
