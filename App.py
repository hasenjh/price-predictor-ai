import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data (replace with real one later)
data = {
    'marketing_spend': [100, 200, 300, 400, 500],
    'social_followers': [1000, 1500, 2000, 2500, 3000],
    'ratings': [4.2, 4.5, 4.8, 5.0, 5.0],
    'price': [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)

# Train model
X = df[['marketing_spend', 'social_followers', 'ratings']]
y = df['price']
model = LinearRegression()
model.fit(X, y)

# UI
st.title("🔮 Price Prediction AI Tool")

marketing = st.slider("Marketing Spend", 100, 1000, 300)
followers = st.slider("Followers", 500, 5000, 2000)
rating = st.slider("Product Rating", 1.0, 5.0, 4.5)

sample = [[marketing, followers, rating]]
prediction = model.predict(sample)[0]

st.success(f"Predicted Price: ${prediction:.2f}")
