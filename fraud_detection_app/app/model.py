import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, LabelEncoder
from imblearn.over_sampling import SMOTE
import joblib

def preprocess_and_train():
    df = pd.read_csv('data/Fraud.csv')

    # Data type optimization
    df['isFlaggedFraud'] = df['isFlaggedFraud'].astype('int8')
    df['amount'] = df['amount'].astype('float32')
    df['newbalanceOrig'] = df['newbalanceOrig'].astype('float32')
    df['newbalanceDest'] = df['newbalanceDest'].astype('float32')
    df['type'] = df['type'].astype('category')

    # Drop irrelevant columns
    df.drop(['nameOrig', 'nameDest', 'step', 'oldbalanceDest', 'oldbalanceOrg'], axis=1, inplace=True)

    # Encode type
    le = LabelEncoder()
    df['transaction_type'] = le.fit_transform(df['type'])
    df.drop('type', axis=1, inplace=True)

    # Scale
    scaler = RobustScaler()
    df[['amount', 'newbalanceOrig', 'newbalanceDest']] = scaler.fit_transform(
        df[['amount', 'newbalanceOrig', 'newbalanceDest']]
    )

    # Train/test split
    X = df.drop('isFraud', axis=1)
    y = df['isFraud']
    X_train, _, y_train, _ = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    # Handle imbalance
    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X_train, y_train)

    # Train model
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X_res, y_res)

    # Save model
    joblib.dump(model, 'model/fraud_model.pkl')
    print("✅ Model trained and saved to 'model/fraud_model.pkl'")

if __name__ == "__main__":
    preprocess_and_train()
